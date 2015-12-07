#!/usr/bin/python

total_ribbon = 0

with open('input.txt') as f:
  for line in f:
    l, w, h = line.split('x')
    # Convert to ints
    l, w, h = [int(c) for c in [l, w, h]]

    smallest, middle, largest = sorted([l, w, h])
    this_ribbon = 2 * smallest + 2 * middle
    this_bow = smallest * middle * largest

    total_ribbon += this_ribbon + this_bow

print 'Total ribbon required is', total_ribbon, 'feet'

