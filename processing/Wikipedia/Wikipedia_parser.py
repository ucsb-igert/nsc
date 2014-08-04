import os
import sys
import numpy as np
import csv
import argparse

DATA_FILE_EXT = '.data'
LENGTH = 15148210

def read_file(src):
	"""

	"""
	sys.stderr('Reading "%s" view file...', src)
	articles_view_count = np.zeros(LENGTH, dtype=np.intc)
	with open(src, 'rb') as views_file:
		for line in views_file:
			article_id, day, view_count = [int(i) for i in line.strip().split(',')]
			articles_view_count[article_id] += view_count
	return articles_view_count

def write_file(dest, articles_view_count):
	print 'Writing to "{}" data file...'.format(dest)
	with open(dest, 'wb') as output_file:
		writer = csv.writer(output_file)
		for row in enumerate(articles_view_count):
			writer.writerow(row)

def line_count(map_file_path):
	with open(map_file_path, 'rb') as map_file:
		map_file.seek(-1024, 2)
		num_articles = int (map_file.readlines()[-1].decode().split()[1])
	return num_articles


parser = argparse.ArgumentParser(description='Processes wiki files.')
parser.add_argument('src', default=sys.stdin, help='Input file.')
parser.add_argument('--lengthfile', help='Specify map file for length.')

if __name__ == "__main__":
    args = parser.parse_args()
    src = args.src
    if args.lengthfile:
    	LENGTH = line_count(args.lengthfile)
    	print 'Length was changed to {}'.format(LENGTH)
    articles_view_count = read_file(src)
    dest = os.path.splitext(src)[0] + DATA_FILE_EXT
    write_file(dest, articles_view_count)

