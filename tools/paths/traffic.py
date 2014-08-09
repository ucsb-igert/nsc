from .paths import data_dir
from os.path import join
from glob import glob

data = sorted(glob(join(data_dir, "Traffic", "*.data")))
graph = join(data_dir, "Traffic/traffic.graph")
