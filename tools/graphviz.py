#!/bin/env python2.7
"""
Generates a GraphViz file from *.graph and *.data files.

Author: Jason White
"""
import sys
import argparse

parser = argparse.ArgumentParser(
    description="Generates a GraphViz file from *.graph and *.data files."
    )
parser.add_argument("data", type=argparse.FileType("r"),
    help="Data input file.")
parser.add_argument("graph", type=argparse.FileType("r"),
    help="Graph input file.")

gv_header = """digraph {
    node [fillcolor=lightskyblue2 label="" shape=circle style=filled]
"""

gv_footer = "}"

if __name__ == "__main__":
    args = parser.parse_args()

    f = sys.stdout

    try:
        f.write(gv_header)

        for line in args.data:
            node, value = line.strip().split(",", 1)
            f.write('    "%s" [label="%s"]\n' % (node, value))

        for line in args.graph:
            a, b = line.strip().split(",", 1)
            f.write("    " + a + " -> " + b + "\n")

        f.write(gv_footer)
    except OSError:
        pass
