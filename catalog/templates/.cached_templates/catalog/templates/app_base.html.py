# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1522783728.742915
_enable_loop = True
_template_filename = 'C:/Users/mayaroney/desktop/fomo/catalog/templates/app_base.html'
_template_uri = '/catalog/templates/app_base.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['menu', 'nav_main', 'content_left', 'content_right']


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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def nav_main():
            return render_nav_main(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def menu():
            return render_menu(context._locals(__M_locals))
        name = context.get('name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu'):
            context['self'].menu(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav_main'):
            context['self'].nav_main(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

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
        __M_writer('\r\n\r\n       <li class = "nav item ')
        __M_writer(str( 'active' if request.dmp.page == 'index' and request.dmp.app == 'homepage' else ''))
        __M_writer('"><a href="/index/">Home</a></li>\r\n       <li class = "nav item ')
        __M_writer(str( 'active' if request.dmp.page == 'index' and request.dmp.app == 'catalog' else ''))
        __M_writer('"><a href="/catalog/">Catalog</a></li>\r\n       <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'about' else '' ))
        __M_writer('"><a href="/about">About Us</a></li>\r\n       <li class=" ')
        __M_writer(str('active' if request.dmp.page == 'faq' else '' ))
        __M_writer('"><a href="/faq">FAQ</a></li>\r\n       <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'contact' else '' ))
        __M_writer('"><a href="/contact">Contact</a></li>\r\n       <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'terms' else '' ))
        __M_writer('"><a href="/terms">Terms</a></li>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        name = context.get('name', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n</br>\r\n</br>\r\n\r\n<ul id="category_list" class="nav  nav-pills nav-stacked">\r\n        <li>\r\n            <a href="/catalog/index/" type="button"\r\n               class="btn btn-link nav-item category_nav ')
        __M_writer(str('on' if name == 'All Products' else 'off'))
        __M_writer('">All\r\n                Products</a>\r\n        </li>\r\n')
        for c in cmod.Category.objects.all():
            __M_writer('            <li>\r\n\r\n                <a id="but" href="/catalog/index/')
            __M_writer(str(c.id))
            __M_writer('" type="button"\r\n                   class="btn btn-link nav-item category_nav ')
            __M_writer(str('on' if c.name == name else 'off'))
            __M_writer('">')
            __M_writer(str(c.name))
            __M_writer('</a>\r\n            </li>\r\n')
        __M_writer('    </ul>\r\n\r\n    <!--<ul id="category_list">-->\r\n        <!--<li><a  href="/catalog/index/0/">All Products</a></li>-->\r\n        <!--%for c in categoryList:-->\r\n            <!--<li><a id="name" href="/catalog/index/')
        __M_writer(str(c.id))
        __M_writer('/">')
        __M_writer(str(c.name))
        __M_writer('</a></li>-->\r\n        <!--%endfor-->\r\n    <!--</ul>-->\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n</br></br></br></br>\r\n    <h3>Recently Viewed</h3>\r\n        ')

        if request.dmp.page == 'details':
            myList = request.last_five[1:6]
        else:
            myList = request.last_five[0:5]
                
        
        __M_writer("\r\n        <ol id='thumbnailsRight'>\r\n")
        for h in myList:
            __M_writer('                <a href="/catalog/details/')
            __M_writer(str(h.id))
            __M_writer('/"><li class =\'rightimage\' alt=""><img src=\'')
            __M_writer(str(h.image_url()))
            __M_writer("'></li></a>\r\n                <p>")
            __M_writer(str(h.name))
            __M_writer('</p>\r\n')
        __M_writer('         </ol>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/mayaroney/desktop/fomo/catalog/templates/app_base.html", "uri": "/catalog/templates/app_base.html", "source_encoding": "utf-8", "line_map": {"18": 2, "31": 0, "46": 1, "47": 2, "52": 7, "57": 19, "62": 47, "67": 65, "73": 5, "79": 5, "85": 10, "92": 10, "93": 12, "94": 12, "95": 13, "96": 13, "97": 14, "98": 14, "99": 15, "100": 15, "101": 16, "102": 16, "103": 17, "104": 17, "110": 22, "117": 22, "118": 29, "119": 29, "120": 32, "121": 33, "122": 35, "123": 35, "124": 36, "125": 36, "126": 36, "127": 36, "128": 39, "129": 44, "130": 44, "131": 44, "132": 44, "138": 50, "145": 50, "146": 53, "153": 58, "154": 60, "155": 61, "156": 61, "157": 61, "158": 61, "159": 61, "160": 62, "161": 62, "162": 64, "168": 162}}
__M_END_METADATA
"""
