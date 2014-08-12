from .paths import data_dir
from os.path import join
from glob import glob
import re

dir = join(data_dir, "DBLP")
data = glob(join(dir, "*.data"))
graph = join(dir, "dblp.graph")
