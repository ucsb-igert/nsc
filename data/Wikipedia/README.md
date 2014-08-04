# Wikipedia Dataset

This dataset consists of the number of views/edits for wikipeida pages between 2008-2011.

The format for each file is given as a regular expression. Curly braces `{}` are
used to denote a group of expressions.

# Files

## `wiki-views-*-day.txt`

Format:

	{^(\d+),(\d+)$}*

Each of these files contains the total number of views/edits that a page has had in a year.
For example, '145,7851' means that the article with the page id '145' was viewed/edited '7851' times in that year.

## `wiki-page-maps.txt`

Format:

    {(\w+) (\d+)\n}*

This file contains a mapping between Wikipedia article names and article ids.

## `wiki-links.graph`

Format:

    {^(\d+),(\d+)$}*

This file contains the hyperlinks between Wikipedia pages.
For example, '145,546' means that article id '145' has a hyperlink to article id '546'.


## 'raw/wiki-views-*-text.tar.gz'

Format:

	{^(\d+),(\d+),(\d+)$}*

These files contain the raw view counts for Wikipedia articles per day. 
For example, '145,5,3' means that the article id '145' was viewed/edited '3' times 
on the 5th day of the year. 

## `raw/wiki-links-graph.txt`

Format:

    {^(\d+),(\d+)$}*

This file contains the hyperlinks between Wikipedia pages.
For example, '145,546,3' means that article id '145' has '3' hyperlinks to article id '546'.

