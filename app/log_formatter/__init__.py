import logging

from flask import has_request_context, request


class RequestFormatter(logging.Formatter):
    """below code dose the same thing as logging"""
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
            record.method = request.method
            record.pathname = request.path
            record.ip = request.headers.get('X-Forwarded-For', request.remote_addr)
            record.host = request.host.split(':', 1)[0]

        else:
            record.url = None
            record.remote_addr = None

        return super().format(record)
