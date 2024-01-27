from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint('web', __name__)

@bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        entered_username = request.form.get('username')
        entered_password = request.form.get('password')
        
        if entered_username == 'admin' and entered_password == 'password':
            return redirect(url_for('web.base'))
        else:
            error = 'Invalid username or password'
            return render_template('login.html', error=error)
    return render_template('login.html')


@bp.route('/base')
def base():
    return render_template('base.html')