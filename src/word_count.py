#!/usr/bin/env python2.7
"""
This word_count module will read data from STDIN, split into words and output a
list of tuples containing words and total counts to wc_output/wc_result.txt.

Also , this module will output running median count to wc_output/med_result.txt
"""

import sys
import string
from collections import defaultdict
from bisect import insort
from blist import blist

def read_input(file_ptr):
    """ Generator function
        yielding an iterator of lines inside the file pointer
    """
    for line in file_ptr:
        # Transformations for each line
        # 1. strip() - remove leading and trailing whitespace
        # 2. lower() - change to lower case
        # 3. translate() - remove punctuation
        # 4. split() - split the line into words
        yield line.strip().lower().translate(string.maketrans("", ""),
                                             string.punctuation).split()

def main(separator='\t'):
    """ main routine for word_count module """
    median_ofile = open('wc_output/med_result.txt', 'w')
    wcount_ofile = open('wc_output/wc_result.txt', 'w')
    # blist - replacement for Python built-in list
    #         with better performance on insort O(log**2 n)
    # counts - sorted list to store all the word counts
    counts = blist()
    # Using defaultdict to count the words
    word_dict = defaultdict(int)
    # from STDIN (standard input)
    data = read_input(sys.stdin)
    for words in data:
        # insert the new word count to list counts in sorted order
        insort(counts, len(words))
        # write running median to median_ofile
        counts_len = len(counts)
        if counts_len % 2 == 0:
            median_ofile.write('{:.1f}\n'.format((counts[counts_len//2-1] +
                                                  counts[counts_len//2])/2.0))
        else:
            median_ofile.write('{:.1f}\n'.format(counts[counts_len//2]))
        # Accumulate word count into word_dict
        for word in words:
            word_dict[word] += 1
    # Sort word_dict and write tuple (word, count) to wcount_ofile
    for word, count in sorted(word_dict.items()):
        wcount_ofile.write(word+separator+str(count)+'\n')
    median_ofile.close()
    wcount_ofile.close()

if __name__ == "__main__":
    main()

