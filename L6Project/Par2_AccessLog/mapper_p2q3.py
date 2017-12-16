#!/usr/bin/env python
# Your task is to make sure that this mapper code does not fail on corrupt data lines,
# but instead just ignores them and continues working
import sys
import io
import re
'''
10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET / HTTP/1.1" 403 202
10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET /favicon.ico HTTP/1.1" 404 209
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET / HTTP/1.1" 200 9157
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/css/reset.css HTTP/1.1" 200 1014
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/css/960.css HTTP/1.1" 200 6206
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/css/the-associates.css HTTP/1.1" 200 15779
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/the-associates.js HTTP/1.1" 200 4492
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lightbox.js HTTP/1.1" 200 25960
10.223.157.186 - - [15/Jul/2009:15:50:36 -0700] "GET /assets/img/search-button.gif HTTP/1.1" 200 168
'''
# %h %l %u %t \"%r\" %>s %b
'''
%h is the IP address of the client
%l is identity of the client, or "-" if it's unavailable
%u is username of the client, or "-" if it's unavailable
%t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
%r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.
%>s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found). See more information on status codes in W3C.org
%b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.
'''

# Note, we need to clean the source file, for the line contain "" or The As, need some special treatment
def mapper():
  # read standard input line by line
  for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
      ip_address, identity, username, datetime, timezone, method, path, proto, status, size = data
      cleaned_path = re.sub(r"^http://www.the-associates.co.uk", '', path)
    print ("{0}\t{1}".format(cleaned_path, 1))
   
test_text = """10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET / HTTP/1.1" 403 202
10.223.157.186 - - [15/Jul/2009:14:58:59 -0700] "GET /favicon.ico HTTP/1.1" 404 209
10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET / HTTP/1.1" 200 9157"""

# This function allows you to test the mapper with the provided test string
def main():
  from io import StringIO
  #sys.stdin = io.StringIO(test_text)
  mapper()
  sys.stdin = sys.__stdin__

if __name__=='__main__':
  main() 
