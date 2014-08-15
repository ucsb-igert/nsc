# Network State Compression

A comparison of three different algorithms for compressing/summarizing a
network. These algorithms include:

 * **Slice Tree**: A technique based on the decomposition of the network into
   smooth regions using slices.

 * **Spectral Graph Fourier**: Extends the notion of the Fourier transform to
   graphs.

 * **Spectral Graph Wavelets**: Extends the notion of wavelets to graphs using
   [spectral graph theory][sgt].

[sgt]: http://en.wikipedia.org/wiki/Spectral_graph_theory

## Dependencies

 * Python 2.7
 * [matplotlib](http://matplotlib.org/)
 * [numpy](http://matplotlib.org/)
 * [scipy](http://www.scipy.org/)
 * [networkx](https://networkx.github.io/)
 * [Graphviz](http://www.graphviz.org/)

## Processing

Several datasets are used to benchmark these algorithms. See `data/README.md`
for more information about the datasets.

Two of the datasets are unprocessed. They can be processed with
```bash
$ ./processing/process_all
```

See `processing/README.md` for more details.

## Experiments

After processing the datasets, experiments can be run on them. To run them all,
do
```bash
$ ./experiments/run_all
```

See `experiments/README.md` for more details.
