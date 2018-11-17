# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1542485516.5402818
_enable_loop = True
_template_filename = 'docs/signup.html'
_template_uri = 'signup.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,success=False,logged_in=False,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,success=success,logged_in=logged_in)
        __M_writer = context.writer()
        __M_writer('\n\n<!doctype html>\n\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n\n  <title>Sign Up</title>\n  <meta name="description" content="Signup">\n  <meta name="author" content="Team 1">\n\n  <link rel="stylesheet" href="/static/css/styles.css">\n\n</head>\n\n<body>\n  <h1>Sign Up</h1>\n')
        if success:
            __M_writer('    <p>You have successfully signed in</p>\n    <p>Click <a href="/view">here</a> to check your inventory</p>\n')
        if logged_in:
            __M_writer('    <p>You are already signed in</p>\n')
        else:
            __M_writer('    <form target="_self" method="POST" action="/signup">\n      <div id="signup">\n        <label for="username">Username: </label>\n        <input type="text" name="username"><br>\n        <label for="password">Password: </label>\n        <input type="password" name="password"><br>\n        <input type="submit" value="Submit">\n      </div>\n    </form>\n')
        __M_writer('  <a href="/home"><input type="button" value="Back To Home"></a>\n\n  <script src="/static/js/scripts.js"></script>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "docs/signup.html", "uri": "signup.html", "source_encoding": "ascii", "line_map": {"16": 1, "21": 1, "22": 19, "23": 20, "24": 23, "25": 24, "26": 25, "27": 26, "28": 36, "34": 28}}
__M_END_METADATA
"""
