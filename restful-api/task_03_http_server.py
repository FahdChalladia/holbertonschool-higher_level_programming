#!/usr/bin/python3
"""
Simple API using http.server
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _set_headers(self, status_code=200, content_type="text/plain"):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == "/":
            self._set_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self._set_headers(content_type="application/json")
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            # Return plain text "OK", not JSON
            self._set_headers(content_type="text/plain")
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self._set_headers(content_type="application/json")
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            # Return plain text "Endpoint not found"
            self._set_headers(404, content_type="text/plain")
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
