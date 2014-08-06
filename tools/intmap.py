#!/bin/env python3.4
"""
Maps string node identifiers to integers.

Author: Jason White
"""
from sys import stderr
import argparse
import random

def main(args):
    datamap = {}

    # Map strings to integers
    i = 0
    for line in args.datain:
        values = line.strip().split(",", 1)
        k, v = values[0], values[1]
        datamap[k] = i
        args.dataout.write("%d,%s\n" % (i, v))
        i += 1

    for line in args.graphin:
        values = line.strip().split(",", 2)
        a, b = values[0], values[1]
        args.graphout.write("%d,%d\n" % (datamap[a], datamap[b]))

    # Write out the map to a file.
    for k,v in datamap.items():
        args.mapout.write("%s,%d\n" % (k, v))


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Maps string node identifiers to integers."
        )
    parser.add_argument("datain", type=argparse.FileType("r"),
        help="Data input file.")
    parser.add_argument("graphin", type=argparse.FileType("r"),
        help="Graph input file.")
    parser.add_argument("dataout", type=argparse.FileType("w"),
        help="Data output file.")
    parser.add_argument("graphout", type=argparse.FileType("w"),
        help="Graph output file.")
    parser.add_argument("mapout", type=argparse.FileType("w"),
        help="Map output file.")

    args = parser.parse_args()

    try:
        main(args)
    except KeyboardInterrupt:
        print("Processing aborted.", file=stderr)
        pass
