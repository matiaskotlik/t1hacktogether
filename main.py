from bottle import static_file, redirect, default_app, request, response
from mako.lookup import TemplateLookup
import os

ROOT = '/home/matias/data/programming/git/t1hacktogether'
STATIC = os.path.join(ROOT, 'static')
STATIC = ROOT
DEBUG = True
if DEBUG:
    PORT = 8080
else:
    PORT = 80

app = default_app()

lookup = TemplateLookup(directories=['./docs'],
                        module_directory='./tmp/mako_modules')

@app.get('/')
@app.get('/index')
def index():
    redirect('/home')


@app.get('/home')
def home():
    serve_template('index.html')


@app.get('/docs/<filepath:path>')
def docs():
    return static_file()


def serve_template(name, **kwargs):
    return lookup.get_template(name).render(**kwargs)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)