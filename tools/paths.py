"""
Various paths. This makes it easier to reference file paths within this
repository.

Author: Jason White
"""

from os.path import *
from glob import glob

# Data directory.
data_dir = relpath(join(dirname(__file__), "../data"))

# List of datasets and their locations.
datasets = {
    "dblp": {
        "data": glob(join(data_dir, "DBLP", "dblp_*.data")),
        "graph": join(data_dir, "Wikipedia/wiki-links.graph"),
    },

    "twitter": {
        "data": join(data_dir, "Twitter/twitter.data"),
        "graph": join(data_dir, "Twitter/twitter.graph"),
    },

    "wikipedia": {
        "data": map(lambda data: join(data_dir, "Wikipedia", data), [
            "wiki-views-2008-day.data",
            "wiki-views-2009-day.data",
            "wiki-views-2010-day.data",
            "wiki-views-2011-day.data",
            ]),
        "graph": join(data_dir, "Wikipedia/wiki-links.graph"),
    }
}

#print(datasets)
