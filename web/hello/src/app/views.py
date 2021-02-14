from flask import request, render_template, send_from_directory
from app import app

@app.route('/', methods=['GET', 'POST'])
def verified():
    user = {'name':None, 'admin':None}

    if request.method == 'GET': 
        user['name'] = request.args.get('name')
        user['admin'] = request.args.get('admin')

    if user['name'] == None and user['admin'] == None:
        return render_template('index.html')

    if user['name'] != 'Alex':
        return f'''
        <h1>Hello {user['name']}!</h1>
        <form action="/">
            <input type="submit" value="Back" />
        </form>
        '''
    
    if user['admin'] != 'true':
        return '''
        <h2>You must be an admin<h2>
        '''

    return 'OWEEK{CHanG1ng_pARam5_15_Fun}'

@app.route('/robots.txt')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])
