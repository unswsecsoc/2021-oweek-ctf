from app import app
from flask import render_template, request, make_response, redirect

USERNAME = 'employee'
PASSWORD = 'biscuit123'

@app.route('/', methods=['POST', 'GET'])
def admin():
    if request.method == 'GET':
        if request.cookies.get('username') == 'admin':
            return render_template('dash.html', message='OWEEK{b1scUit5_moR3_L1k3_C00KIE!!_0MN0MN0M}')
        elif request.cookies.get('username') == USERNAME:
            return render_template('dash.html', message='Welcome! There are no messages for you.')
        else:
            return render_template('login.html', message='')
    else:
        if request.form['username'] == USERNAME and request.form['password'] == PASSWORD:
            resp = make_response(redirect('/'))
            resp.set_cookie('username', USERNAME)
            return resp
        else:
            return render_template('login.html', message='Incorrect username or password.')
    
@app.route('/favicon.ico')
def favicon():
    return ''
