#!/usr/bin/python

floor = 0
position = 0

with open("input.txt") as f:
  for line in f:
    for char in line:
      position += 1

      if char == '(':
        floor += 1
      elif char == ')':
        floor -= 1

      if floor < 0:
        print 'We enter the basement on position', position
        break
