#!/bin/env python2.7
"""
Filters edges that are not in the list of nodes.

Author: Jason White

Usage: ./prune_edges mydataset.data < mydataset.graph | less
"""
from __future__ import print_function

from sys import stdin, stderr, stdout
import argparse

def read_data(f):
    data = set([])

    for line in f:
        values = line.strip().split(",", 1)
        data.add(values[0])

    return data

def main(args):
    stderr.write("Reading nodes...")
    stderr.flush()
    data = read_data(args.data)
    stderr.write(" Done.\n")

    filtered = 0

    for line in stdin:
        values = line.strip().split(",", 2)
        if values[0] in data and values[1] in data:
            stdout.write(line)
        else:
            filtered += 1

    print("Filtered %d edges." % filtered, file=stderr)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Filters edges that are not in the list of nodes."
        )
    parser.add_argument("data", type=argparse.FileType("r"),
        help="Data file.")

    args = parser.parse_args()

    try:
        main(args)
    except KeyboardInterrupt:
        pass
