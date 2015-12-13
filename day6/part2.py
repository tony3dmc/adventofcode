#!/usr/bin/python

from itertools import repeat
import re
import sys

re_range = re.compile('(?P<command>turn on|turn off|toggle) (?P<x1>\d+),(?P<y1>\d+) through (?P<x2>\d+),(?P<y2>\d+)')

world_height = 1000
world_width = 1000

world = [[0 for i in xrange(world_height)] for i in xrange(world_width)]

def main():
  with open('input.txt') as f:
    for line in f:
      match = re_range.match(line)
      command = match.group('command')
      (x1, y1, x2, y2) = [int(i) for i in match.group('x1', 'y1', 'x2', 'y2')]

      if command == 'turn on':
        switch_lights(x1, y1, x2, y2, 1)
      elif command == 'turn off':
        switch_lights(x1, y1, x2, y2, 0)
      elif command == 'toggle':
        toggle_lights(x1, y1, x2, y2)

  print('There is %d total_brightness' % sum_lights())

def switch_lights(from_x, from_y, to_x, to_y, direction):
  for x in range(from_x, to_x + 1):
    for y in range(from_y, to_y + 1):
      if direction:
        world[x][y] += 1
      else:
        if world[x][y] > 0:
          world[x][y] -= 1

def toggle_lights(from_x, from_y, to_x, to_y):
  for x in range(from_x, to_x + 1):
    for y in range(from_y, to_y + 1):
        world[x][y] += 2

def sum_lights():
  light_sum = 0
  for x in world:
    for y in x:
      light_sum += y
  return light_sum

# Run the program
main()
