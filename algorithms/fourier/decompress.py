#!/bin/env python2.7
"""
Decompresses a network using the Spectral Graph Fourier method.

Author: Ali Hajimirza (ali@alihm.net)
"""
import fourier
import argparse
import sys
from os import path
import numpy as np

sys.path.append(path.dirname(path.realpath(path.join(__file__, '../..'))))
import tools.graph_reader as graph_reader

parser = argparse.ArgumentParser(
    description="Decompresses a network using the Spectral Graph Fourier method."
    )
parser.add_argument("graph", type=argparse.FileType("rb"),
    help="Input graph file.")
parser.add_argument("signal", type=argparse.FileType("rb"),
    help="Input signal values.")

if __name__ == '__main__':
    args = parser.parse_args()
    sys.stderr.write('Loading the files...\n')
    data = np.load(args.signal)
    node_signal_value = data['signal']
    elements = data['position']
    graph = graph_reader.read_graph(args.graph, data['size'])
    sys.stderr.write('Signal and graph file loaded.\n')
    decompressed = fourier.decompress(graph, node_signal_value, elements)
    for i,v in enumerate(decompressed):
        sys.stdout.write('{},{}\n'.format(i,v))

