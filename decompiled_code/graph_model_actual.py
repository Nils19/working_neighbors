import torch
from torch import nn
from torch.nn import functional as F

class GraphModel(torch.nn.Module):
    def __init__(self, gnn_type, num_layers, dim0, h_dim, out_dim, last_layer_fully_adjacent,
                 unroll, layer_norm, use_activation, use_residual):
        super(GraphModel, self).__init__()
        self.gnn_type = gnn_type
        self.unroll = unroll
        self.last_layer_fully_adjacent = last_layer_fully_adjacent
        self.use_layer_norm = layer_norm
        self.use_activation = use_activation
        self.use_residual = use_residual
        
        # Device selection: CUDA > MPS > CPU
        if torch.cuda.is_available():
            self.device = torch.device('cuda')
        elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
            self.device = torch.device('mps')
        else:
            self.device = torch.device('cpu')

        self.num_layers = num_layers
        
        # Use embeddings instead of linear layer
        self.layer0_keys = nn.Embedding(num_embeddings=dim0 + 1, embedding_dim=h_dim)
        self.layer0_values = nn.Embedding(num_embeddings=dim0 + 1, embedding_dim=h_dim)
        
        self.layers = nn.ModuleList()
        self.layer_norms = nn.ModuleList()
        if unroll:
            self.layers.append(gnn_type.get_layer(in_dim=h_dim, out_dim=h_dim))
        else:
            for i in range(num_layers):
                self.layers.append(gnn_type.get_layer(in_dim=h_dim, out_dim=h_dim))
        
        if self.use_layer_norm:
            for i in range(num_layers):
                self.layer_norms.append(nn.LayerNorm(h_dim))

        self.out_dim = out_dim
        self.out_layer = nn.Linear(in_features=h_dim, out_features=out_dim, bias=False)
    
    def forward(self, data):
        x, edge_index, batch = data.x, data.edge_index, data.batch
        
        # Check if this is a tree task
        is_tree_task = hasattr(data, 'root_mask')
        
        if is_tree_task:
            roots = data.root_mask
            # Extract key and value from two columns
            x_key, x_val = x[:, 0], x[:, 1]
            x_key_embed = self.layer0_keys(x_key)
            x_val_embed = self.layer0_values(x_val)
            x = x_key_embed + x_val_embed
        else:
            # For non-tree tasks (if any)
            x_key, x_val = x[:, 0], x[:, 1]
            x_key_embed = self.layer0_keys(x_key)
            x_val_embed = self.layer0_values(x_val)
            x = x_key_embed + x_val_embed

        # GNN layers
        for i in range(self.num_layers):
            if self.unroll:
                layer = self.layers[0]
            else:
                layer = self.layers[i]
            
            if self.last_layer_fully_adjacent and i == self.num_layers - 1:
                if is_tree_task:
                    root_indices = torch.nonzero(roots, as_tuple=False).squeeze(-1)
                    target_roots = root_indices.index_select(dim=0, index=batch)
                    source_nodes = torch.arange(0, data.num_nodes).to(self.device)
                    edges = torch.stack([source_nodes, target_roots], dim=0)
                else:
                    edges = self._make_fully_connected(data.num_nodes, batch)
            else:
                edges = edge_index
            
            new_x = layer(x, edges)
            
            if self.use_activation:
                new_x = F.relu(new_x)
            
            if self.use_residual:
                x = x + new_x
            else:
                x = new_x
            
            if self.use_layer_norm:
                x = self.layer_norms[i](x)

        # Output layer
        if is_tree_task:
            root_nodes = x[roots]
            logits = self.out_layer(root_nodes)
        else:
            logits = self.out_layer(x)
        
        return logits
    
    def _make_fully_connected(self, num_nodes, batch):
        """Create fully connected edges within each graph in the batch."""
        edges = []
        
        unique_batches = torch.unique(batch)
        
        for batch_idx in unique_batches:
            node_mask = (batch == batch_idx)
            graph_nodes = torch.nonzero(node_mask, as_tuple=False).squeeze(-1)
            
            for i in graph_nodes:
                for j in graph_nodes:
                    if i != j:
                        edges.append([i.item(), j.item()])
        
        if len(edges) == 0:
            return edge_index
        
        return torch.tensor(edges, device=self.device).t()