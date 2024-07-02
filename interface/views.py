from flask import render_template, Blueprint


log_view = Blueprint('log_view', __name__)

@log_view.route('/api/v1/log')
def log():
    return {'apple': 3}