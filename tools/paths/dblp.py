from .paths import data_dir
from os.path import join
from glob import glob

data = glob(join(data_dir, "DBLP", "*.data"))
graph = join(data_dir, "DBLP/dblp.graph")
