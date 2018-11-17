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
accounts.load('accounts.db')

# we don't save or load this database but we can if we want to
sessions = Database()

def get_ID():
    return str(uuid4())

@app.get('/')
@app.get('/index')
def index():
    redirect('/home')


@app.get('/home')
def home():
    return serve_template('index.html')


@app.get('/login')
def login():
    if get_username():
        return serve_template('login.html', logged_in=True)
    return serve_template('login.html')


@app.get('/signup')
def signup():
    if get_username():
        return serve_template('signup.html', logged_in=True)
    return serve_template('signup.html')

@app.get('/view')
def view():
    user = get_username()
    if user:
        rem = request.GET.remove
        if rem:
            items = accounts.data[user]['items']
            for item in items:
                if item['name'] == rem:
                    items.remove(item)
                    break
        items = accounts.data[user]['items']
        return serve_template('view.html', items=items)
    print('this guy tryna view his stuff without loggin in get outta here')
    return serve_template('view.html', logged_in=False)


@app.post('/login')
def loginPOST():
    logindats = {
        'username': request.POST.username,
        'password': request.POST.password
    }
    print(logindats, 'logging in')
    try:
        print('trying to login somebody:', logindats['username'])
        print('heres a list of accounts', accounts.data)
        print('is it in there?', logindats['username'] in accounts.data)

        # if this failes not found
        user_data = accounts.data[logindats['username']]

        print('ok username is good lets check their password')
        
        # if this failes bad password
        if (check(logindats['password'], user_data['salt'], user_data['hashed'])):
            print('ok password good let em in')
            set_login_cookie(logindats['username'])
            redirect('/view')
        else:
            print('some bitch entered a bad password')
            return serve_template('login.html', bad_pw=True)
    except KeyError:
        print('ok their username doesn\' exist abort abort')
        return serve_template('login.html', not_found=True)


@app.post('/signup')
def signupPOST():
    salt = gen_salt()
    username = request.POST.username
    data = {
        'username': username,
        'hashed': hashpass(request.POST.password, salt),
        'salt': salt,
        'items': []
    }
    print(username + ' just signed up')
    accounts.data[username] = data
    accounts.save('accounts.db')


    print('setting their cookie')
    set_login_cookie(username)

    return serve_template('signup.html', success=True)


@app.post('/view')
def viewPOST():
    user = get_username()
    if user:
        name = request.POST.name
        if name:
            quantity = request.POST.quantity
            items = accounts.data[user]['items']
            items.append({
                'name': name,
                'quantity': quantity
            })
            accounts.save('accounts.db')
            return serve_template('view.html', success=True, items=items)
    else:
        print('no id not adding item')
        return serve_template('view.html', success=False)
    


@app.get('/static/<filepath:path>')
def docs(filepath):
    return static_file(filepath, root=STATIC)

def set_login_cookie(username):
    sid = get_ID()
    sessions.data[sid] = {'logged_in': True, 'username': username}
    response.set_cookie('id', sid)

def get_username():
    try:
        user = sessions.data[request.get_cookie('id')]['username']
        print('getting username', user)
        print('sessions', sessions.data)
        print('id', request.get_cookie('id'))
        print('username', user)
        return user
    except KeyError:
        return None

def serve_template(name, **kwargs):
    return lookup.get_template(name).render(**kwargs)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)