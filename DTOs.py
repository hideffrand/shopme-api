# response_template.py

class ResponseTemplate:
    def __init__(self, status_code, message, data=None):
        self.status_code = status_code
        self.message = message
        self.data = data

    def to_dict(self):
        response_dict = {
            'status_code': self.status_code,
            'message': self.message
        }

        if self.data is not None:
            response_dict['data'] = self.data

        return response_dict
