#!/usr/bin/env python
import sys
import math

if __name__ == '__main__':
  salesTotal = 0
  oldKey = None

  for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
      # Something has gone wrong. Skip this line.
      continue

    thisKey, thisSale = data
    if oldKey and oldKey != thisKey:
      print (oldKey, "\t", salesTotal)
      oldKey = thisKey
      salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)

  #salesTotal = round(salesTotal, 2)
  if oldKey != None:
    print ( oldKey, "\t", format(salesTotal, '.2f') )
