# Twitter Dataset

This dataset consists of raw lists of tweets from June to December 2009.

The format for each file is given as a regular expression. Curly braces `{}` are
used to denote a group of expressions.

## Source

[Stanford Network Analysis Project](http://snap.stanford.edu/data/twitter7.html)

## Files

### `raw/tweets2009-*.txt`

Format:

    ^total number:(\d+)$
    {
        ^T\t((\d{4}=\d{2}-\d{2} \d{2}:\d{2}:\d{2})$
        ^U\t.*?/([^/\n]+)$")
        ^W\t(.*)$")
    }*

Each of these files contains the raw list of tweets for that month. Each entry
consists of a time stamp, URL to the user, and their message. The number of
entries is given in the first line of each file.

### `raw/numeric2screen`

Format:

    {(\d+) (\w+)\n}*

This file contains a mapping between Twitter user names and numeric identifiers.


### `raw/twitter_rv.net`

Format:

    {^(\d+)\t(\d+)$}*

This file contains the links between users that "follow" each other. For
example, `12\t237` means that the user with ID `12` follows the user with id
`237`. The mapping between user IDs and user names is given in the file
`numeric2screen`.

## Processing

The above raw files are processed using the scripts `data` and `graph`.

### Data

The `data` script generates a list of users and their average response time to
retweet. For example, to generate the response times for all users in 2009, the
following command can be used:

```bash
$ ./data --usermap raw/numeric2screen raw/tweets2009-*.txt > twitter.data
```

This can take a very long time and use a lot of memory, progress of the
processing is written to `stderr`. On a machine with a 2.6 GHz processor, it
took ~10 hours and ~200 GiB of memory.

### Graph

The `graph` script simply reformats `twitter_rv.net` (the mapping of followers):

```bash
$ ./graph < twitter_rv.net > twitter.graph
```
