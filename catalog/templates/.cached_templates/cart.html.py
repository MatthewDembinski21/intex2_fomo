# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523321499.290129
_enable_loop = True
_template_filename = '/Users/matthewdembinski/Downloads/fomo/catalog/templates/cart.html'
_template_uri = 'cart.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['top_center', 'content_center']


from catalog import models as cmod

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
        def content_center():
            return render_content_center(context._locals(__M_locals))
        taxprice = context.get('taxprice', UNDEFINED)
        def top_center():
            return render_top_center(context._locals(__M_locals))
        total = context.get('total', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
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
        __M_writer('\r\n<h2 id="shopTitle">Shopping Cart</h2>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        items = context.get('items', UNDEFINED)
        def content_center():
            return render_content_center(context)
        total = context.get('total', UNDEFINED)
        taxprice = context.get('taxprice', UNDEFINED)
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
            __M_writer(str(c.id))
            __M_writer('" >Delete</a>\r\n            </td>\r\n        </tr>\r\n')
        __M_writer('\r\n        </tbody>\r\n    </table>\r\n\r\n    <div class="totals">\r\n        <br>\r\n        <h5>Sales Tax: ')
        __M_writer(str(taxprice))
        __M_writer('</h5>\r\n        <hr>\r\n        <h5><b>Total: ')
        __M_writer(str(total))
        __M_writer('</b> </h5>\r\n        <br>\r\n        <a class="butt" href="/catalog/checkout/" type="button" class="btn btn-link nav-item category_nav">Checkout</a>\r\n        <br><br>\r\n    </div>\r\n\r\n\r\n\r\n\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/matthewdembinski/Downloads/fomo/catalog/templates/cart.html", "uri": "cart.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "43": 1, "44": 2, "49": 6, "54": 61, "60": 4, "66": 4, "72": 9, "81": 9, "82": 24, "83": 25, "84": 27, "85": 27, "86": 30, "87": 30, "88": 33, "89": 33, "90": 36, "91": 36, "92": 39, "93": 39, "94": 43, "95": 49, "96": 49, "97": 51, "98": 51, "104": 98}}
__M_END_METADATA
"""
