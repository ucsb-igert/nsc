# Generates the data and plots for this experiment.
#
# Usage:
#     make -j4
#
# This may take quite a while to complete.
#
# Author: Jason White
.PHONY: all clean

all: smooth.plot.png rough.plot.png

#GRAPH=../../data/Traffic/traffic.graph
#SMOOTH_DATA=../../data/Traffic/traffic_0.data
#ROUGH_DATA=../../data/Traffic/traffic_random.data

GRAPH=../../data/Human/human_0.graph
SMOOTH_DATA=../../data/Human/human_0.data
ROUGH_DATA=../../data/Human/human_0.random.data

${ROUGH_DATA}: ${SMOOTH_DATA}
	../../tools/randomize < $^ > $@

smooth.slicetree.csv: ${SMOOTH_DATA} ${GRAPH}
	./sse_slicetree $^ 1> $@

smooth.fourier.csv: ${SMOOTH_DATA} ${GRAPH}
	./sse_fourier $^ 1> $@

rough.slicetree.csv: ${ROUGH_DATA} ${GRAPH}
	./sse_slicetree $^ 1> $@

rough.fourier.csv: ${ROUGH_DATA} ${GRAPH}
	./sse_fourier $^ 1> $@

smooth.plot.png: smooth.slicetree.csv smooth.fourier.csv
	./plot $^ $@

rough.plot.png: rough.slicetree.csv rough.fourier.csv
	./plot $^ $@

clean:
	${RM} *.csv *.png
