# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1542493234.2344928
_enable_loop = True
_template_filename = 'docs/login.html'
_template_uri = 'login.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,bad_pw=False,not_found=False,logged_in=False,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(logged_in=logged_in,bad_pw=bad_pw,not_found=not_found,pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n\n<!doctype html>\n\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n\n  <title>Login</title>\n  <meta name="description" content="Login">\n  <meta name="author" content="Team 1">\n\n  <link rel="stylesheet" href="/static/css/styles.css">\n  <link rel="stylesheet" href="/static/css/bootstrap.min.css">\n</head>\n\n<body>\n  <div class="container">\n  <h1>Login</h1>\n')
        if bad_pw:
            __M_writer('    <p>Bad password</p>\n')
        if not_found:
            __M_writer('    <p>Username not found</p>\n')
        if logged_in:
            __M_writer('    <p>You are already logged in</p>\n')
        else:
            __M_writer('    <form action="/login" method="POST">\n      <div id="login">\n        <input type="text" name="username" placeholder="Username"><br><br>\n        <input type="password" name="password" placeholder="Password"><br><br>\n        <input type="submit" value="Submit" class="btn btn-success">\n      </div>\n    </form>\n    <p>Don\'t have an account? <a href="signup"><input type="button" value="Sign Up" class="btn btn-secondary"></a></p>\n')
        __M_writer('  <p><a href="/home"><input type="button" value="Back To Home" class="btn btn-primary"></a></p>\n  </div>\n  <script src="/static/js/scripts.js"></script>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "docs/login.html", "uri": "login.html", "source_encoding": "ascii", "line_map": {"16": 1, "21": 1, "22": 20, "23": 21, "24": 23, "25": 24, "26": 26, "27": 27, "28": 28, "29": 29, "30": 38, "36": 30}}
__M_END_METADATA
"""
