#!/usr/bin/env python

from flask import Flask, request, render_template, Response
from pygments import highlight               
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pprint import pformat

from request_properties import REQUEST_PROPERTIES

app = Flask(__name__)

#formatter = HtmlFormatter(style="colorful")
formatter = HtmlFormatter()

@app.route("/")
def index():
    data = {}
    for field in REQUEST_PROPERTIES:
        data[field] = getattr(request, field)
    data = pformat(data, indent=1, width=80, depth=None, compact=False) #py38: sort_dicts=True
    content = highlight(data, get_lexer_by_name("python"), formatter)
    return render_template('base.html', content=content)

@app.route("/pygments.css")
def pygments_css():
    return Response(formatter.get_style_defs(".highlight"), mimetype="text/css")
