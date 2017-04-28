"""
Implement an HTTP web server in Python that knows how to run server-side
CGI scripts coded in Python; serves files and scripts form current 
working dir; Python scripts must be stored in webdir\cgi-bin or 
websir\htbin
"""

import os, sys

from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'  # where your html files and cgi-bin script directory live
port = 80  # default http://localhost/, else use http://localhost:xxxx/

os.chdir(webdir)  # run in HTML root dir
srvaddr = ("", port)  # my hostname, port number
srvobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvobj.serve_forever()  # run as perpetual daemon
