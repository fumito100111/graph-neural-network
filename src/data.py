from __future__ import annotations
from typing import Any
import numpy as np
from numpy import ndarray
import torch
from torch import Tensor
import networkx as nx

# class Graph(object):
#     def __init__(self, index: int, node_labels: ndarray, edges: ndarray):
#         index: int
#         self.node_labels = node_labels
#         self.edges = edges

class Data(object):
    def __init__(self, title: str, dataset_dir: str) -> None:
        self.edges = np.loadtxt(f'{dataset_dir}/{title}.edges', delimiter=',')
        self.graph_idx = np.loadtxt(f'{dataset_dir}/{title}.graph_idx')
        self.graph_labels = np.loadtxt(f'{dataset_dir}/{title}.graph_labels')
        self.node_attrs = np.loadtxt(f'{dataset_dir}/{title}.node_attrs')
        self.node_labels = np.loadtxt(f'{dataset_dir}/{title}.node_labels', delimiter=',')
    
    def create_graphs(self):
        index = np.unique(self.graph_idx)
        # print(index)
        graphs = []
        node_ids = np.arange(1, self.node_attrs.shape[0]+1)

        for idx in index[:10]:

            sub = self.graph_idx == idx
            current_nodes = node_ids[sub]
            edges = []
            for edge in self.edges:
                if edge[0] in current_nodes and edge[1] in current_nodes:
                    edges.append(edge)
            # edges = self.edges[self.edges[0] in current_nodes and self.edges[1] in current_nodes]
            # graph_labels = self.graph_labels[sub]
            node_attrs = self.node_attrs[sub]
            node_labels = self.node_labels[sub]
            nodes = [(current_nodes[i], node_attrs[i]) for i in range(0, len(current_nodes))]

            G = nx.Graph()
            G.add_nodes_from(nodes)
            G.add_edges_from(edges)
            graphs.append(G)
        self.graphs = graphs
        print(len(self.graphs))



#     def connected_edges(self) -> ndarray:




if __name__ == '__main__':
   data = Data('proteins', './dataset/proteins')
   data.create_graphs()        