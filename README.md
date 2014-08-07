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

## Processing

Several datasets are used to benchmark these algorithms. See `data/README.md`
for more information about the datasets.

Two of the datasets are unprocessed. They can be processed with
```bash
$ ./processing/process_all
```

See `processing/README.md` for more details.

## Analysis
