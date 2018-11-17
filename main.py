from bottle import static_file, redirect, default_app, request, response
from mako.lookup import TemplateLookup
import os
from database import Database
from crypt import *
from uuid import uuid4

ROOT = '/home/matias/data/programming/git/t1hacktogether'
STATIC = os.path.join(ROOT, 'static')
DEBUG = True
if DEBUG:
    PORT = 8080
else:
    PORT = 80

app = default_app()

lookup = TemplateLookup(directories=['./docs'],
                        module_directory='./tmp/mako_modules')

accounts = Database()
accounts.load()

# we don't save or load this database but we can if we want to
sessions = Database()

def get_ID():
    return uuid4()

@app.get('/')
@app.get('/index')
def index():
    redirect('/home')


@app.get('/home')
def home():
    return serve_template('index.html')


@app.get('/login')
def login():
    return serve_template('login.html')


@app.get('/signup')
def signup():
    return serve_template('signup.html')

@app.get('/view')
def view():
    sid = request.get_cookie('id')
    if (sid):
        username = sessions[sid]['username']
        items = accounts[username]['items']
        return serve_template('view.html', items=items)
    else:
        return serve_template('view.html', logged_in=False)


def loginPOST():
    data = {
        'username': request.POST.username,
        'password': request.POST.password
    }
    try:
        # if this failes not found
        user_data = accounts.data[data['username']]
        
        # if this failes bad password
        if (check(data['password'], user_data['salt'], user_data['hashed'])):
            sid = get_ID()
            sessions[sid] = {'logged_in': True, 'username': data['username']}
            response.set_cookie('id', sid)
        else:
            serve_template('login.html', bad_pw=True)
    except:
        serve_template('login.html', not_found=True)


@app.post('/signup')
def signupPOST():
    salt = gen_salt()
    username = request.POST.username
    data = {
        'username': username
        'hashed': hashpw(request.POST.password, salt)
        'salt': salt,
        'items': {}
    }
    accounts[username] = data
    return serve_template('signup.html', success=True)


@app.post('/view')
def viewPOST():
    sid = request.get_cookie('id')
    if (sid):
        name = request.POST.name
        quantity = request.POST.quantity
        username = sessions[sid]['username']
        items = accounts[username]['items']
        items['name'] = name
        items['quantity'] = quantity
    redirect('/view')


@app.get('/static/<filepath:path>')
def docs(filepath):
    print(STATIC, filepath)
    return static_file(filepath, root=STATIC)


def serve_template(name, **kwargs):
    return lookup.get_template(name).render(**kwargs)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)