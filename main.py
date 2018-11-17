from bottle import static_file, redirect, default_app, request, response
from mako.lookup import TemplateLookup
import os
from database import Database

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

@app.get('/')
@app.get('/index')
def index():
    redirect('/home')


@app.get('/home')
def home():
    serve_template('index.html')


@app.get('/login')
def login():
    serve_template('login.html')


@app.get('/signup')
def signup():
    serve_template('signup.html')

@app.get('/view')
def view():
    serve_template('view.html')


def loginPOST():
    data = {
        'username': request.POST.username,
        'password': request.POST.password
    }


@app.post('/signup')
def signupPOST():
    data = {
        'username': request.POST.username,
        'password': request.POST.password
    }
    # todo add to database here


@app.get('/static/<filepath:path>')
def docs(filepath):
    print(STATIC, filepath)
    return static_file(filepath, root=STATIC)


def serve_template(name, **kwargs):
    return lookup.get_template(name).render(**kwargs)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)