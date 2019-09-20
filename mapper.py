#!/usr/bin/env python
import sys
from sklearn.feature_extraction import stop_words
import string

# get all lines from stdin
for line in sys.stdin:

    # remove leading and trailing whitespace
    line = line.strip()

    # Make lower case
    line = line.lower()

    # remove punc
    line  = line.translate(None, string.punctuation)

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    stops = set(stop_words.ENGLISH_STOP_WORDS)

    for word in words:
     if word not in stops:
        print '%s\t%s' % (word, "1")
