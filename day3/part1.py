#!/usr/bin/python

position_x = 0
position_y = 0

min_x = 0
max_x = 0
min_y = 0
max_y = 0


with open('input.txt') as f:
  # Start by figuring out the size of our world
  for line in f:
    for instruction in line:
      if instruction == '<':
        position_x -= 1
        if position_x < min_x:
          min_x = position_x
      elif instruction == '>':
        position_x += 1
        if position_x > max_x:
          max_x = position_x
      elif instruction == '^':
        position_y -= 1
        if position_y < min_y:
          min_y = position_y
      elif instruction == 'v':
        position_y += 1
        if position_y > max_y:
          max_y = position_y

print 'Original coodinate range is (',min_x,',',min_y,') to (',max_x,',',max_y,')'

# We're going to be storing the counts in arrays, let's stay positive
max_x -= min_x
max_y -= min_y

print 'Normalised coordinate range is (0,0) to (',max_x,',',max_y,')'

# Generate our worldspace
world = [[0 for i in xrange(max_y + 1)] for i in xrange(max_x + 1)]

# Reposition the start coordinates so we don't fall off the edge
position_x = -min_x
position_y = -min_y

print 'Positioning ourselves at (',position_x,',',position_y,')'

# Santa delivers to the home spot first
world[position_x][position_y] = 1;

with open('input.txt') as f:
  for line in f:
    for instruction in line:
      if instruction == '<':
        position_x -= 1
      elif instruction == '>':
        position_x += 1
      elif instruction == '^':
        position_y -= 1
      elif instruction == 'v':
        position_y += 1

      if instruction.strip():
        # Let's stay in single digits, for pretty map output reasons
        if world[position_x][position_y] < 9:
          world[position_x][position_y] += 1
          

# Print the world map
print('\n'.join([''.join(['{0:1}'.format(item) for item in row]) for row in world]))

# Finally, find how many houses got presents
dupes = 0
for x in world:
  for y in x:
    if y > 0:
      dupes += 1

print 'There were', dupes, 'houses with multiple presents'
