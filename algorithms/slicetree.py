#!/bin/env python2.7

from os import path
import subprocess

# Find the slice tree executable.
slice_tree = path.relpath(path.join(path.dirname(__file__), "../algorithms/slice-tree/graph_compression"))

def precompute(data, graph, partsizes, numthreads=8):
    return [slice_tree,
        "--values"    , data           ,
        "--graph"     , graph          ,
        "--partsizes" , partsizes      ,
        "--numthreads", str(numthreads)
        ]

def greedy(data, graph, partsizes, numpart, radius=2, numthreads=8):
    return [slice_tree,
        "--compression", "ST"           ,
        "--values"     , data           ,
        "--graph"      , graph          ,
        "--partsizes"  , partsizes      ,
        "--numthreads" , str(numthreads),
        "--numpart"    , str(numpart)   ,
        "--maxradius"  , str(radius)    ,
        ]

def sampling(data, graph, partsizes, numpart, radius=2, numthreads=8,
        delta=0.1, rho=0.6, sampling_rate=0.1):
    return [slice_tree,
        "--compression"  , "STBS"            ,
        "--values"       , data              ,
        "--graph"        , graph             ,
        "--partsizes"    , partsizes         ,
        "--numthreads"   , str(numthreads)   ,
        "--numpart"      , str(numpart)      ,
        "--maxradius"    , str(radius)       ,
        "--delta"        , str(delta)        ,
        "--rho"          , str(rho)          ,
        "--sampling-rate", str(sampling_rate),
        ]

def run_precompute(data, graph, partsizes, numthreads=8, **kwargs):
    return subprocess.check_call(greedy(
        data, graph, partsizes, numthreads
        ), **kwargs)

def run_greedy(data, graph, partsizes, numpart, radius=2, numthreads=8, **kwargs):
    return subprocess.check_call(greedy(
        data, graph, partsizes, numpart, radius, numthreads
        ), **kwargs)

def run_sampling(data, graph, partsizes, numpart, radius=2, numthreads=8,
        delta=0.1, rho=0.6, sampling_rate=0.1, **kwargs):
    return subprocess.check_call(greedy(
        data, graph, partsizes, numpart, radius, numthreads, delta, rho,
        sampling_rate
        ), **kwargs)

# Example of output:
# budget = 547
# sse = 107058
# sse_reduction = 95444.7
# compression_rate = 146.252
# compression_time = 40.2648
# pruned_slices = 0
def parse_output(output):
    parsed = {}
    for line in output.splitlines():
        k, v = line.split(" = ")
        if k == "budget" or k == "pruned_slices":
            parsed[k] = int(v)
        else:
            parsed[k] = float(v)
    return parsed
