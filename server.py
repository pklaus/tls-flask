#!/usr/bin/env python

from flask import Flask, request, Response, render_template_string
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pprint import pformat

app = Flask(__name__)

# formatter = HtmlFormatter(style="colorful")
formatter = HtmlFormatter()

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>tls-flask</title>
    <link rel="stylesheet" type="text/css" href="/pygments.css">
  </head>
  <body>
    {{ content|safe }}
  </body>
</html>
""".strip()

REQUEST_PROPERTIES = [
    "environ", "path", "full_path", "script_root", "url", "base_url", "url_root", "accept_charsets", "accept_encodings",
    "accept_languages", "accept_mimetypes", "access_control_request_headers", "access_control_request_method",
    "access_route", "args", "authorization", "base_url", "blueprint", "cache_control", "content_encoding", "content_length",
    "content_md5", "content_type", "cookies", "data", "date", "endpoint", "files", "form", "full_path", "headers", "host",
    "host_url", "if_match", "if_modified_since", "if_none_match", "if_range", "if_unmodified_since", "is_json",
    "is_multiprocess", "is_multithread", "is_run_once", "is_secure", "json", "max_content_length", "max_forwards", "method",
    "mimetype", "mimetype_params", "origin",
]

@app.route("/")
def index():
    data = {}
    for field in REQUEST_PROPERTIES:
        data[field] = getattr(request, field)
    data = pformat(
        data, indent=1, width=80, depth=None, compact=False
    )  # py38: sort_dicts=True
    content = highlight(data, get_lexer_by_name("python"), formatter)
    return render_template_string(TEMPLATE, content=content)


@app.route("/pygments.css")
def pygments_css():
    return Response(formatter.get_style_defs(".highlight"), mimetype="text/css")
