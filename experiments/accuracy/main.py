#!/bin/env python2.7

import matplotlib.pyplot as plt
import numpy as np
import sys
import os

def read_ST_SSE(src):
    budget = []
    sse = []
    with open(src, 'rb') as error_file:
        for line in error_file:
            i, s = [float (a) for a in line.strip().split(',')]
            budget.append(i)
            sse.append(s)
    return np.array([budget,sse])

def scatter_plot(data_arrays, labels, title, save=False):
    plt.suptitle(title, fontsize=14)
    plots = []
    for data in data_arrays:
        plot, = plt.plot(data[0], data[1])
        plots.append(plot)
    plt.legend(plots, labels, loc=2)
    plt.xlabel('Bytes')
    plt.ylabel('SSE')

    if save:
        plt.savefig(os.path.join(_PLOT_DEFAULT_PATH, title + '.png'))
    else:
        plt.show()

    plt.clf()

def main():
    fourier_error = np.load('path/to/fourier/output.npy')[2]
    fourier_error = np.array([np.arange(len(fourier_error))*12, fourier_error])
    st_error = read_ST_SSE('path/to/ST/SLICE')

    scatter_plot([fourier_error, st_error], ['Fourier','ST'], 'Fourier_vs_ST_1000x5')


if __name__ == '__main__':
    main()
