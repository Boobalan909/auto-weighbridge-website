from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('web', __name__)

@bp.route('/')
def login():
    return render_template('login.html')