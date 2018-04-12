# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519240025.6540954
_enable_loop = True
_template_filename = 'C:/Users/mayaroney/desktop/fomo/manager/templates/app_base.html'
_template_uri = 'app_base.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['menu', 'nav_main']


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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def nav_main():
            return render_nav_main(context._locals(__M_locals))
        def menu():
            return render_menu(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav_main'):
            context['self'].nav_main(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu():
            return render_menu(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_nav_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def nav_main():
            return render_nav_main(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n       <li class="')
        __M_writer(str( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('"><a href="/">Home</a></li>\r\n       <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'about' else '' ))
        __M_writer('"><a href="/about">About Us</a></li>\r\n       <li class=" ')
        __M_writer(str('active' if request.dmp.page == 'faq' else '' ))
        __M_writer('"><a href="/faq">FAQ</a></li>\r\n       <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'contact' else '' ))
        __M_writer('"><a href="/contact">Contact</a></li>\r\n       <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'terms' else '' ))
        __M_writer('"><a href="/terms">Terms</a></li>\r\n       <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'product' else '' ))
        __M_writer('"><a href="/manager/products/">Product</a></li>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/mayaroney/desktop/fomo/manager/templates/app_base.html", "uri": "app_base.html", "source_encoding": "utf-8", "line_map": {"28": 0, "38": 1, "43": 6, "48": 17, "54": 4, "60": 4, "66": 9, "73": 9, "74": 11, "75": 11, "76": 12, "77": 12, "78": 13, "79": 13, "80": 14, "81": 14, "82": 15, "83": 15, "84": 16, "85": 16, "91": 85}}
__M_END_METADATA
"""
