#!/usr/bin/python3
'''Http server'''

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    '''Class BaseHTTPRequestHandler'''

    def do_GET(self):
        '''do get'''
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes("Hello, this is a simple API!", "utf-8"))
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(bytes(json.dumps(data), "utf-8"))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes("OK", "utf-8"))
        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self.wfile.write(bytes(json.dumps(info), "utf-8"))
        else:
            self.send_error(404, "Endpoint not found")


def run():
    print('Starting server...')
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Server is running...')
    httpd.serve_forever()


run()
