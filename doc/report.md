# Introduction

The purpose of this project is to compare competing approaches for network state
compression. The networks we are interested in have nodes with associated values
or *states*. Network state compression refers to the translation of these
states to a more compact form. For the compression methods we investigated, all
are lossy. Thus, we are mainly concerned about the accuracy and scalability of
the compression algorithms.

# Relevant Work

There are four papers relevant to this project. These are:

 * Arlei Silva, Petko Bogdanov, Ambuj K. Singh. "Network State Summarization via
   In-Graph Compression". Under review, 2014.
 * David Shuman, et al. "[The Emerging Field of Signal Processing on Graphs:
   Extending high-dimensional data analysis to networks and other irregular
   domains.][signals]" Signal Processing Magazine, 2013.
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

# Data Processing

We were provided with five real-world datasets to test the different methods on.

Three of these datasets were already processed and in the form of a network.
These include:

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

The other two datasets needed to be processed. These include:

 * **Twitter**: This consists of all the raw tweets from June through December
   of 2009. Also included is a list of which users are following who. The raw
   tweets were processed to generate a network where nodes are users, a node's
   value is the average response time for that user to retweet another user's
   message, and an edge indicates that a user is following another user. Users
   who have not made any retweets are not included in the network. Similarly,
   retweets that do not exactly match the original message are also not factored
   in.

 * **Wikipedia**: Only minor processing was needed for the Wikipedia dataset.
   Each node is an article, the node value is the total number of views for that
   article, and an edge means that one article links to another. The network
   state consists of view counts from the years 2008 through 2011. This network
   has 15,148,210 nodes and 2,434,781 edges.

# Methods

## Slice Tree

## Spectral Graph Fourier

## Spectral Graph Wavelets

# Experiments

## Scalability

## Accuracy

## Dataset Comparison

# Results and Analysis

# Future Experiments

# Future Work

## Outlier Detection

## Value Prediction

## Trend Analysis/Change
