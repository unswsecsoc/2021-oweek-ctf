from app import app
from flask import render_template, request, make_response, redirect

LAST_NAME = 'clemington'
ID_NUM = '6750754009180'
COOKIE = 'PYFcbQOlB6mQ3a$6B82'

@app.route('/', methods=['POST', 'GET'])
def admin():
    if request.method == 'GET':
        if request.cookies.get('auth') == COOKIE:
            return render_template('dash.html')
        else:
            return render_template('login.html', message='')
    else:
        if request.form['name'].lower() == LAST_NAME and request.form['id'] == ID_NUM:
            resp = make_response(redirect('/'))
            resp.set_cookie('auth', COOKIE)
            return resp
        else:
            return render_template('login.html', message='Incorrect name and/or student ID.')
    
@app.route('/favicon.ico')
def favicon():
    return ''
