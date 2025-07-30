#!/usr/bin/env python3

fname = input("Enter the filename: ")
# fh = open(fname)
# lines = fh.readlines()
# for line in lines:
#     print(line.strip())

# # Do not forget to close the file handle
# fh.close()

with open(fname) as fh:
    lines = fh.readlines()
    for line in lines:
        print(line)