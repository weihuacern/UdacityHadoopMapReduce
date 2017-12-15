#!/usr/bin/env python
import sys
import math

if __name__ == '__main__':
  highestSale = 0
  oldKey = None

  for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
      # Something has gone wrong. Skip this line.
      continue

    thisKey, thisSale = data
    if oldKey and oldKey != thisKey:
      print (oldKey, "\t", highestSale)
      highestSale = 0

    oldKey = thisKey
    if highestSale < float(thisSale):
      highestSale = float(thisSale)

  if oldKey != None:
    print ( oldKey, "\t", highestSale )
