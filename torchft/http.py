import socket
from http.server import ThreadingHTTPServer


class _IPv6HTTPServer(ThreadingHTTPServer):
    address_family = socket.AF_INET6
    request_queue_size = 1024