Insight Data Engineering - Coding Challenge
===========================================

This repository contains Python module in response to Insight Data Engineering Fellow program's coding challenge.

The challenge is to solve one of the first problems in data engineering - Word Count. Along with that, the module will write out a running median of word count in each line of the input text files.

This README page describes the algorithm used to solve the problem.

Reading Input Files
-------------------
For the challenge, it is required to combine all the files inside wc_input directory into a single stream for the program to process.

We are using the bash command `cat` to concatenate the files together. We used pattern matching capability of bash filename expansion. The expansion will return an alphabetically sorted list of filenames under the wc_input directory. Then we are using the bash redirecton and pipe the `cat` output to our Python program as STDIN.

In word_count.py, we have a read_input() that will convert the STDIN stream to an iterator. During the conversion, we have performed these transformations (as to follow instructions in FAQ of the challenge):

1. remove leading and trailing whitespace
2. change to lower case
3. remove punctuation
4. split the line into list of words

Word Count
----------
In this solution, we are using Python dictionary data type to keep track of frequency count of each word. Python dict is like a hash table which is an unordered set of key:value pairs. It serves well for this problem where we will use dict to store the word-frequency pairs.

As we gather more words from the input text file, the dictionary can grow large. For each input word, we will need to first look up if the word exists in the dictionary. If yes, we will increment the count in the dictionary; otherwise, we will add the (word:1) pair to the dictionary. Luckily in Python, the `defaultdict(int)` is an optimized high performance data structure that serves these operations very well.
(This is chosen after some profiling against the Counter class object.)

Lastly, as Python dictionary is an unordered set, we will need to use `sorted()` function onto the dictionary's key and write the result (word, total count) to the output file in alphabetical order as required.

Running median
--------------
In this solution, we are using sorted python list to store the word count collected so far. As we collect a new word count from the new line of input text file, we will insert the new count to the list while maintaining the order of elements inside the list. The `insort()` of bisect module performs this insertion well. However, the built-in Python list didn't perform too well with this `insort()` function and has *O(n)* time complexity.

In effort to optimize this time complexity as n can grow very large with the size of input text files, we have chosen `blist` module [link](http://pypi.python.org/pypi/blist/) as the replacement list data type for the Python built-in type.

Below is the performance comparison of `insort()` between blist and built-in list

|Use Case|blist|list|
|--------|-----|----|
|Maintain a sorted lists with bisect.insort|O(log<sub>2</sub> n)|O(n)|

In the `run.sh`, we have the following line to ensure this dependent module intalled in the platform before the running.

> apt-get install python-blist ## For Debian / Ubuntu Linux

In case of `apt-get` command not available in the system, an alternative way of installation can be used by un-commenting this line.

> pip install blist

Lastly, finding median in a sorted list is just:

- getting the middle element of the list if the length of list is odd
- averaging the middle two elements of the list if the length of list is even

Results
-------
The solution has been tested with **600MB** of text input data. It takes only about **120 sec** to process with a 2.7GHz i5 CPU / OSX 10.10 / 8GB RAM.

