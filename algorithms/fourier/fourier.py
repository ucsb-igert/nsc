"""
Fourier transform on graphs.

This module provides methods to compress a graph using the fourier transform method.

Author: Ali Hajimirza (ali@alihm.net)
"""
from os import path
from sys import stderr
from scipy.sparse import csgraph
from scipy import linalg
import numpy as np

def compress(csr_matrix, node_value, budget, f, compression_type=3):
    """
    Compress the node values of a compressed row matrix and saves it to the disk.

    Parameters
    ----------
    csr_matrix: scipy csr_matrix
        The adjacency matrix of the graph.

    node_value: numpy array
        Values of the nodes to be compressed.

    budget: int
        The number of eigenvectors to use for the decompression. This value should
        be between 1 and size of the nodes.

    f: file path
        File to save the compressed graph to.

    compression_type: int, optional
        compression_type = 1: uses the highest x number of signal values.
        compression_type = 2: uses the lowest x number of signal values.
        compression_type = 2: uses x number of the extrema (absolute value) signal values.

    dest: string, optional
        The path to save the graph.

    Returns
    -------
    None
        Saves file to the disk.

    """
    eig_vals, eig_vecs = laplacian_eigs(csr_matrix)
    node_signal_value = to_signal_domain(node_value, eig_vals, eig_vecs)
    elements = compress_method(node_signal_value, compression_type, budget)
    error = SSE(node_value, to_graph_domain(node_signal_value[elements], eig_vecs[:,elements]))
    stderr.write('Graph was compressed with a budget of {} and error of {}.\n'.format(budget, error))
    np.savez(f, signal=node_signal_value[elements], position=elements)

def decompress(csr_matrix, f):
    """
    Reads and decompresses the values for a node.

    Parameters
    ----------
    csr_matrix: scipy csr_matrix
        The adjacency matrix of the graph.

    f: file path or handle
        Compressed graph file. (.npz)

    Returns
    -------
    decompressed_vals: numpy array
        Returns the values reconstructed by the fourier algorithm
    """
    stderr.write('Loading the file...\n')
    data = np.load(f)
    node_signal_value = data['signal']
    elements = data['position']
    stderr.write('Signal file loaded.\n')
    eig_vals, eig_vecs = laplacian_eigs(csr_matrix)
    decompressed_vals = to_graph_domain(node_signal_value, eig_vecs[:,elements])
    return decompressed_vals

def laplacian_eigs(csr_matrix):
    """
    Computes the eigenvalues and eigenvectors of the laplacian matrix.

    Parameters
    ----------
    csr_matrix: scipy csr_matrix
        The adjacency matrix of the graph.

    Returns
    -------
    eig_vals : (M,) double or complex ndarray
        The eigenvalues, each repeated according to its multiplicity.
    eig_vecs : (M, M) double or complex ndarray
        The normalized left eigenvector corresponding to the eigenvalue
        ``w[i]`` is the column v[:,i].
    """
    stderr.write('Computing Eigenvectors...')
    lap = csgraph.laplacian(csr_matrix, normed=False)
    eig_vals, eig_vecs = linalg.eigh(lap.todense(), type=3)
    stderr.write('\rEigenvector decomposition complete.\n')
    return eig_vals, eig_vecs

def to_signal_domain(node_value, eig_vals, eig_vecs):
    """
    Transforms the node values from graph domain to signal domain.

    Parameters
    ----------
    node_value: numpy array
        Values of the nodes to be compressed.

    eig_vals : (M,) double or complex ndarray
        The eigenvalues, each repeated according to its multiplicity.

    eig_vecs : (M, M) double or complex ndarray
        The normalized left eigenvector corresponding to the eigenvalue
        ``w[i]`` is the column v[:,i].

    Returns
    -------
    node_signal_value: numpy array
        Returns the equivalent signal values.
    """
    node_signal_value = np.zeros(len(node_value))
    for i, eig_val in enumerate(eig_vals):
        node_signal_value[i] = np.dot(node_value, eig_vecs[:,i])
    return node_signal_value

def to_graph_domain(node_signal_values, eig_vecs):
    """
    Transforms the node values from graph domain to signal domain.

    Parameters
    ----------
    node_signal_values: numpy array
        Values of nodes in the signal domain.

    eig_vecs : (M, M) double or complex ndarray
        The normalized left eigenvector corresponding to the signal values.

    Returns
    -------
    node_signal_value: numpy array
        Returns the equivalent signal values.
    """
    original_value = np.zeros(len(eig_vecs))
    for i, eig_vec in enumerate(eig_vecs):
        original_value[i] = np.dot(node_signal_values, eig_vec)
    return original_value

def SSE(original, compressed):
    """
    Computes the Residual sum of squares for the compressed values.

    Parameters
    ----------
    original: numpy array
        Values of nodes before compression.

    original: numpy array
        Values of nodes after compression.

    Returns
    -------
    sse: int
        Compression error.
    """
    return np.sum(np.square(np.subtract(original, compressed)))

def compress_method(node_signal_values, type, count):
    """
    Chooses the signal values to be saved based on their value.

    Parameters
    ----------
    node_signal_values: numpy array
        Values of nodes in the signal domain.

    type: int, optional
        type = 1: uses the highest x number of signal values.
        type = 2: uses the lowest x number of signal values.
        type = 2: uses x number of the extrema (absolute value) signal values.

    Returns
    -------
    elements: numpy array
        The indices of the signal values and eigenvectors to be kept.

    Raises
    -------
    Exception:
        If the value of the count is not between 1 to size of the node_signal_values.
    """
    if count > len(node_signal_values) or count < 1:
        raise Exception('{} is not a valid count.'.format(count))
    elements = np.argsort(node_signal_values)
    if type == 1:
        elements = elements[:count]
    elif type == 2:
        elements = elements[::-1]
        elements = elements[:count]
    elif type == 3:
        elements = np.append(elements[:count/2], elements[-count/2:])
    return elements
