# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1542493741.3446052
_enable_loop = True
_template_filename = 'docs/index.html'
_template_uri = 'index.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('<!doctype html>\n\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n\n  <title>Home</title>\n  <meta name="description" content="Home">\n  <meta name="author" content="Team 1">\n\n  <link rel="stylesheet" href="/static/css/styles.css">\n  <link rel="stylesheet" href="/static/css/bootstrap.min.css">\n</head>\n\n<body>\n  <div class="container">\n  <h1>Home</h1>\n  <p><a href="/view"><input type="button" value="View Inventory" class="btn btn-secondary"></a><p>\n  <p><a href="/login"><input type="button" value="Login" class="btn btn-primary"></a></p>\n  <p><a href="/logout"><input type="button" value="Logout" class="btn btn-danger" /></a></p>\n  <img src="/static/img/img.jpg" alt="East Asia Place Logo">\n  </div>\n  <script src="/static/js/scripts.js"></script>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "docs/index.html", "uri": "index.html", "source_encoding": "ascii", "line_map": {"16": 0, "21": 1, "27": 21}}
__M_END_METADATA
"""
