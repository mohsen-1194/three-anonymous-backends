import json

from a2wsgi import ASGIMiddleware
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from waitress import serve

app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)


@app.exception_handler(404)
async def not_found(request: Request, exc):
    data = json.dumps({"error": "Not Found"}, separators=(",", ":"))
    return Response(content=data, media_type="application/json", status_code=404)


@app.exception_handler(500)
async def server_error(request: Request, exc):
    data = json.dumps({"error": "Internal Server Error"}, separators=(",", ":"))
    return Response(content=data, media_type="application/json", status_code=500)


ALLOWED_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "HEAD",
    "OPTIONS",
    "TRACE",
    "CONNECT",
]


class ForceCapsStatusMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        def custom_start_response(status, headers, exc_info=None):
            # Split status into code + reason
            code, reason = status.split(" ", 1)
            # Force reason phrase to all caps
            status = f"{code} {reason.upper()}"
            return start_response(status, headers, exc_info)

        return self.app(environ, custom_start_response)


@app.api_route("/", methods=ALLOWED_METHODS)
def home():
    data = json.dumps({"body": "hello"}, separators=(",", ":"))
    return Response(
        content=data,
        media_type="application/json",
    )


# @app.get("/boom")
# @app.get("/boom/")
# def boom():
#     raise Exception("Something broke!")


# Global 405 handler
@app.exception_handler(405)
async def custom_405_handler(request: Request, exc):
    data = json.dumps({"error": "Method not allowed"}, separators=(",", ":"))
    return Response(content=data, media_type="application/json", status_code=405)


# Wrap the ASGI app to make it WSGI-compatible
wsgi_app = ASGIMiddleware(app)

if __name__ == "__main__":
    wsgi_app = ForceCapsStatusMiddleware(wsgi_app)
    serve(wsgi_app, host="0.0.0.0", port=8002, ident="Unknown")
