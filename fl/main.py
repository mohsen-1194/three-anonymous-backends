from flask import Flask, Response, request, jsonify
from werkzeug.serving import WSGIRequestHandler, run_simple
import json

app = Flask(__name__)
app.debug = False

@app.errorhandler(404)
def not_found(e):
    data = json.dumps({"error": "Not Found"}, separators=(",", ":"))
    return Response(data, content_type="application/json", status=404)

@app.errorhandler(500)
def server_error(e):
    data = json.dumps({"error": "Internal Server Error"}, separators=(",", ":"))
    return Response(data, content_type="application/json", status=500)

ALLOWED_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'HEAD', 'OPTIONS',
    'TRACE', 'CONNECT']

@app.route("/", methods=ALLOWED_METHODS)
def home():
    data = json.dumps({"body": "hello"}, separators=(",", ":"))
    return Response(data, content_type="application/json",)
   

# @app.route("/boom")
# @app.route("/boom/")
# def boom():
#     raise Exception("Something broke!")  # forces 500




# Optional: catch unknown methods globally
@app.errorhandler(405)
def method_not_allowed(e):
    data = json.dumps({"error": "Method not allowed"}, separators=(",", ":"))
    return Response(data, content_type="application/json", status=405)
