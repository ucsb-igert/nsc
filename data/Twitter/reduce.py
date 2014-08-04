"""
Reduces the number of nodes in the Twitter dataset to several different sizes.
"""

import data.tools.reduce as reduce
import sys

# Generate graphs with these node counts.
reductions = [50, 100, 250, 500, 1000, 10000, 50000, 100000]

with open("twitter.data", "r") as fdata, \
        open("twitter.graph", "r") as fgraph:
    print("Reading data...", file=sys.stderr)
    data = reduce.read_data(fdata)

    print("Reading graph...", file=sys.stderr)
    graph = reduce.read_graph(fgraph)

    for r in reductions:
        with open("twitter_%d.data" % r, "w") as fdataout, \
                open("twitter_%d.graph" % r, "w") as fgraphout:
            print("Reducing to %d nodes..." % r, file=sys.stderr)
            reduce.reduce_graph(data, graph, r, fdataout, fgraphout)

