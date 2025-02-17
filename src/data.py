from __future__ import annotations
from typing import Any
import numpy as np
from numpy import ndarray
import torch
from torch import Tensor
import networkx as nx
import matplotlib.pyplot as plt


class Data(object):
    def __init__(self, title: str, dataset_dir: str) -> None:
        self.edges = np.loadtxt(f'{dataset_dir}/{title}.edges', delimiter=',')
        self.graph_idx = np.loadtxt(f'{dataset_dir}/{title}.graph_idx')
        self.graph_labels = np.loadtxt(f'{dataset_dir}/{title}.graph_labels')
        self.node_attrs = np.loadtxt(f'{dataset_dir}/{title}.node_attrs')
        self.node_labels = np.loadtxt(f'{dataset_dir}/{title}.node_labels', delimiter=',')
    
    def create_graphs(self):
        index = np.unique(self.graph_idx)
        graphs = []
        node_ids = np.arange(1, self.node_attrs.shape[0]+1)

        for idx in index[:1]:
            sub = self.graph_idx == idx
            current_nodes = node_ids[sub]

            G = nx.Graph()
            node_attrs = self.node_attrs[sub]
            node_labels = self.node_labels[sub]
            for i in range(0, len(current_nodes)):
                G.add_node(int(current_nodes[i]), label=node_attrs[i])

            for edge in self.edges:
                if edge[0] in current_nodes and edge[1] in current_nodes:
                    G.add_edge(int(edge[0]), int(edge[1]))
            
            graphs.append(G)
        self.graphs = graphs

      

if __name__ == '__main__':
    data = Data('proteins', './dataset/proteins')
    data.create_graphs()
    graphs = data.graphs

    nx.draw_networkx(graphs[0])
    plt.show()

