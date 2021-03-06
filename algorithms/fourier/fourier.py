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
import math


_EXCHANGE_RATE = 12

def compress(csr_matrix, node_value, num_eig, f, compression_type=3):
    """
    Compress the node values of a compressed row matrix and saves it to the disk.

    Parameters
    ----------
    csr_matrix: scipy csr_matrix
        The adjacency matrix of the graph.

    node_value: numpy array
        Values of the nodes to be compressed.

    num_eig: int
        The number of eigenvectors to use for the decompression. This value should
        be between 1 and size of the nodes.

    f: file path
        File to save the compressed graph to.

    compression_type: int, optional
        compression_type = 1: uses the highest x number of signal values.
        compression_type = 2: uses the lowest x number of signal values.
        compression_type = 3: uses x number of the extrema (absolute value) signal values.

    dest: string, optional
        The path to save the graph.

    Returns
    -------
    None
        Saves file to the disk.

    """
    eig_vals, eig_vecs = laplacian_eigs(csr_matrix)
    node_signal_value = to_signal_domain(node_value, eig_vecs)
    elements = compress_method(node_signal_value, compression_type, num_eig)
    error = SSE(node_value, to_graph_domain(node_signal_value[elements], eig_vecs[:,elements]))
    stderr.write('Graph was compressed with a num_eig of {} and error of {}.\n'.format(num_eig, error))
    np.savez(f, signal=node_signal_value[elements], position=elements, size=np.array(len(node_value)))

def sse_compress_graph(csr_matrix, node_value, num_eig, compression_type=3):
    """
    Returns the error (SSE) of a compressed graph with a certain num_eig.

    Parameters
    ----------
    csr_matrix: scipy csr_matrix
        The adjacency matrix of the graph.

    node_value: numpy array
        Values of the nodes to be compressed.

    num_eig: int
        The number of eigenvectors to use for the decompression. This value should
        be between 1 and size of the nodes.

    compression_type: int, optional
        compression_type = 1: uses the highest x number of signal values.
        compression_type = 2: uses the lowest x number of signal values.
        compression_type = 2: uses x number of the extrema (absolute value) signal values.

    dest: string, optional
        The path to save the graph.

    Returns
    -------
    error: float
        The calculated SSE after compression.
    """

    eig_vals, eig_vecs = laplacian_eigs(csr_matrix)
    node_signal_value = to_signal_domain(node_value, eig_vecs)
    elements = compress_method(node_signal_value, compression_type, num_eig)
    error = SSE(node_value, to_graph_domain(node_signal_value[elements], eig_vecs[:,elements]))
    return error

def decompress(csr_matrix, node_signal_value, elements):
    """
    Reads and decompresses the values for a node.

    Parameters
    ----------
    csr_matrix: scipy csr_matrix
        The adjacency matrix of the graph.

    node_signal_values: numpy array
        Values of nodes in the signal domain.

    elements: numpy array
        The indices of the signal values and eigenvectors that are kept.

    Returns
    -------
    decompressed_vals: numpy array
        Returns the values reconstructed by the fourier algorithm
    """

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

def to_signal_domain(node_value, eig_vecs):
    """
    Transforms the node values from graph domain to signal domain.

    Parameters
    ----------
    node_value: numpy array
        Values of the nodes to be compressed.

    eig_vecs : (M, M) double or complex ndarray
        The normalized left eigenvector corresponding to the eigenvalue
        ``w[i]`` is the column v[:,i].

    Returns
    -------
    node_signal_value: numpy array
        Returns the equivalent signal values.
    """
    return np.dot(np.transpose(eig_vecs), node_value)

def budget_to_num_eigs(budget):
    """
    Converts budget (bytes) to the number of eigenvectors used to decompress the graph.

    Parameters
    ----------
    budget: int
        Number of bites after the compression.
    Returns
    -------
    num_eigs: int
        Returns number of eigenvectors used to decompress the graph.
    """
    return int(math.floor(budget/_EXCHANGE_RATE))

def num_eigs_to_budget(num_eigs):
    """
    Converts the number of eigenvectors used to decompress the graph to budget (bytes).

    Parameters
    ----------
    num_eigs: int
        Returns number of eigenvectors used to decompress the graph.
    Returns
    -------
    budget: int
        Number of bites after the compression.
    """
    return num_eigs*_EXCHANGE_RATE

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
    return np.dot(eig_vecs, node_signal_values)

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
        type = 3: uses x number of the extrema (absolute value) signal values.

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
    if type == 1:
        elements = np.argsort(node_signal_values)
        elements = elements[:count]
    elif type == 2:
        elements = np.argsort(node_signal_values)[::-1]
        elements = elements[:count]
    elif type == 3:
        elements = np.argsort(np.absolute(node_signal_values))[::-1]
        elements = elements[:count]
    return elements

