#!/usr/bin/python

import re
import sys

re_twopairs = re.compile(r'([a-z][a-z]).*\1')
re_onerep   = re.compile(r'([a-z])[a-z]\1')

def main():
  word_count = 0
  nice_word_count = 0
  with open('input.txt') as f:
    for line in f:
      word_count += 1
      word = line.strip()
      if is_nice(word):
        nice_word_count += 1

  print('There are %d / %d nice words"' % (nice_word_count, word_count))


def is_nice(word):
  if not re_twopairs.search(word):
    return 0

  if re_onerep.search(word):
    return 1

  return 0

# Would be nice if python supported forward declaration
main()
