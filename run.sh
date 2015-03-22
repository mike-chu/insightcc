#!/usr/bin/env bash

##############################################
## Installing Python module blist if needed
##############################################
## blist is a drop-in replacement for the Python list that provides better
## performance when modifying large lists
##
## Use Case	                                    blist	    list
## Maintain a sorted lists with bisect.insort	O(log**2 n)	O(n)
##
## PyPi link: http://pypi.python.org/pypi/blist/
#### Uncomment this line and comment out the next line if using Max OSX #### pip install blist
apt-get install python-blist ## For Debian / Ubuntu Linux

##############################################
## Setting Run Permission on Python script
##############################################
chmod a+x ./src/word_count.py

##############################################
## Running the Python script
##############################################
# First, concatenate all the files under wc_input directory in alphabetical order
# Then, redirect as STDIN to word_count.py
cat wc_input/* | ./src/word_count.py

