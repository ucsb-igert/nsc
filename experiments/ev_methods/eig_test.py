#!/bin/env python2.7
"""
Tests the accuracy of the fourier method by using different number of eigenvectors.

Author: Ali Hajimirza (ali@alihm.net)
"""
from os import path
import sys
sys.path.append(path.dirname(path.realpath(path.join(__file__, '../..'))))
import tools.graph_reader as graph_reader
import tools.plotter as plotter
import algorithms.fourier as fourier
import numpy as np
import argparse
import os

def SSE_compress_graph(adjacency_matrix, node_value, parallel=True):
    node_signal_values, eig_vecs = to_signal_domain(adjacency_matrix, node_value)
    size = len(node_value)
    sse = np.zeros((size, 3))
    p = 0
    for i in xrange(size):
        p1 = int((i * 100.0)/size)
        if p != p1:
            p = p1
            sys.stderr.write('\rReconstructing graph {}%'.format(p))
        sse[i][t] = SSE(node_value, uncompress_method(node_signal_values, eig_vecs, type=t+1, count=i+1))
    # Rearranging the values so each set of sse is in one array.
    sys.stderr.write('\rReconstruction complete.\n')
    return np.swapaxes(sse,0,1)

def uncompress_method(node_signal_values, eig_vecs, type=3 ,count=None):
    # Find the incidences of the highest f_signal and truncate the matrix
    elements = np.argsort(node_signal_values)
    if type == 1:
        if count:
            elements = elements[:count]
    elif type == 2:
        elements = elements[::-1]
        if count:
            elements = elements[:count]
    elif type == 3:
        if count:
            elements = np.append(elements[:count/2], elements[-count/2:])
    return to_graph_domain(node_signal_values[elements] ,eig_vecs[:,elements])

_TMP_PATH = 'tmp'
_RESULT_PATH = 'results'
parser = argparse.ArgumentParser(description='Test SSE.')
parser.add_argument('graph', type=argparse.FileType('rb'), help='.graph file that contains the links between the nodes.')
parser.add_argument('data', type=argparse.FileType('rb'), help='.graph file that contains the links between the nodes.')
parser.add_argument('title', default=None, help='.graph file that contains the links between the nodes.')

if __name__ == '__main__':
    if not os.path.exists(_TMP_PATH):
        os.makedirs(_TMP_PATH)
    if not os.path.exists(_RESULT_PATH):
            os.makedirs(_RESULT_PATH)

    if len(sys.argv) > 1:
        args = parser.parse_args()
        node_vals = graph_reader.read_node_values(data_file)
        adjacency_matrix = graph_reader.read_graph(graph_file, len(node_vals))
        sse_vals = fourier.SSE_compress_graph(adjacency_matrix, node_vals)
        np.save(os.path.join(_TMP_PATH, title +'_sse_vals.npy'), sse_vals)
        line_graph(sse_vals, ['Ascending', 'Descending', 'Max absolute'] , title=title)

    else:
        sys.stderr.write('No file specified.')

