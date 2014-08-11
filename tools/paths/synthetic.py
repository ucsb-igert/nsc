from .paths import data_dir
from os.path import join
from glob import glob

dir = join(data_dir, "Synthetic")
data = sorted(glob(join(dir, "*.data")))
graph = sorted(glob(join(dir, "*.graph")))
