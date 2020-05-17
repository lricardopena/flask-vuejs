from controllers.base import BaseController


class Introduction(BaseController):
    def get(self):
        return {'Hi': 'Hello World!'}

    def post(self):
        json_request_send = self.my_request.get_json()
        return {'JSON sent': json_request_send}


class Add(BaseController):
    def get(self, number):
        number = int(number)
        return {'result': number + 2}
