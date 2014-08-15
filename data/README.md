# Reference Datasets

This project contains the documentation for the five real-world datasets used to
test network state compression methods.

## Datasets

The following is a list of each dataset and their corresponding description.

 * **DBLP**: Academic co-authorship network in which author nodes are annotated
   with publication counts for 15 research areas.

 * **Human**: Gene network for *Homo sapiens* with gene and protein interactions
   as edges and tissue expression as node value (114 tissues).

 * **Traffic**: Highway network of Los Angeles, CA with node values
   corresponding to average speeds at highway locations along time.

 * **Twitter**: Unprocessed dataset. Contains a list of tweets for several
   months from the year 2009.

 * **Wikipedia**: Unprocessed dataset. Contains the number of views/edits for
   Wikipedia pages between 2008 and 2011.

For more details, see each `README.md` file under the corresponding directory
for each dataset.

## Network Format

Each network consists of two main files, the `*.data` and `*.graph` files.

`*.data` files contain the state corresponding to each node and have the format

    <integer>,<double>\n

where the first column is the node ID and the second column is that node's
value (or state).

For example:

    4,6.283185
    8,3.14
    15,1.61803
    16,2.71828
    23,10.0
    42,1.0

`*.graph` files contain the set of all edges between nodes and have the
format

    <integer>,<integer>\n

where an edge is going from the node in the first column to the node in the
second column.

For example:

    4,15
    4,23
    15,16
    15,23
    16,23

