#!/usr/bin/python

def interpolate(row):
    col = 0
    ret = []
    while col < num_cols:
        col_width = max_lengths[col]
        val_width = len(row[col])
        whitespace = col_width - val_width
        left_space = whitespace/2
        right_space = whitespace - left_space
        ret.append("%s%s%s" % (" "*left_space, row[col], " "*right_space))
        col += 1
    return ret

from sys import stdin
line = stdin.readline()
table = []
num_cols = len(line.rstrip('\n').split(','))
max_lengths = [0] * num_cols

while line != "":
    row = line.rstrip('\n').split(',')
    index = 0
    for v in row:
        if len(v) > max_lengths[index]:
            max_lengths[index] = len(v)
        index += 1
    table.append(line.rstrip('\n').split(','))
    line = stdin.readline()

row_width = sum(max_lengths) + num_cols + 1

for row in table:
    row = interpolate(row)
    print "|%s|" % "|".join(row)
    print "-"*row_width

