#!/bin/env python2.7

import subprocess
from os import path

# Find the slice tree executable.
slice_tree = path.relpath(path.join(path.dirname(__file__), "../algorithms/slice-tree/graph_compression"))

def precompute(data, graph, partsizes, numthreads=8, **kwargs):
    subprocess.check_call([slice_tree,
        "--values"    , data           ,
        "--graph"     , graph          ,
        "--partsizes" , partsizes      ,
        "--numthreads", str(numthreads)
        ], **kwargs)

def greedy(data, graph, partsizes, budget, radius=2, numthreads=8, **kwargs):
    subprocess.check_call([slice_tree,
        "--compression", "ST"           ,
        "--values"     , data           ,
        "--graph"      , graph          ,
        "--partsizes"  , partsizes      ,
        "--numthreads" , str(numthreads),
        "--budget"     , str(budget)    ,
        "--maxradius"  , str(radius)    ,
        ], **kwargs)

def sampling(data, graph, partsizes, budget, radius=2, numthreads=8,
        delta=0.1, rho=0.6, sampling_rate=0.1, **kwargs):
    subprocess.check_call([slice_tree,
        "--compression"  , "STBS"            ,
        "--values"       , data              ,
        "--graph"        , graph             ,
        "--partsizes"    , partsizes         ,
        "--numthreads"   , str(numthreads)   ,
        "--budget"       , str(budget)       ,
        "--maxradius"    , str(radius)       ,
        "--delta"        , str(delta)        ,
        "--rho"          , str(rho)          ,
        "--sampling-rate", str(sampling_rate),
        ], **kwargs)
