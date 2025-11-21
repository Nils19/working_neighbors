# Use official TensorFlow 1.x image (CPU, Python 3.7 + TF 1.15.5)
FROM tensorflow/tensorflow:1.15.5-py3

ENV PYTHONUNBUFFERED=1

# Basics
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Conservative toolchain for TF1-era deps
RUN pip install --no-cache-dir --upgrade pip==20.3.4 setuptools==49.6.0 wheel==0.36.2

# Keep TF stack consistent; (re)pin some libs
RUN pip install --no-cache-dir numpy==1.16.4 scipy==1.2.3 gast==0.2.2 keras==2.2.5

# Put repo in /workspace
WORKDIR /workspace
COPY . /workspace

# Install project deps but DON'T let them alter TensorFlow
WORKDIR /workspace/tf-gnn-samples
RUN pip install --no-cache-dir -r requirements.txt --no-deps || true
# Add the few packages the runner uses explicitly
RUN pip install --no-cache-dir dpu-utils docopt regex tqdm networkx==2.3 scikit-learn==0.22.2.post1
# (add rdkit-pypi==2021.9.4 only if QM9 featurization complains about RDKit)
