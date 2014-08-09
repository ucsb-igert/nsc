#!/bin/env python2.7
import os
import matplotlib.pyplot as plt
import numpy as np
import sys


def bar_chart(data_arrays, xlabel, ylabel, legend, title, f, width=0.25, color=['r', 'g', 'b', 'c', 'k', 'y', 'm']):
    """
    Plots a bar chart.

    Parameters
    ----------
    data_arrays: 2d numpy array
        Data to be plotted. This array consists of arrays of real values to be plotted.
        Each row of this matrix will be plotted as a bar on the graph.

    xlabel: list of string
        The list of categories on for the x axis labels. The length of this list should be equal to the
        columns of the data_arrays.

    ylabel: string
        The label on the y axis.

    legend: list of string
        The labels for each category .

    title: string
        The title of the graph. Will be used as the name of the graph file.

    f: string or file-like object
        Path to the directory to save the image.

    width: float, optional
        Width of each column.

    color: list, optional
        List of colors to be used for different labels.

    Returns
    -------
    None:
        Saves the plot to the disk.
    """
    ind = np.arange(len(data_arrays[0]))
    fig, ax = plt.subplots()
    plots = []
    for i, data in enumerate(data_arrays):
        plots.append(ax.bar(ind+(i*width), data, width, color=color[i]))

    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(ind + width)
    ax.set_xticklabels(xlabel)
    ax.legend([plot[0] for plot in plots], legend)
    plt.savefig(f, format="png")
    plt.clf()

def scatter_plot(data_arrays, xlabel, ylabel, labels, title, dest=''):
    """
    Plots a scatter chart.

    Parameters
    ----------
    data_arrays: 3d numpy array
        Data to be plotted. This array consists of matrices of real values to be plotted.
        Each row of this matrix will be plotted as a line on the graph.

    xlabel: list of string
        The list of categories on for the x axis labels. The length of this list should be equal to the
        columns of the data_arrays.

    ylabel: string
        The label on the y axis.

    labels: list of string
        The labels for each category.

    title: string
        The title of the graph. Will be used as the name of the graph file.

    dest: string, optional
        Path to the directory to save the image

    Returns
    -------
    None:
        Saves the plot to the disk.
    """
    plt.suptitle(title, fontsize=14)
    plots = []
    for data in data_arrays:
        plot, = plt.plot(data[0], data[1])
        plots.append(plot)
    plt.legend(plots, labels, loc=2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(os.path.join(dest, title + '.png'))
    plt.clf()

def line_plot(data_arrays, xlabel, ylabel, labels, title, dest=''):
    """
    Plots a scatter chart.

    Parameters
    ----------
    data_arrays: 2d numpy array
        Data to be plotted. This array consists of matrices of real values to be plotted.
        Each row of this matrix will be plotted as a line on the graph.

    xlabel: list of string
        The list of categories on for the x axis labels. The length of this list should be equal to the
        columns of the data_arrays.

    ylabel: string
        The label on the y axis.

    labels: list of string
        The labels for each category.

    title: string
        The title of the graph. Will be used as the name of the graph file.

    dest: string, optional
        Path to the directory to save the image

    Returns
    -------
    None:
        Saves the plot to the disk.
    """
    plt.suptitle(title, fontsize=14)
    plots = []
    for data in data_arrays:
        plot, = plt.plot(data)
        plots.append(plot)
    plt.legend(plots, labels, loc=2)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(os.path.join(dest, title + '.png'))
    plt.clf()

def Test ():
    bar_chart([np.random.randint(100,size=5), np.random.randint(100,size=5)], ['G1', 'G2', 'G3', 'G4', 'G5'], 'ylabel', ['m','w'], 'title', dest='', width=0.25, color=['r','g', 'b', 'c', 'k', 'y','m'])
    scatter_plot([[np.random.randint(9,size=10), np.random.randint(9,size=10)], [np.random.randint(9,size=10), np.random.randint(9,size=10)]], 'xlabel', 'ylabel', ['1','2'], 'title1', dest='')
    line_plot([np.random.randint(100,size=100), np.random.randint(100,size=100), np.random.randint(100,size=100), np.random.randint(100,size=100)], 'xlabel', 'ylabel', ['1','2','3','4'], 'title2', dest='')

if __name__ == '__main__':
    Test()
