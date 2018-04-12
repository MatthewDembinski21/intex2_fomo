# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1522783728.7119834
_enable_loop = True
_template_filename = 'C:/Users/mayaroney/desktop/fomo/catalog/templates/cart.html'
_template_uri = '/catalog/templates/cart.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['top_center', 'content_center']


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
        items = context.get('items', UNDEFINED)
        def top_center():
            return render_top_center(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_center'):
            context['self'].top_center(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_center():
            return render_top_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n<h2>Shopping Cart</h2>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        items = context.get('items', UNDEFINED)
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="container">\r\n\r\n    <table class="table">\r\n        <thead>\r\n        <tr>\r\n            <th>Name</th>\r\n            <th>Quantity</th>\r\n            <th>Price</th>\r\n            <th>Extended</th>\r\n\r\n        </tr>\r\n        </thead>\r\n        <tbody>\r\n')
        for c in items:
            __M_writer('        <tr>\r\n            <td>\r\n                ')
            __M_writer(str(c.product.name))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(str(c.quantity))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(str(c.price))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(str(c.extended))
            __M_writer('\r\n            </td>\r\n            <td>\r\n               <a href="/catalog/deleteitem/')
            __M_writer(str(c.product.id))
            __M_writer('/" >Delete</a>\r\n            </td>\r\n        </tr>\r\n')
        __M_writer('\r\n        </tbody>\r\n    </table>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/mayaroney/desktop/fomo/catalog/templates/cart.html", "uri": "/catalog/templates/cart.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "44": 6, "49": 47, "55": 4, "61": 4, "67": 9, "74": 9, "75": 24, "76": 25, "77": 27, "78": 27, "79": 30, "80": 30, "81": 33, "82": 33, "83": 36, "84": 36, "85": 39, "86": 39, "87": 43, "93": 87}}
__M_END_METADATA
"""
