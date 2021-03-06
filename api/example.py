from api.base import BaseApi


class Introduction(BaseApi):
    def get(self):
        return {'Hi': 'Hello World!'}

    def post(self):
        json_request_send = self.my_request.get_json()
        return {'JSON sent': json_request_send}


class Add:
    def get(self, number):
        return {'result': number + 2}
