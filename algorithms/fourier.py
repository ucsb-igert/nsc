#!/bin/env python2.7
from scipy.sparse import csgraph
import multiprocessing
from multiprocessing import Pool
import matplotlib.pyplot as plt
from scipy import linalg
import numpy as np
import sys

def compress_graph(adjacency_matrix, node_value):
    node_signal_value = to_signal_domain(adjacency_matrix, node_signal_value)
    # write to a file(decide on number of signals to save)

def reconsruct_graph(adjacency_matrix, signal_file):
    pass

def to_signal_domain(adjacency_matrix, node_value):
    sys.stderr.write('Computing Eigenvectors...\n')
    lap = csgraph.laplacian(adjacency_matrix, normed=False)
    del adjacency_matrix
    eig_vals, eig_vecs = linalg.eigh(lap, type=3)
    sys.stderr.write('Eigenvector decomposition complete.\n')
    node_signal_value = np.zeros(len(node_value))
    for i, eig_val in enumerate(eig_vals):
        node_signal_value[i] = np.dot(node_value, eig_vecs[:,i])
    return node_signal_value, eig_vecs

def to_graph_domain(node_signal_values, eig_vecs):
    original_value = np.zeros(len(eig_vecs))
    for i, eig_vec in enumerate(eig_vecs):
        original_value[i] = np.dot(node_signal_values, eig_vec)
    return original_value

def SSE_compress_graph(adjacency_matrix, node_value, parallel=True):
    node_signal_values, eig_vecs = to_signal_domain(adjacency_matrix, node_value)
    del adjacency_matrix
    size = len(node_value)
    sse = np.zeros((size, 3))
    if parallel:
        pass
        # p = Pool(multiprocessing.cpu_count())
        # for i in xrange(size):
        #   res = p.apply(parallel_SSE_helper, args = (node_value,node_signal_values, eig_vecs, i))
        #   sse[i] = res
        # p.close()
        # p.join()
    else:
        p = 0
        for i in xrange(size):
            p1 = int((i * 100.0)/size)
            if p != p1:
                p = p1
                sys.stderr.write('\rReconstructing graph {}%'.format(p))
            res = parallel_SSE_helper(node_value, node_signal_values, eig_vecs, i)
            sse[i] = res
    # Rearranging the values so each set of sse is in one array.
    sys.stderr.write('\rReconstruction complete.\n')
    return np.swapaxes(sse,0,1)

def parallel_SSE_helper(node_value, node_signal_values, eig_vecs, i):
    res = np.zeros(3)
    for t in xrange(3):
        res[t] = SSE(node_value, uncompress_method(node_signal_values, eig_vecs, type=t+1, count=i+1))
    return res

def uncompress_method(node_signal_values, eig_vecs, type=3 ,count=None):
    # Find the incidences of the highest f_signal and truncate the matrix
    elements = np.argsort(node_signal_values)
    if type == 1:
        if count:
            elements = elements[:count]
    elif type == 2:
        elements = elements[::-1]
        if count:
            elements = elements[:count]
    elif type == 3:
        if count:
            elements = np.append(elements[:count/2], elements[-count/2:])
    return to_graph_domain(node_signal_values[elements] ,eig_vecs[:,elements])

def SSE(original, perturbed):
    return np.sum(np.square(np.subtract(original, perturbed)))


if __name__ == '__main__':
    np.set_printoptions(suppress=True)
"""
    G = np.array([
        [0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 0, 1, 0]
        ])
    f_i = np.array([1,5,7, 4, 3])

    print SSE_compress_graph(G, f_i, parallel=False)
"""
"""
sparse
    from scipy.sparse import *
    import scipy
    import scipy.sparse.linalg as LA
    row = np.array([0,0,1,1,1,2,2,2,3,3,3,4])
    col = np.array([1,2,0,2,3,0,1,3,1,2,4,3])
    data = np.ones(12)
    G = scipy.sparse.csr_matrix( (data,(row,col)), shape=(5,5) )

    lap = csgraph.laplacian(G, normed=False)



    eig_val, eig_vecs = LA.eigs(lap, k=3)
    print eig_val
    print eig_vecs
"""

