#!/usr/bin/env python
import sys
import math

if __name__ == '__main__':
  Total = 0
  Count = 0

  for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
      # Something has gone wrong. Skip this line.
      continue

    thisKey, thisSale = data
    Count += 1
    Total += float(thisSale)

  print ("Total", "\t", Total)
  print ("Count", "\t", float(Count))
