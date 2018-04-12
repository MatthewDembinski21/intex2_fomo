# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519321818.2136323
_enable_loop = True
_template_filename = 'C:/Users/mayaroney/desktop/fomo/catalog/templates/product.html'
_template_uri = '/catalog/templates/product.html'
_source_encoding = 'utf-8'
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
        def content_center():
            return render_content_center(context._locals(__M_locals))
        productList = context.get('productList', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        def top_center():
            return render_top_center(context._locals(__M_locals))
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
        __M_writer('\r\n<h2>Product List</h2>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        productList = context.get('productList', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n<div class="container">\r\n\r\n    <table class="table">\r\n        <thead>\r\n        <tr>\r\n            <th>Category</th>\r\n            <th>Type</th>\r\n            <th>Name</th>\r\n            <th>Price</th>\r\n            <th>Quantity</th>\r\n            <th>Actions</th>\r\n        </tr>\r\n        </thead>\r\n        <tbody>\r\n')
        for p in productList:
            __M_writer('        <tr>\r\n            <td>\r\n                ')
            __M_writer(str(p.category.name))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(str(p.__class__.__name__))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(str(p.name))
            __M_writer('\r\n            </td>\r\n            <td>\r\n                ')
            __M_writer(str(p.price))
            __M_writer('\r\n            </td>\r\n            <td>\r\n')
            if hasattr(p, 'quantity'):
                __M_writer('                ')
                __M_writer(str(p.quantity))
                __M_writer('\r\n')
            else:
                __M_writer('                    1\r\n')
            __M_writer('            </td>\r\n            <td>\r\n                <a href="/manager/edit/')
            __M_writer(str(p.id))
            __M_writer('/" >Edit </a> | <a href="/manager/delete/')
            __M_writer(str(p.id))
            __M_writer('/" >Delete</a>\r\n            </td>\r\n        </tr>\r\n')
        __M_writer('\r\n        </tbody>\r\n    </table>\r\n</div>\r\n\r\n<div class="text-center">\r\n    <a href="/manager/create/" class="btn btn-info" role="button">Create Product</a>\r\n\r\n</div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/mayaroney/desktop/fomo/catalog/templates/product.html", "uri": "/catalog/templates/product.html", "source_encoding": "utf-8", "line_map": {"28": 0, "39": 1, "44": 6, "49": 63, "55": 4, "61": 4, "67": 9, "75": 9, "76": 26, "77": 27, "78": 29, "79": 29, "80": 32, "81": 32, "82": 35, "83": 35, "84": 38, "85": 38, "86": 41, "87": 42, "88": 42, "89": 42, "90": 43, "91": 44, "92": 46, "93": 48, "94": 48, "95": 48, "96": 48, "97": 52, "103": 97}}
__M_END_METADATA
"""
