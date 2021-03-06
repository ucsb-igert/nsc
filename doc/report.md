# Introduction

The purpose of this project is to compare competing approaches for network state
compression. The networks we are interested in have nodes with associated values
or *states*. Network state compression refers to the translation of these
states to a more compact form. For the compression methods we investigated, all
are lossy. Thus, we are mainly concerned about the accuracy and scalability of
the compression algorithms.

# Relevant Work

There are four papers relevant to this project:

 * Arlei Silva, Petko Bogdanov, Ambuj K. Singh. "Network State Summarization via
   In-Graph Compression". Under review, 2014.

    This paper introduces a new network state compression algorithm called Slice
    Tree. Details of this algorithm will be discussed in the next section.

 * David Shuman, et al. "[The Emerging Field of Signal Processing on Graphs:
   Extending high-dimensional data analysis to networks and other irregular
   domains.][signals]" Signal Processing Magazine, 2013.

    This paper introduces the concept of transforming network state into the
    signal domain.

 * Zachi Karni, and Craig Gotsman. "[Spectral Compression of Mesh
   Geometry.][spectral]" Proceedings of the 27th annual conference on Computer
   graphics and interactive techniques. ACM Press/Addison-Wesley Publishing Co.,
   2000.

 * David Hammond, Pierre Vandergheynst, and Remi Gribonval. "[Wavelets on Graphs
   via Spectral Graph Theory.][wavelets]" Applied and Computational Harmonic
   Analysis, 2011.

[signals]: http://dx.doi.org/10.1109/MSP.2012.2235192
[spectral]: http://dx.doi.org/10.1145/344779.344924
[wavelets]: http://dx.doi.org/10.1016/j.acha.2010.04.005

# Algorithms

In general, network state compression algorithms work like this:

![bigidea](the-big-idea.png "The Big Idea")

 1. The compression algorithm takes in the state of the network and its
    topology.
 2. The algorithm compresses the network state and produces an
    algorithm-specific compressed network state. The size (in bytes) of the
    compressed state is determined by the *budget* given to the algorithm. Thus,
    because the size of the compressed state can be set, it must be a lossy
    compression.
 3. Finally, the network state can be decompressed, but with some information
    loss.

It is important to note that the *topology* of the network is never compressed,
only the *values* associated with each node. Thus, the only different between
the original network and the compressed-then-decompressed network is the node
values (or state). The edges don't change.

We measure the error of the compression by taking the [Sum of Squared Errors
(SSE)][SSE]. This is computed by looking at the original network state and the
new network state after a compression-decompression cycle. For each pair of
nodes corresponding to the two networks, the difference between their states is
squared and summed up, producing the *error* of the compression.

[SSE]: http://en.wikipedia.org/wiki/Residual_sum_of_squares

We studied three different algorithms for network state compression. Most of our
time was spent studying Slice Tree and implementing the Spectral Graph Fourier
algorithm. The third algorithm, Spectral Graph Wavelets, was not studied in
great depth nor were we able to find or devise a working implementation under
our time constraints. Thus, information on this algorithm is sparse.

## Slice Tree

Slice Tree was created by Arlei Silva and is described in his paper "Network
State Summarization via In-Graph Compression" (which is unpublished at the time
of this writing).

Slice Tree partitions a network into smooth regions such that each region can be
compactly represented by a single value. This single value summarizes the values
of the nodes inside the region by taking the average of those values. A *smooth*
region is defined to be one that contains values that do not significantly
differ from each other across the topology of the region.

As slices are chosen, they are inserted into a "slice tree". Thus, forming
something like this:

![slicetree](slice-tree.png "Example of a Slice Tree")

Each leaf node corresponds to a region of the network.

There are two main variants of Slice Tree: a greedy version and an approximate
version. Each variant determines how a slice is chosen that is to be inserted
into the tree.

### Greedy Slice

While constructing the Slice Tree, the greedy algorithm selects the best slice
at each iteration. The best slice is defined to be the one that contributes to
the highest error reduction. All nodes and all possible radii at those nodes are
searched to find the largest error reduction. Intuitively, *error reduction* is
the amount of error that is removed by introducing another slice. Put another
way, a network with 1 slice will have the greatest amount of error because all
the node values in the network will be reduced to a single node value. By
taking a second slice, and grouping nodes with similar values into that slice,
the error should be further reduced. As the number of slices approaches the
number of nodes, the error approaches 0. The goal is to make the error approach
0 as quickly as possible while the number of slices increases.

### Approximate Slice

Sampling takes a slightly different approach. Instead of finding the best slice
at a particular iteration, it *approximates* the best slice. This is done by
generating a set of all possible slices, and then pruning those slices until
only the best approximate slice is left. Using a small sample of node values
from the entire network, the slice from the list of candidate slices with the
maximum estimated error reduction is used as the current best slice. This is
done for each iteration of a loop during which the pool of candidate slices is
pruned. Thus, the slice with the best *estimated* error reduction is returned by
this algorithm.

There are three parameters used to tune this algorithm:

 * A confidence parameter *δ* (delta).
 * An approximation constant *ρ* (rho).
 * A sampling rate *π* (pi).

If `δ = 0`, `ρ = 1`, and `π = 1`, then the approximate slice tree algorithm is
the same as the greedy version and finds the best slice without approximation.

## Spectral Graph Fourier

## Spectral Graph Wavelets

# Datasets

We were provided with five real-world datasets to test the effectiveness of the
different methods on.

Three of these datasets were already processed and in the form of a network:

 * **Traffic**: A highway network of Los Angeles, CA with node values
   corresponding to average speeds at highway locations along time. For each
   time interval, there is a separate set of node values. These values are
   expected to be smooth across the topology of the network. This network
   consists of 1,923 nodes and 2,659 edges.

 * **Human**: A gene network for *Homo sapiens* with gene and protein
   interactions as edges and tissue expressions as node values. The number of
   nodes ranges from 540 to 3,178 and the number of edges range from 251 to
   6,856.

 * **DBLP**: An academic co-authorship network in which author are nodes and
   publication counts are values. An edge between nodes indicates co-authorship.
   This network consists of 1,291,210 nodes and 5,227,553 edges.

The other two datasets needed to be processed:

 * **Twitter**: This consists of all the raw tweets from June through December
   of 2009. Also included is a list of which users are following who. The raw
   tweets were processed to generate a network where nodes are users, a node's
   value is the average response time for that user to retweet another user's
   message, and an edge indicates that a user is following another user. Users
   who have not made any retweets are not included in the network. Similarly,
   retweets that do not exactly match the original message are also not factored
   in. The resulting network consists of 773,977 nodes and 465,150 edges.

 * **Wikipedia**: Only minor processing was needed for the Wikipedia dataset.
   Each node is an article, the node value is the total number of views for that
   article, and an edge means that one article links to another. The network
   state consists of view counts from the years 2008 through 2011. This network
   consists of 15,148,210 nodes and 2,434,781 edges.

These datasets are also documented in their respective directories under
`data/`.

Additionally, each of these datasets were reduced to 1000 nodes each. The script
that does this is `reduce.py` under `tools/`. It works by choosing a random node
(or center) from the network and doing a breadth-first search from that
location. This continues until the specified number of nodes are collected or if
the pool of nodes is exhausted. Then, the selected nodes and the edges between
them are written out to their respective `.data` and `.graph` files.

There is one major problem with this approach to reduction. For networks with
many small connected components (i.e., disconnected sub-networks), such as the
Wikipedia network, this results in networks with very few or no edges. Instead,
nodes should be drawn from the largest connected components first. However, due
to time constraints, this was never implemented.

# Experiments and Results

We performed three experiments using Greedy Slice Tree and Spectral Graph
Fourier algorithms. Note that, due to time constraints, the Spectral Graph
Wavelets method is not included in these experiments. The purpose of these
experiments is to assess the effectiveness of each algorithm in terms of
scalability, accuracy, and sensitivity to the network.

## Scalability

For this experiment, we use Los Angeles traffic network with ~1900 nodes.  We
set a fixed compression size of 100 bytes and vary the number of nodes in the
network using the graph reduction tool. The number of nodes range from 100 to
~1900 nodes. We start from 100 nodes to ensure that the budget does not exceed
the number of nodes. The time taken to perform the network state compression for
each algorithm is recorded.

From this, we can see a clear trend that the Spectral Graph Fourier method takes
far longer than Slice Tree as the number of nodes increases. Thus, Slice Tree is
more scalable.

## Accuracy

For this experiment, we keep the number of nodes fixed and vary the compressed
size (or budget) and measure the SSE for each algorithm. As the budget
approaches the total size of the network state, the SSE should approach 0. With
a minimal budget, the SSE should be at a maximum. Again, we use the traffic
network for this experiment, thus the maximum SSE is specific to this network.

From this, we can see that Slice Tree tends to zero significantly faster than
Fourier. Thus, for this dataset, Slice Tree gives a more accurate compressed
network state. This is to be expected because the Los Angeles traffic network
has values that are smooth across the network.

## Dataset Comparison

For this experiment, we want to compare the relative compression accuracy for
each algorithm and each dataset. Each dataset is reduced to 1000 nodes and
compressed to 600 bytes. We measure the SSE of the compressed state that each
algorithm produces.

We find that, in general, Slice Tree produces a slightly more accurate
compressed network state. Yet, for the Los Angeles traffic network, Slice Tree
gives much better results than the Fourier method. Again, this is to be expected
because the traffic network is smooth.

# Future Experiments

Here are some ideas for future experiments:

 * Do multiple compression-decompression cycles to see how the SSE changes from
   the original network state and the final decompressed network state. For
   Slice Tree, it is expected that the SSE should not change regardless of the
   number of compression-decompression cycles because the same slices should be
   selected each time.

 * Compare the scalability and accuracy of the two versions of Slice Tree.

# Future Work

## Outlier Detection

Find nodes with outlier values from the compressed network state. For Slice
Tree, the idea is that outliers should be put into their own slices because they
have no similar values around it. This can be useful, for example, in traffic
networks where we want to find areas of congestion.

## Value Prediction

Predicting the value of a node based on the compressed values of its neighbors.
This can be useful for making predictions about changes to a node's state.

## Trend Analysis/Change

For dynamic networks, node values may change, and new nodes and may be added
over time. Analysis of these changes can be done to understand how values are
evolving. Abrupt or unexpected changes to the network may also be identified.
Again, this can be useful for real-world networks such as traffic networks.

## Code Base

Our code base can be improved quite a bit. There are a couple of major changes
that can be made:

 * Merge dataset processing, reduction, and experiments into one or more
   Makefiles. This will allow these actions to be done in parallel using `make
   -j8`, for example. This will also automate everything and aid
   reproducibility.

   However, using `make` for everything may prove challenging because it does
   not support multiple outputs for a single rule very well.  Other build
   systems such as [Tup][], [SCons][], [CMake][], [Rake][], or [Ninja][] may be
   better suited.

 * Python is used because it is fast to develop and prototype in. However,
   execution time is not so fast. Most of the tools can be rewritten in a faster
   language (such as C++ or D) and parallelized to give significant speedups.

[Tup]: http://gittup.org/tup/
[SCons]: http://www.scons.org/
[CMake]: http://www.cmake.org/
[Rake]: https://github.com/jimweirich/rake
[Ninja]: http://martine.github.io/ninja/
