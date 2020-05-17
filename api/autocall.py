from flask import jsonify
from api.base import BaseApi


class Hello(BaseApi):
    def post(self):
        return jsonify({
            "Sended": self.my_request.get_json()
        })

    def get(self, name):
        return jsonify({
            "Name": name
        })
