# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523552737.1957424
_enable_loop = True
_template_filename = 'C:/Users/Linds/desktop/intex2_fomo/manager/templates/products.html'
_template_uri = 'products.html'
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
        productList = context.get('productList', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        productList = context.get('productList', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n   <div class="content">\r\n    <h1 class=\'cen\'>Products</h1>\r\n    <a href="/manager/create/" class="btn btn-primary btn-md active rightside" role="button" aria-pressed="true">Create Product</a>\r\n     <table class="table">\r\n         <thead>\r\n           <tr>\r\n             <th>Category</th>\r\n             <th>Product Type</th>\r\n             <th>Name</th>\r\n             <th>Price</th>\r\n             <th>Quantity</th>\r\n             <th></th>\r\n             <th></th>\r\n           </tr>\r\n         </thead>\r\n         <tbody>\r\n')
        for p in productList:
            __M_writer('           <tr>\r\n             <td>')
            __M_writer(str(p.category))
            __M_writer('</td>\r\n             <td>')
            __M_writer(str(p.TITLE))
            __M_writer('</td>\r\n             <td>')
            __M_writer(str(p.name))
            __M_writer('</td>\r\n             <td>')
            __M_writer(str(p.price))
            __M_writer('</td>\r\n             <td>\r\n')
            if hasattr(p, 'quantity'):
                __M_writer('                 ')
                __M_writer(str(p.quantity))
                __M_writer('\r\n')
            else:
                __M_writer('                 1\r\n')
            __M_writer('             </td>\r\n             <td>\r\n               <a href="/manager/edit/')
            __M_writer(str(p.id))
            __M_writer('" class="btn btn-danger btn-md active" role="button" aria-pressed="true">Edit</a>\r\n             </td>\r\n             <td>\r\n               <a href="/manager/delete/')
            __M_writer(str(p.id))
            __M_writer('" class="btn btn-info btn-md active" role="button" aria-pressed="true">Delete</a>\r\n             </td>\r\n           </tr>\r\n')
        __M_writer('         </tbody>\r\n     </table>\r\n     <br>\r\n </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Linds/desktop/intex2_fomo/manager/templates/products.html", "uri": "products.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 45, "49": 3, "57": 3, "58": 20, "59": 21, "60": 22, "61": 22, "62": 23, "63": 23, "64": 24, "65": 24, "66": 25, "67": 25, "68": 27, "69": 28, "70": 28, "71": 28, "72": 29, "73": 30, "74": 32, "75": 34, "76": 34, "77": 37, "78": 37, "79": 41, "85": 79}}
__M_END_METADATA
"""
