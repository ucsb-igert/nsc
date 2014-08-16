#!/bin/env python2.7
"""
Compresses a network using the Spectral Graph Fourier method.

Author: Ali Hajimirza (ali@alihm.net)
"""
import fourier
import argparse
import sys
from os import path

sys.path.append(path.dirname(path.realpath(path.join(__file__, '../..'))))
import tools.graph_reader as graph_reader

parser = argparse.ArgumentParser(
    description="Compresses a network using the Spectral Graph Fourier method."
    )
parser.add_argument("data", type=argparse.FileType("rb"),
    help="Data input file.")
parser.add_argument("graph", type=argparse.FileType("rb"),
    help="Graph input file.")
parser.add_argument("signal", type=argparse.FileType("wb"),
    help="Signal output file.")
parser.add_argument("--budget", type=int, default=0,
    help="The number of eigenvectors to use for the decompression. This value should be between 1 and size of the nodes.")

if __name__ == '__main__':
    args = parser.parse_args()

    translation, data = graph_reader.read_nodes(args.data)
    graph = graph_reader.read_edges(args.graph, translation)

    if args.budget == 0:
        args.budget = len(data)/2

    fourier.compress(graph, data, args.budget, f=args.signal)

