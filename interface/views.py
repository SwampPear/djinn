from flask import Blueprint, request

# project
project_view = Blueprint('project_view', __name__)

@project_view.route('/api/v1/project')
def project():
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
    

# sprint
sprint_view = Blueprint('sprint_view', __name__)

@sprint_view.route('/api/v1/sprint')
def sprint():
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
    

# iteration
iteration_view = Blueprint('iteration_view', __name__)

@sprint_view.route('/api/v1/iteration')
def iteration():
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
