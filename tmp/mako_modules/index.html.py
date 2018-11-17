# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1542469021.2173896
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
        __M_writer('<!doctype html>\n\n<html lang="en">\n<head>\n  <meta charset="utf-8">\n\n  <title>The HTML5 Herald</title>\n  <meta name="description" content="The HTML5 Herald">\n  <meta name="author" content="SitePoint">\n\n  <link rel="stylesheet" href="css/styles.css?v=1.0">\n\n</head>\n\n<body>\n  <script src="js/scripts.js"></script>\n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "docs/index.html", "uri": "index.html", "source_encoding": "ascii", "line_map": {"16": 0, "21": 1, "27": 21}}
__M_END_METADATA
"""
