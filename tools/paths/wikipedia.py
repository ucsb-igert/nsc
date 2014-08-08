from .paths import data_dir
from os.path import join

data = map(lambda data: join(data_dir, "Wikipedia", data), [
    "wiki-views-2008-day.data",
    "wiki-views-2009-day.data",
    "wiki-views-2010-day.data",
    "wiki-views-2011-day.data",
    ])

graph = join(data_dir, "Wikipedia/wiki-links.graph")
