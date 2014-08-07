#!/bin/env python2.7
"""
Reduces a graph to the number of specified nodes.

Author: Jason White
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import division

from sys import stderr
import argparse
import random

def read_data(f):
    data = {}

    for line in f:
        values = line.strip().split(",", 1)
        data[int(values[0])] = float(values[1])

    return data

def read_graph(f):
    graph = {}

    for line in f:
        values = line.strip().split(",", 2)
        a, b = int(values[0]), int(values[1])

        try:
            graph[a].append(b)
        except KeyError:
            graph[a] = [b]

    return graph

def bfs(center, graph, visited):
    """Iterates over nodes starting at the specified center node in a
    breadth-first search."""

    queue = [center]
    visited.add(center)

    while queue:
        node = queue.pop()
        yield node

        # Queue all outgoing nodes
        try:
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)
        except KeyError:
            pass

def reduce_graph(data, graph, count, fdataout, fgraphout):
    nodes = set(data.keys())

    # Nodes visited.
    visited_nodes = set([])

    # Nodes taken from the graph
    taken = set([])

    # Take nodes from the larger graph and build the smaller graph with those
    # nodes. We do a breadth-first search from a randomly chosen center until it
    # is exhausted and then choose a new random center to search from.
    while len(taken) < count:
        # Pool of nodes to choose a center from
        pool = nodes - visited_nodes
        if not pool:
            break;

        # Choose a random center to start from
        center = random.choice(list(pool))

        for node in bfs(center, graph, visited_nodes):
            if node not in nodes:
                continue

            taken.add(node)

            if len(taken) >= count:
                break

    # Write out the chosen nodes and the links between them.
    for node in taken:
        fdataout.write("%d,%f\n" % (node, data[node]))

        try:
            for child in graph[node]:
                if child in taken:
                    fgraphout.write("%d,%d\n" % (node, child))
        except KeyError:
            pass

def reduce_graphs(fdata, fgraph, datafmt, graphfmt, counts):
    print("Reading data...", file=stderr)
    data = read_data(fdata)

    print("Reading graph...", file=stderr)
    graph = read_graph(fgraph)

    for r in counts:
        with open(datafmt % r, "w") as fdataout, \
                open(graphfmt % r, "w") as fgraphout:
            print("Reducing to %d nodes..." % r, file=stderr)
            reduce_graph(data, graph, r, fdataout, fgraphout)


def main(args):
    stderr.write("Reading nodes...")
    stderr.flush()
    data = read_data(args.datain)
    stderr.write(" Done.\n")

    stderr.write("Reading graph...")
    stderr.flush()
    graph = read_graph(args.graphin)
    stderr.write(" Done.\n")

    stderr.write("Reducing to %d nodes..." % args.count)
    stderr.flush()
    reduce_graph(data, graph, args.count, args.dataout, args.graphout)
    stderr.write(" Done.\n")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Reduces a graph using a breadth-first search starting at the specified node."
        )
    parser.add_argument("datain", type=argparse.FileType("r"),
        help="Data input file.")
    parser.add_argument("graphin", type=argparse.FileType("r"),
        help="Graph input file.")
    parser.add_argument("dataout", type=argparse.FileType("w"),
        help="Data output file.")
    parser.add_argument("graphout", type=argparse.FileType("w"),
        help="Graph output file.")
    parser.add_argument("--count", type=int, default=100, help="Number of nodes to take.")

    args = parser.parse_args()

    try:
        main(args)
    except KeyboardInterrupt:
        print("Processing aborted.", file=stderr)
        pass
