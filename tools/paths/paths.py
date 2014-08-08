from os.path import *

# Data directory.
data_dir = relpath(join(dirname(__file__), "../../data"))

# Slice tree algorithm directory
slice_tree_dir = relpath(join(dirname(__file__), "../../algorithms/slice-tree"))

# Path to the slice tree executable
slice_tree = join(slice_tree_dir, "graph_compression")
