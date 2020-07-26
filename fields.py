
"""
The FIELDS are all properties of the flask.Request
object that can be accessed easily.
See https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data
"""

FIELDS = """
environ
path
full_path
script_root
url
base_url
url_root
accept_charsets
accept_encodings
accept_languages
accept_mimetypes
access_control_request_headers
access_control_request_method
access_route
args
authorization
base_url
blueprint
cache_control
content_encoding
content_length
content_md5
content_type
cookies
data
date
endpoint
files
form
full_path
headers
host
host_url
if_match
if_modified_since
if_none_match
if_range
if_unmodified_since
is_json
is_multiprocess
is_multithread
is_run_once
is_secure
json
max_content_length
max_forwards
method
mimetype
mimetype_params
origin
""".strip().split()