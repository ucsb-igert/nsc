# Generates the data and plots for this experiment.
#
# Usage: 
#     make -j4
#
# Author: Jason White
.PHONY: all clean

all: smooth.plot.png rough.plot.png

SMOOTH_DATA=../../data/Traffic/traffic_0.data
GRAPH=../../data/Traffic/traffic.graph

ROUGH_DATA=../../data/Traffic/traffic_random.data

${ROUGH_DATA}: ${SMOOTH_DATA}
	../../tools/randomize < $^ > $@

smooth.slicetree.csv: ${SMOOTH_DATA} ${GRAPH}
	./sse_slicetree $^ 1> $@

smooth.fourier.csv: ${SMOOTH_DATA} ${GRAPH}
	./sse_fourier $^ 1> $@

rough.slicetree.csv: ${SMOOTH_DATA} ${GRAPH}
	./sse_slicetree $^ 1> $@

rough.fourier.csv: ${SMOOTH_DATA} ${GRAPH}
	./sse_fourier $^ 1> $@

smooth.plot.png: smooth.slicetree.csv smooth.fourier.csv
	./plot $^ $@

rough.plot.png: rough.slicetree.csv rough.fourier.csv
	./plot $^ $@

clean:
	${RM} *.csv *.png
