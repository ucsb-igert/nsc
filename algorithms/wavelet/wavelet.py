
from os import path
import sys
sys.path.append(path.dirname(path.realpath(path.join(__file__, '../..'))))
from tools import graph_reader
from algorithms.fourier import fourier
import numpy as np

def to_wavelet_domain(node_signal_values, eig_vals, eig_vecs, func, t):
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
    node_wavelet_value = np.zeros(len(node_signal_values))
    for i, eig_vec in enumerate(eig_vecs):
        node_wavelet_value[i] = func(t * eig_vals[i]) * np.dot(node_signal_values, eig_vec)
    return node_wavelet_value

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

def ricker(points, a):

    A = 2 / (np.sqrt(3 * a) * (np.pi**0.25))
    wsq = a**2
    vec = np.arange(0, points) - (points - 1.0) / 2
    xsq = vec**2
    mod = (1 - xsq / wsq)
    gauss = np.exp(-xsq / (2 * wsq))
    total = A * mod * gauss
    return total

def main():
    import scipy.signal
    vals = np.array([1,2,7,4,5,6])
    graph = graph_reader.read_graph(open('test.graph','rb'), 6)
    g = graph.todense()

    for i in xrange(6):
        for j in xrange(6):
            print g[i,j],
        print 
    eig_vals, eig_vecs = fourier.laplacian_eigs(graph)
    signal = fourier.to_signal_domain(vals, eig_vecs)
    print signal

    # Scipy
    wavelet = scipy.signal.ricker
    widths = np.arange(1, 11)
    cwtmatr = scipy.signal.cwt(signal, wavelet, [5])[0]
    print cwtmatr


   
    my_wave = to_wavelet_domain(signal, eig_vals,eig_vecs, f, 5)
    print my_wave

def f(x):
    x1 = 1
    x2 = 2
    a = 2
    b = 2
    if x < x1:
        return (x1*(x**a))
    elif x > x2:
        return (x2**b)*(x**(-b))
    else:
        return (-5 + (11*x) - (6*(x**2)) + (x**3))


if __name__ == '__main__':
    main()