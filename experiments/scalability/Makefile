# Generates the data and plots for this experiment.
#
# Usage:
#     make -j2
#
# This may take quite a while to complete.
#
# Author: Jason White
.PHONY: all clean

DATA=../../data/Traffic/traffic_0.data
GRAPH=../../data/Traffic/traffic.graph

all: plot.png

slicetree.csv: ${DATA} ${GRAPH}
	./time_slicetree $^ 1> $@

fourier.csv: ${DATA} ${GRAPH}
	./time_fourier $^ 1> $@

plot.png: slicetree.csv fourier.csv
	./plot $^ $@

clean:
	${RM} *.csv *.png
