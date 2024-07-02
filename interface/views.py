from flask import Blueprint, request


# log
log_view = Blueprint('log_view', __name__)

@log_view.route('/api/v1/log')
def log():
    if request.method == 'POST':
        return 'post'
    elif request.method == 'GET':
        return 'get'
    elif request.method == 'PATCH':
        return 'patch'
    elif request.method == 'DELETE':
        return 'delete'
    else:
        return 'request method not accepted'
