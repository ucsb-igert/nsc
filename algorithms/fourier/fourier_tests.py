#!/bin/env python2.7
import fourier
import argparse
import os
import matplotlib.pyplot as plt
import numpy as np
import sys

_BINARY_DEFAULT_PATH = 'sse'
_PLOT_DEFAULT_PATH = 'plots'

def read_graph(f, size, weighted=False, weight=1, undirected=True):
    """
    Reads a graph from a graph file.

    Parameters
    ----------
    f: file
        Graph file. The file format should be in from_node_id,to_node_id,wight(optional)
        The wight parameter can be safely ignored in unweighted graphs.

    size: int
        The size of the graph (number of nodes).

    weighted: bool, optional
        To read a weighted graph. The file should include a third column.

    weight: bool, optional
        The weight for the connections.

    undirected: bool, optional
        To read a undirected graph.

    Returns
    -------
    graph: 2d numpy array.
        This is adjacency matrix representing the unweighted graph with value of 1.
    """
    sys.stderr.write('Reading graph file "{}"...\n'.format(f.name))
    graph = np.zeros((size,size))
    with f as graph_file:
        for line in f:
            args = line.strip().split(',')
            i, j = [int(i) for i in args[:2]]
            if weighted:
                weight = float(args[2])
            graph[i,j] = weight
            if undirected:
                graph[j,i] = weight
    return graph

def read_node_values(f):
    """
    Reads the values for nodes in a graph from a file.

    Parameters
    ----------
    f: file
        Node value file. The file format should be in node_id,value.
        The node_if will be ignored and the values are added in order from 0 to n

    Returns
    -------
    node_vals: 1d numpy array.
        This array contains the value for each node.
    """
    sys.stderr.write('Reading node values from file "{}"...\n'.format(f.name))
    node_vals = []
    with f as data_file:
        for line in data_file:
            node_vals.append(float(line.strip().split(',')[1]))
    return np.array(node_vals)


def main(graph_file, data_file, title, save=True):
    node_vals = read_node_values(data_file)
    adjacency_matrix = read_graph(graph_file, len(node_vals))
    sse_vals = fourier.SSE_compress_graph(adjacency_matrix, node_vals, parallel=False)
    if save:
        if not os.path.exists(_BINARY_DEFAULT_PATH):
            os.makedirs(_BINARY_DEFAULT_PATH)
        np.save(os.path.join(_BINARY_DEFAULT_PATH, title +'_sse_vals.npy'), sse_vals)
    plot_graph(sse_vals, ['Ascending', 'Descending', 'Max absolute'] , title=title)


def plot_graph(data_arrays, labels, title):
    plt.suptitle(title, fontsize=14)
    plots = []
    for data in data_arrays:
        plot, = plt.plot(data)
        plots.append(plot)
    plt.legend(plots, labels, loc=2)
    plt.xlabel('Number of used eigenvectors')
    plt.ylabel('SSE')
    plt.savefig(os.path.join(_PLOT_DEFAULT_PATH, title + '.png'))
    plt.clf()

parser = argparse.ArgumentParser(description='Test SSE.')
parser.add_argument('graph', type=argparse.FileType('rb'), help='.graph file that contains the links between the nodes.')
parser.add_argument('data', type=argparse.FileType('rb'), help='.graph file that contains the links between the nodes.')
parser.add_argument('title', default=None, help='.graph file that contains the links between the nodes.')

if __name__ == '__main__':
    if not os.path.exists(_PLOT_DEFAULT_PATH):
        os.makedirs(_PLOT_DEFAULT_PATH)
    if len(sys.argv) > 1:
        args = parser.parse_args()
        main(args.graph, args.data, args.title, save=True)
    else:
        print "No args"

