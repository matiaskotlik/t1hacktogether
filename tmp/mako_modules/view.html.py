# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1542486271.4206295
_enable_loop = True
_template_filename = 'docs/view.html'
_template_uri = 'view.html'
_source_encoding = 'ascii'
_exports = []


def render_body(context,logged_in=True,success=False,items={},**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs,success=success,logged_in=logged_in,items=items)
        __M_writer = context.writer()
        __M_writer('\n\n<!doctype html>\n\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n\n  <title>View</title>\n  <meta name="description" content="View">\n  <meta name="author" content="Team 1">\n\n  <link rel="stylesheet" href="/static/css/styles.css">\n\n</head>\n\n<body>\n  <h1>Inventory</h1>\n')
        if success:
            __M_writer('    <p>Added item.</p>\n')
        if logged_in:
            __M_writer('    <form method="POST" action="/view">\n      <label for="name">Name: </label>\n      <input type="text" name="name"><br>\n      <label for="quantity">Quantity: </label>\n      <input type="text" name="quantity"><br>\n      <input type="submit" value="Add Item">\n    </form>\n')
            for item in items:
                __M_writer('      <div class="item">\n        <p>')
                __M_writer(str(item['name']))
                __M_writer('</p>\n        <p>')
                __M_writer(str(item['quantity']))
                __M_writer('</p>\n        <a href="?remove=')
                __M_writer(str(item['name']))
                __M_writer('">Remove Item</a>\n      </div>\n')
        else:
            __M_writer('    <p>You are not logged in. Click <a href="/login">here</a> to login.</p>\n')
        __M_writer('  <a href="/home"><input type="button" value="Back To Home"></a>\n\n  <script src="/static/js/scripts.js"></script>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "docs/view.html", "uri": "view.html", "source_encoding": "ascii", "line_map": {"16": 1, "21": 1, "22": 19, "23": 20, "24": 22, "25": 23, "26": 30, "27": 31, "28": 32, "29": 32, "30": 33, "31": 33, "32": 34, "33": 34, "34": 37, "35": 38, "36": 40, "42": 36}}
__M_END_METADATA
"""
