from app import app
from flask import render_template, request, make_response, redirect, send_from_directory

USERNAME = 'skynet'
PASSWORD = 'b33pb00pWeRu1EtHeW0rLD8392389'

@app.route('/', methods=['POST', 'GET'])
def admin():
    if request.method == 'GET':
        if request.cookies.get('username') == USERNAME:
            return render_template('dash.html', message='OWEEK{w3_w0Nt_t4kE_0v3r_tH3_wOrLd_p1nKY_pR0MisE}')
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

@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, request.path[1:])
