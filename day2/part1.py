#!/usr/bin/python

total_paper = 0

with open('input.txt') as f:
  for line in f:
    l, w, h = line.split('x')
    # Convert to ints
    l, w, h = [int(c) for c in [l, w, h]]
    # Calculate the three sides
    lw = l*w
    wh = w*h
    hl = h*l

    surface_area = 2*lw + 2*wh + 2* hl

    smallest_side = min([lw, wh, hl])

    this_paper = surface_area + smallest_side

    total_paper += this_paper

print 'Total paper required is', total_paper, 'square feet'

