# Generates the data and plots for this experiment.
#
# Usage:
#     make -j4
#
# This may take quite a while to complete.
#
# Author: Jason White
.PHONY: all clean

all: plot.png


DATA_DIR=../../data

DBLP_DATA=${DATA_DIR}/DBLP/reduced/1000.dblp_ai.data
DBLP_GRAPH=${DATA_DIR}/DBLP/reduced/1000.dblp_ai.graph

HUMAN_DATA=${DATA_DIR}/Human/reduced/1000.human_0.data
HUMAN_GRAPH=${DATA_DIR}/Human/reduced/1000.human_0.graph

SYNTHETIC_DATA=${DATA_DIR}/Synthetic/reduced/1000.synthetic.data
SYNTHETIC_GRAPH=${DATA_DIR}/Synthetic/reduced/1000.synthetic.graph

TRAFFIC_DATA=${DATA_DIR}/Traffic/reduced/1000.traffic_0.data
TRAFFIC_GRAPH=${DATA_DIR}/Traffic/reduced/1000.traffic_0.graph

TWITTER_DATA=${DATA_DIR}/Twitter/reduced/1000.twitter.data
TWITTER_GRAPH=${DATA_DIR}/Twitter/reduced/1000.twitter.graph

WIKIPEDIA_DATA=${DATA_DIR}/Wikipedia/reduced/1000.wiki-views-2010-day.data
WIKIPEDIA_GRAPH=${DATA_DIR}/Wikipedia/reduced/1000.wiki-views-2010-day.graph

# The order of these datasets matters. The program expects each of them to be in
# this order: DBLP, Human, Synthetic, Traffic, Twitter, Wikipedia
DATASETS=${DBLP_DATA} ${DBLP_GRAPH} \
		 ${HUMAN_DATA} ${HUMAN_GRAPH} \
		 ${SYNTHETIC_DATA} ${SYNTHETIC_GRAPH} \
		 ${TRAFFIC_DATA} ${TRAFFIC_GRAPH} \
		 ${TWITTER_DATA} ${TWITTER_GRAPH} \
		 ${WIKIPEDIA_DATA} ${WIKIPEDIA_GRAPH}

slicetree.csv: ${DATASETS}
	./sse_slicetree $^ > $@

fourier.csv: ${DATASETS}
	./sse_fourier $^ > $@

plot.png: slicetree.csv fourier.csv
	./plot $^ $@

clean:
	${RM} *.csv *.png
