from .paths import data_dir
from os.path import join
from glob import glob

dir = join(data_dir, "Synthetic")
data = join(dir, "synthetic.data")
graph = join(dir, "synthetic.graph")

reductions = {
    1000: (join(dir, "synthetic.1000.data"), join(dir, "synthetic.1000.graph"))
}
