from flask import request


class BaseController:
    my_request: request

    def __init__(self, request_received):
        self.my_request = request_received
