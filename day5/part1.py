#!/usr/bin/python

def main():
  # word = 'aaa'
  # if is_nice(word):
  #   print('%s is a nice word' % word)
  # else:
  #   print('%s is a naughty  word' % word)
  # 
  # return 0

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
  vowels = ['a', 'e', 'i', 'o', 'u']
  vowel_count = 0
  for letter in word:
    if letter in vowels:
      vowel_count += 1
  if vowel_count < 3:
    return 0

  banned_substrings = ['ab', 'cd', 'pq', 'xy']
  for substring in banned_substrings:
    if substring in word:
      return 0

  last_letter = ''
  for letter in word:
    if letter == last_letter:
      return 1

    last_letter = letter

  return 0

# Would be nice if python supported forward declaration
main()
