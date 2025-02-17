from __future__ import annotations
from typing import Any
import torch
import torch.nn as nn
from torch.optim import Adam
from torch import Tensor
from src.data import Data
import networkx as nx

state_dim = 10

class Phi(nn.Module):
    def __init__(self, input_features: int, output_features: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_features = input_features
        self.output_features = output_features
        self.linear = nn.Linear(input_features, output_features)

    def forward(self, x):
        out = self.linear(x)
        return out


class Rho(nn.Module):
    def __init__(self, input_features: int, output_features: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_features = input_features
        self.output_features = output_features
        self.linear = nn.Linear(input_features, output_features)

    def forward(self, l_n):
        out = self.linear(l_n)
        return out


class H(nn.Module):
    def __init__(self, input_features: int, output_features: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_features = input_features
        self.output_features = output_features
        self.phi = Phi(input_features, output_features)
        self.rho = Rho(input_features, output_features)
        self.mu = 0.9

    def forward(self, l_n, x_u, l_u, u_degree):
        weight_vec = self.phi(torch.cat([l_n, l_u]))
        weight = weight_vec.reshape((self.output_features, self.output_features))
        weight = (self.mu / (self.output_features * u_degree)) * weight
        bias = self.rho(l_n)
        out = weight@x_u + bias
        return out


class F(nn.Module):
    def __init__(self, input_features: int, output_features: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_features = input_features
        self.output_features = output_features
        self.h_unit = H(input_features, output_features)

    def forward(self, l_n, list_x, list_l, list_degree):
        out = 0
        
        for i in range(len(list_x)):
            out += self.h_unit(l_n, list_x[i], list_l[i], list_degree[i])
        return out

"""
F_w(x,l,G)
x: states (state_dim*n_node)
l: labels (n_node*1)
G: graph
"""
class RNNF(nn.Module):
    def __init__(self, input_features: int, output_features: int, epsilon: float = 1.0e-5, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_features = input_features
        self.output_features = output_features
        self.f_unit = F(input_features, output_features)
        self.epsilon = epsilon

    def forward(self, x, l, G):
        x_tmp = x
        while True:
            x_next = torch.zeros((n_node, self.output_features))
            for i in range(n_node):
                x_next[i] += self.f_unit(l[i], list_x, list_l, list_degree)
            error = torch.abs(x_tmp - x_next)

            if error <= self.epsilon:
                break
            
            x_tmp = x_next
        
        return x_tmp


class G(nn.Module):
    def __init__(self, input_features: int, output_features: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_features = input_features
        self.output_features = output_features
        self.linear = nn.Linear(input_features, output_features)

    def forward(self, x, l_n):
        out = self.linear(torch.cat([x, l_n]))
        return out

"""
MAIN block in TABLE I
"""
class Main():
    def __init__(self):
        self.fw = RNNF()
        self.gw = G() # function G_w
        self.g = nx.karate_club_graph()
    
    def __call__(self, *args, **kwds):
        return self.fw.weight
    
    def learn(self, epochs, lamb =0.01):
        x = torch.rand((self.f.output_features, n_node))
        for epoch in range(epochs):
            x = self.fw()
            diff = grad()
            self.fw.weight = self.fw.weight - lamb * diff
            self.gw.weight = self.gw.weight - lamb * diff


    



def main():
    model = G()
    x = model()
    optim = Adam(model)
    # e_criterion = 
    # while 
    for _ in range(100):
        grad = model.backword()
        for parameter in model.parameters():
            parameter.





if __name__ == '__main__':
    pass