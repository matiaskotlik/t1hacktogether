from bottle import static_file, redirect, default_app, request, response
from mako.lookup import TemplateLookup
import os

ROOT = '/home/matias/data/programming/git/t1hacktogether'
STATIC = os.path.join(ROOT, 'static')
print(STATIC)
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


@app.get('/static/<filepath:path>')
def docs(filepath):
    print(filepath)
    return static_file(filepath, root=STATIC)


def serve_template(name, **kwargs):
    return lookup.get_template(name).render(**kwargs)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)