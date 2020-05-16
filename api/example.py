from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Introduction(Resource):
    def get(self):
        return {'Hi': 'Hello World!'}

    def post(self):
        json_request_send = request.get_json()
        return {'JSON sent': json_request_send}


class Add(Resource):
    def get(self, number):
        return {'result': number + 2}


api.add_resource(Introduction, '/')
api.add_resource(Add, '/add/<int:number>')

if __name__ == "__main__":
    app.run(debug=True)
