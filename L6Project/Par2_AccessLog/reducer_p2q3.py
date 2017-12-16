#!/usr/bin/env python
import sys
import math

if __name__ == '__main__':
  CountTotal = 0
  oldKey = None
  MostCount = 0
  MostKey = None

  for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
      # Something has gone wrong. Skip this line.
      continue

    thisKey, thisCount = data
    if oldKey and oldKey != thisKey:
      print ( oldKey, "\t", CountTotal )
      if MostCount < CountTotal : 
        MostCount = CountTotal
        MostKey = oldKey
      oldKey = thisKey
      CountTotal = 0

    oldKey = thisKey
    CountTotal += 1

  if oldKey != None:
    print ( oldKey, "\t", CountTotal )
    if MostCount < CountTotal : 
      MostCount = CountTotal
      MostKey = oldKey

print ("Most popular path: ", MostKey)
print ("Count of most popular ", MostCount)
