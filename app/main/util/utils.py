from datetime import datetime, timedelta


class ApiResponse:
    @staticmethod
    def success(message):
        response_object = {
            'status': 1,
            'message': message
        }
        return response_object, 200

    @staticmethod
    def created(message):
        response_object = {
            'status': 1,
            'message': message
        }
        return response_object, 201

    @staticmethod
    def error(message, status_code):
        response_object = {
            'status': 0,
            'message': message
        }
        return response_object, status_code

    @staticmethod
    def custom(message, data, status_code):
        response = {
            'data': data,
        }
        response_object = {
            'status': 1,
            'message': message,
            'asset_id': response
        }
        return response_object, status_code

    @staticmethod
    def detail(message, data, status_code):
        response = {
            'data': data,
        }
        response_object = {
            'status': 1,
            'message': message,
            'data': response
        }
        return response_object, status_code

    @staticmethod
    def value(message, data, status_code):
        response_object = {
            'status': 1,
            'message': message,
            'data': data
        }
        return response_object, status_code

    @staticmethod
    def update(message, status_code):
        response_object = {
            'status': 1,
            'message': message,
        }
        return response_object, status_code

    @staticmethod
    def login(message, data, status_code):
        response_object = {
            'status': 1,
            'message': message,
            'Authorization': data
        }
        return response_object, status_code


def serialize_datetime(dt):
    if isinstance(dt, datetime):
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    return dt