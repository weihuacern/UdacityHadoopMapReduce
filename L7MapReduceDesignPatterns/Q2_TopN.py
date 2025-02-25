#!/usr/bin/env python
"""
Your mapper function should print out 10 lines containing longest posts, sorted in
ascending order from shortest to longest.
Please do not use global variables and do not change the "main" function.
"""
import sys
import csv
import io

def mapper():
  reader = csv.reader(sys.stdin, delimiter='\t')
  writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

  length_line_pair = []
  for line in reader:
    # YOUR CODE HERE
    length_line_pair.append([len(line[4]),line])
    #print (line[4])
    #writer.writerow(line)

  N = 10
  #Sort lineWithLength list in descending order,pick the top 10 
  Top_N = sorted(length_line_pair, reverse = True)[0:N]    
  #Sort the Top_N in ascending order to fit the output format
  Top_N = sorted(Top_N, reverse = False)
  #print (len(Top_N)) 
  for record in Top_N:
    #print("\n")
    print(record[1])
    #writer.writerow(record[1])

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
