# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523549969.3490257
_enable_loop = True
_template_filename = 'C:/Users/Linds/desktop/intex2_fomo/catalog/templates/index.products.html'
_template_uri = 'index.products.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['content']


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
    return runtime._inherit_from(context, 'base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <ul>\r\n')
        for p in products:
            __M_writer('        <a href="/catalog/details/')
            __M_writer(str(p.id))
            __M_writer('/">\r\n          <li class="product_tile">\r\n            <div class=\'prodpic cen\'><img class=\'catalog_pics\' src= \'')
            __M_writer(str(p.image_url()))
            __M_writer("' /></div>\r\n            <div class='monies'> $")
            __M_writer(str(p.price))
            __M_writer("</div>\r\n            <div class='prodname cen'>")
            __M_writer(str(p.name))
            __M_writer('</div>\r\n          </li>\r\n        </a>\r\n')
        __M_writer('    </ul>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Linds/desktop/intex2_fomo/catalog/templates/index.products.html", "uri": "index.products.html", "source_encoding": "utf-8", "line_map": {"29": 0, "37": 1, "42": 22, "48": 3, "55": 3, "56": 6, "57": 12, "58": 12, "59": 12, "60": 14, "61": 14, "62": 15, "63": 15, "64": 16, "65": 16, "66": 20, "72": 66}}
__M_END_METADATA
"""
