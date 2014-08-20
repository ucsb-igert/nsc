# Description:
# This processes the Twitter dataset. Expect this to run for 10+ hours and to
# consume 200+ GB of RAM.
#
# Usage:
#     make
#
# Author: Jason White
.PHONY: all clean
default: all

TWITTER=../../data/Twitter

# Path to the Twitter dataset
SRC_DIR=${TWITTER}/raw

# List of the tweet files to process.
SRC_TWEETS=$(wildcard ${SRC_DIR}/tweets2009-*.txt)

# Map between numeric identifiers and screen names.
SRC_USERMAP=${SRC_DIR}/numeric2screen

# Links between users.
SRC_GRAPH=${SRC_DIR}/twitter_rv.net

# Output *.data and *.graph files.
OUT_DATA=${TWITTER}/twitter.data
OUT_GRAPH=${TWITTER}/twitter.graph

all: ${OUT_DATA} ${OUT_GRAPH}

# Process the tweets to create the data
${OUT_DATA}: ${SRC_USERMAP} ${SRC_TWEETS}
	./data --usermap ${SRC_USERMAP} ${SRC_TWEETS} > $@

# Reformat the followers file and prunes edges between nodes that don't exist.
${OUT_GRAPH}: ${SRC_GRAPH} ${OUT_DATA}
	sed 's/\t/,/' ${SRC_GRAPH} | ../../tools/prune_edges.py ${OUT_DATA} > $@

clean:
	${RM} ${OUT_DATA} ${OUT_GRAPH}
