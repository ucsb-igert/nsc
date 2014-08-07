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

