from flask import Blueprint, request

bp = Blueprint('user', __name__)

@bp.route('/user/')
def user():
    return "Hello, User!"