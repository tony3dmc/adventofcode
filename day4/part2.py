#!/usr/bin/python

import hashlib
md5 = hashlib.md5()

secret = 'ckczppom'

number = 0
while True:
  number += 1
  attempt = secret + str(number)
  myhash = hashlib.md5(attempt).hexdigest()
  if myhash[:6] == '000000':
    break

print 'Output of %s is %s' % (attempt, myhash)
