# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1520386187.9715517
_enable_loop = True
_template_filename = 'C:/Users/mayaroney/desktop/fomo/homepage/templates/app_base.html'
_template_uri = 'app_base.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['menu', 'navitems']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def navitems():
            return render_navitems(context._locals(__M_locals))
        def menu():
            return render_menu(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'navitems'):
            context['self'].navitems(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
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


def render_navitems(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def navitems():
            return render_navitems(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <ul class="nav navbar-nav">\r\n       <li class="')
        __M_writer(str( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('"><a href="/">Home</a></li>\r\n        <li class="')
        __M_writer(str( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('"><a href="/">Catalog</a></li>\r\n       <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'about' else '' ))
        __M_writer('"><a href="/about">About Us</a></li>\r\n       <li class=" ')
        __M_writer(str('active' if request.dmp.page == 'faq' else '' ))
        __M_writer('"><a href="/faq">FAQ</a></li>\r\n       <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'contact' else '' ))
        __M_writer('"><a href="/contact">Contact</a></li>\r\n       <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'terms' else '' ))
        __M_writer('"><a href="/terms">Terms</a></li>\r\n       <li class="dropdown">\r\n               <a class="dropdown-toggle" data-toggle="dropdown" href="#">Login\r\n               <span class="caret"></span></a>\r\n               <ul class="dropdown-menu">\r\n                <li><a href="#">Account</a></li>\r\n                <li><a href="#">Profile</a></li>\r\n                <li><a href="#">Sign Out</a></li>\r\n               </ul>\r\n       </li>\r\n           </ul>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/mayaroney/desktop/fomo/homepage/templates/app_base.html", "uri": "app_base.html", "source_encoding": "utf-8", "line_map": {"28": 0, "38": 1, "43": 5, "48": 25, "54": 3, "60": 3, "66": 7, "73": 7, "74": 9, "75": 9, "76": 10, "77": 10, "78": 11, "79": 11, "80": 12, "81": 12, "82": 13, "83": 13, "84": 14, "85": 14, "91": 85}}
__M_END_METADATA
"""
