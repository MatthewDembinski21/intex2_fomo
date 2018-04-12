# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523548743.9264762
_enable_loop = True
_template_filename = 'C:/Users/Linds/desktop/intex2_fomo/catalog/templates/app_base.html'
_template_uri = 'app_base.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['menu', 'nav_main', 'content_left', 'content_right']


from catalog import models as cmod

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
        def nav_main():
            return render_nav_main(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        category = context.get('category', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def menu():
            return render_menu(context._locals(__M_locals))
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
        def nav_main():
            return render_nav_main(context)
        request = context.get('request', UNDEFINED)
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
        category = context.get('category', UNDEFINED)
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        __M_writer("\r\n</br>\r\n</br>\r\n<ul id='catlist'>\r\n  <li><a id='allprod' href='/catalog/index'/>All Products</a></li>\r\n  ")
        __M_writer('\r\n')
        for c in cmod.Category.objects.all():
            if category == c.name:
                __M_writer("      <li><a class ='active' href='/catalog/index/")
                __M_writer(str(c.id))
                __M_writer("'/>")
                __M_writer(str(c.name))
                __M_writer('</a></li>\r\n')
            else:
                __M_writer("      <li><a href='/catalog/index/")
                __M_writer(str(c.id))
                __M_writer("'/>")
                __M_writer(str(c.name))
                __M_writer('</a></li>\r\n')
        __M_writer('\r\n    <!--<ul id="category_list">-->\r\n        <!--<li><a  href="/catalog/index/0/">All Products</a></li>-->\r\n        <!--%for c in categoryList:-->\r\n            <!--<li><a id="name" href="/catalog/index/')
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
        def content_right():
            return render_content_right(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n</br>\r\n    <h3>Recently Viewed</h3>\r\n        ')

        if request.dmp.page == 'details':
            myList = request.last_five[1:6]
        else:
            myList = request.last_five[0:5]
                
        
        __M_writer("\r\n        <ol id='thumbnailsRight' class='rv cen'>\r\n")
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
{"filename": "C:/Users/Linds/desktop/intex2_fomo/catalog/templates/app_base.html", "uri": "app_base.html", "source_encoding": "utf-8", "line_map": {"18": 2, "20": 27, "33": 0, "48": 1, "49": 2, "54": 7, "59": 19, "64": 42, "69": 60, "75": 5, "81": 5, "87": 10, "94": 10, "95": 12, "96": 12, "97": 13, "98": 13, "99": 14, "100": 14, "101": 15, "102": 15, "103": 16, "104": 16, "105": 17, "106": 17, "112": 22, "119": 22, "120": 27, "121": 28, "122": 29, "123": 30, "124": 30, "125": 30, "126": 30, "127": 30, "128": 31, "129": 32, "130": 32, "131": 32, "132": 32, "133": 32, "134": 35, "135": 39, "136": 39, "137": 39, "138": 39, "144": 45, "151": 45, "152": 48, "159": 53, "160": 55, "161": 56, "162": 56, "163": 56, "164": 56, "165": 56, "166": 57, "167": 57, "168": 59, "174": 168}}
__M_END_METADATA
"""
