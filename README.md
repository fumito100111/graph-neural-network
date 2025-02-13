# GNN for PPI (Protein-Protein Interaction)
## Contents
- [GNN for PPI (Protein-Protein Interaction)](#gnn-for-ppi-protein-protein-interaction)
  - [Contents](#contents)
  - [Reference](#reference)
    - [「 The Graph Neural Network Model 」](#-the-graph-neural-network-model-)
  - [Development environment](#development-environment)
  - [How to set up](#how-to-set-up)
    - [1. Clone this repository](#1-clone-this-repository)
    - [2. Create virtual environment for Python](#2-create-virtual-environment-for-python)
    - [3. Download dataset of PPI](#3-download-dataset-of-ppi)

## Reference
### 「 The Graph Neural Network Model 」
> [Franco Scarselli, Marco Gori, Ah Chung Tsoi, Markus Hagenbucher, and Gabriele Monfardini. The graph neural network model. IEEE transactions on neural networks, Vol. 20, No. 1, pp. 61-80, 2008](https://ieeexplore.ieee.org/document/4700287)

## Development environment
```
macOS    - Sonoma 14.x.x
python   - v3.13.0
pip      - v25.0.1
jupyter  - v1.1.1
notebook - v7.3.2
torch    - v2.6.0
numpy    - v2.2.2
```
## How to set up
### 1. Clone this repository
```zsh {iscopy=true}
git clone https://github.com/fumito100111/gnn-for-ppi.git
cd gnn-for-ppi
```
### 2. Create virtual environment for Python
```zsh {iscopy=true}
python3 -m venv .venv
source .venv/bin/activate
.venv/bin/python3 pip install --upgrade pip
.venv/bin/python3 pip install jupyter notebook
.venv/bin/python3 pip install torch
.venv/bin/python3 pip install numpy
```
### 3. Download dataset of PPI
```zsh {iscopy=true}
mkdir dataset
curl -o dataset/proteins.zip https://nrvis.com/download/data/labeled/proteins.zip
unzip -d dataset/proteins dataset/proteins.zip
rm dataset/proteins.zip
rm dataset/proteins/readme.html
```
> Network Data Repository - PROTEINS: https://networkrepository.com/proteins.php