#!/usr/bin/env python
import sys
import math

if __name__ == '__main__':
  CountTotal = 0
  oldKey = None

  for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
      # Something has gone wrong. Skip this line.
      continue

    thisKey, thisCount = data
    if oldKey and oldKey != thisKey:
      print (oldKey, "\t", CountTotal)
      oldKey = thisKey
      CountTotal = 0

    oldKey = thisKey
    CountTotal += float(thisCount)

  if oldKey != None:
    print ( oldKey, "\t", format(CountTotal, '.2f') )
