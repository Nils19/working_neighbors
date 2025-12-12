import numpy as np
import random
import torch
from tasks.tree_dataset import TreeDataset

class TreeNeighborsMatchDataset(TreeDataset):
    def __init__(self, depth):
        super(TreeNeighborsMatchDataset, self).__init__(depth)
        self.num_leaves = len(self.leaf_indices)
        self.num_colors = self.num_leaves
    
    def get_combinations(self):
        """Generate 32000 random examples with unique blue counts per leaf."""
        num_leaves = self.num_leaves
        max_examples = 32000
        
        combinations = []
        
        print(f"Generating {max_examples} examples for {num_leaves} leaves...")
        
        for i in range(max_examples):
            # Random permutation of blue counts (each leaf gets unique count)
            leaf_blue_counts = tuple(np.random.permutation(num_leaves))
            
            # Random target blue count
            target_blue_count = random.randint(0, num_leaves - 1)
            
            combinations.append((target_blue_count, leaf_blue_counts))
            
            if (i + 1) % 1000 == 0:
                print(f"Generated {i + 1}/{max_examples} examples...")
        
        print(f"Completed: {len(combinations)} combinations")
        return combinations
    
    def get_nodes_features(self, combination):
        """Return features as (node_type_id, blue_count_id) tuples."""
        target_blue_count, leaf_blue_counts = combination
        
        nodes = []
        
        # Root node: (root_marker, blue_count)
        root_type_id = self.num_leaves  # Use num_leaves as root marker
        nodes.append((root_type_id, target_blue_count))
        
        # Other nodes
        for i in range(1, self.num_nodes):
            if i in self.leaf_indices:
                # Leaf node: (leaf_index, blue_count)
                leaf_idx = self.leaf_indices.index(i)
                nodes.append((leaf_idx, leaf_blue_counts[leaf_idx]))
            else:
                # Intermediate node: (intermediate_marker, 0)
                intermediate_marker = self.num_leaves + 1
                nodes.append((intermediate_marker, 0))
        
        return nodes
    def label(self, combination):
        """Return the leaf index whose blue_count matches target's blue_count."""
        target_blue_count, leaf_blue_counts = combination
        
        for leaf_idx, blue_count in enumerate(leaf_blue_counts):
            if blue_count == target_blue_count:
                return leaf_idx
        
        raise ValueError(f"No leaf matches target blue count {target_blue_count}!")
    
    def get_dims(self):
        """
        Input dimension: concatenated one-hot vectors
        Output dimension: number of leaves
        """
        # Input: [one-hot(node_type) || one-hot(blue_count)]
        node_type_size = self.num_leaves + 2
        blue_count_size = self.num_leaves
        in_dim = node_type_size + blue_count_size
        
        out_dim = self.num_leaves
        
        return in_dim, out_dim