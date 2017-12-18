#!/usr/bin/env python
import math
import sys, csv, string
import numpy as np

if __name__ == '__main__':

  Count1 = 0 #fantastically
  UIDList1 = np.array([]) #fantastically uid list
  Count2 = 0 #fantastic
  UIDList2 = np.array([]) #fantastic uid list

  for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
      # Something has gone wrong. Skip this line.
      continue

    thisKey, thisValue = data
    #print (int(thisValue))
    if thisKey == "fantastically":
      #print (thisKey, "\t", thisValue)
      Count1 += 1
      UIDList1 = np.append(UIDList1, float(thisValue))
    elif thisKey == "fantastic":
      #print (thisKey, "\t", thisValue)
      Count2 += 1
      UIDList2 = np.append(UIDList2, float(thisValue))

  #UIDList2 = np.append(UIDList2, 1)
  #UIDList2 = np.append(UIDList2, 3)
  #UIDList2 = np.append(UIDList2, 2)
  UIDList1.sort()
  UIDList2.sort()
  print ( "Total Count of fantastically\t", Count1 )
  print ( "Total Count of fantastic\t", Count2 )
  print ( "UID list of fantastically, sorted\t", UIDList1 )
  print ( "UID list of fantastic, sorted\t", UIDList2 )
