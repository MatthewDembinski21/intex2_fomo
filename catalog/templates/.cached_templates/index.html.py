# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1521142647.7937262
_enable_loop = True
_template_filename = 'C:/Users/mayaroney/desktop/fomo/catalog/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['content_center']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        name = context.get('name', UNDEFINED)
        myPages = context.get('myPages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        name = context.get('name', UNDEFINED)
        myPages = context.get('myPages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <h1 class="title">')
        __M_writer(str( name ))
        __M_writer('</h1>\r\n\r\n    <div id="paginator">\r\n        <a id= "pLeft"><<< </a>Page <span id="Page">1</span> of <span id="total">')
        __M_writer(str(myPages))
        __M_writer('</span><a id="pRight"> >>></a>\r\n    </div>\r\n\r\n    <div id="ajax_container">\r\n\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/mayaroney/desktop/fomo/catalog/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 20, "49": 9, "57": 9, "58": 11, "59": 11, "60": 14, "61": 14, "67": 61}}
__M_END_METADATA
"""
