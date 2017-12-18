#!/usr/bin/env python                                                                                                                                                                                       

import sys
import csv
import io
import string

def mapper():
  reader = csv.reader(sys.stdin, delimiter='\t')
  specials = ',.!?:;"()<>[]#$=-/'
  trans = str.maketrans(specials, ' '*len(specials))

  for line in reader:
    # YOUR CODE HERE
    if len(line) == 19:
      #print (line[4])
      Body = line[4]
      NodeID = line[0]
      Body = Body.translate(trans)
      Words = Body.strip().split()
      for thisWord in Words:
        print ( "{0}\t{1}".format( thisWord.lower(), NodeID ) )

test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"333\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"88888888\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"11111111111\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1000000000\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"22\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"4444\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"666666\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"55555\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"999999999\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"7777777\"\t\"\"
"""

# This function allows you to test the mapper with the provided test string
def main():
  from io import StringIO
  #sys.stdin = io.StringIO(test_text)
  mapper()
  sys.stdin = sys.__stdin__

if __name__ == "__main__":
  main()
