from .paths import data_dir
from os.path import join
from glob import glob

data = sorted(glob(join(data_dir, "Human", "*.data")))
graph = sorted(glob(join(data_dir, "Human", "*.graph")))
