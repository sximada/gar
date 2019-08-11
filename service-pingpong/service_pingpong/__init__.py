#! /usr/bin/env python3
from flask import Flask

__version__ = '0.1.0'

app = Flask(__name__)

@app.route("/")
def root():
    return """<!DOCTYPE html>
<html>
    <head>
	<title>Flask Ping Pong Server</title>
    </head>
    <body>
	<h1>Flask Ping Pong Server</h1>
	<p>
	    Call <a href="/ping/">Ping Pong API</a>.
	</p>
    </body>
</html>
"""

@app.route("/ping/")
def ping():
    return "PONG"
