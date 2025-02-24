# Graph Neural Network (GNN)
## Contents
- [Graph Neural Network (GNN)](#graph-neural-network)
  - [Contents](#contents)
  - [Reference](#reference)
    - [「 The Graph Neural Network Model 」](#-the-graph-neural-network-model-)
  - [Development environment](#development-environment)
  - [How to set up](#how-to-set-up)
    - [1. Clone this repository](#1-clone-this-repository)
    - [2. Create virtual environment for Python](#2-create-virtual-environment-for-python)

## Reference
### 「 The Graph Neural Network Model 」
> [Franco Scarselli, Marco Gori, Ah Chung Tsoi, Markus Hagenbucher, and Gabriele Monfardini. The graph neural network model. IEEE transactions on neural networks, Vol. 20, No. 1, pp. 61-80, 2008](https://ieeexplore.ieee.org/document/4700287)

## Development environment
```
macOS      - Sonoma 14.x.x
python     - v3.13.0
pip        - v25.0.1
jupyter    - v1.1.1
notebook   - v7.3.2
torch      - v2.6.0
numpy      - v2.2.2
networkx   - v.3.4.2
matplotlib - v3.10.0
```
## How to set up
### 1. Clone this repository
```zsh {iscopy=true}
git clone https://github.com/fumito100111/graph-neural-network.git
cd graph-neural-network
```
### 2. Create virtual environment for Python
```zsh {iscopy=true}
python3 -m venv .venv
source .venv/bin/activate
.venv/bin/python3 -m pip install --upgrade pip
.venv/bin/python3 -m pip install jupyter notebook
.venv/bin/python3 -m pip install torch
.venv/bin/python3 -m pip install numpy
.venv/bin/python3 -m pip install networkx
.venv/bin/python3 -m pip install matplotlib
```
