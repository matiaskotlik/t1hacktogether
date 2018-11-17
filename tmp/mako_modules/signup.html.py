# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1542487865.6460552
_enable_loop = True
_template_filename = 'docs/signup.html'
_template_uri = 'signup.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,success=False,logged_in=False,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,logged_in=logged_in,success=success)
        __M_writer = context.writer()
        __M_writer('\n\n<!doctype html>\n\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n\n  <title>Sign Up</title>\n  <meta name="description" content="Signup">\n  <meta name="author" content="Team 1">\n\n  <link rel="stylesheet" href="/static/css/styles.css">\n  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css">\n\n</head>\n\n<body>\n  <h1>Sign Up</h1>\n')
        if success:
            __M_writer('    <p>You have successfully signed in</p>\n    <p>Click <a href="/view">here</a> to check your inventory</p>\n')
        if logged_in:
            __M_writer('    <p>You are already signed in</p>\n')
        else:
            __M_writer('    <form target="_self" method="POST" action="/signup">\n      <div id="signup">\n        <input type="text" name="username" placeholder="Username"><br><br>\n        <input type="password" name="password" placeholder="Password"><br><br>\n        <input type="submit" value="Submit" class="btn btn-success">\n      </div>\n    </form>\n')
        __M_writer('  <a href="/home"><input type="button" value="Back To Home" class = "btn btn-primary"></a>\n\n  <script src="/static/js/scripts.js"></script>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "docs/signup.html", "uri": "signup.html", "source_encoding": "ascii", "line_map": {"16": 1, "21": 1, "22": 20, "23": 21, "24": 24, "25": 25, "26": 26, "27": 27, "28": 35, "34": 28}}
__M_END_METADATA
"""
