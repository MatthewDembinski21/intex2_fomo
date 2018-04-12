# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1522732944.0809944
_enable_loop = True
_template_filename = 'C:/Users/mayaroney/desktop/fomo/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['header_maintenance', 'skip', 'nav_main', 'top_center', 'content_left', 'content_center', 'content_right', 'bottom', 'footer']


from catalog import models as cmod

from datetime import datetime 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def bottom():
            return render_bottom(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def skip():
            return render_skip(context._locals(__M_locals))
        def top_center():
            return render_top_center(context._locals(__M_locals))
        def nav_main():
            return render_nav_main(context._locals(__M_locals))
        def header_maintenance():
            return render_header_maintenance(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n\r\n\r\n<html>\r\n<meta charset="UTF-8">\r\n<head>\r\n\r\n    <title>FOMO</title>\r\n\r\n')
        __M_writer('    <!--<script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>-->\r\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap3/js/bootstrap.min.js"></script>\r\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap3/css/bootstrap.min.css"/>\r\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap3/css/bootstrap-theme.min.css"/>\r\n    <link href="https://fonts.googleapis.com/css?family=Quicksand" rel="stylesheet">\r\n\r\n\r\n')
        __M_writer('    <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n    ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n')
        __M_writer('    <link id = "icon" rel="shortcut icon" type="image/png" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/Images/icon.png"/>\r\n\r\n\r\n</head>\r\n<body>\r\n<a href="#content" class="skip">Skip to content</a>\r\n\r\n<header>\r\n    <!--Maintenance Message-->\r\n    <div id="maintenance">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_maintenance'):
            context['self'].header_maintenance(**pageargs)
        

        __M_writer('\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'skip'):
            context['self'].skip(**pageargs)
        

        __M_writer('\r\n    </div>\r\n\r\n\r\n    <!--Make a navbar-->\r\n    <nav class="navbar navbar-inverse">\r\n      <div class="container-fluid">\r\n        <div class="navbar-header">\r\n          <a class="navbar-brand" href="index"><img id="icon" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/Images/icon.png"/></a>\r\n        </div>\r\n          <ul class="nav navbar-nav">\r\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav_main'):
            context['self'].nav_main(**pageargs)
        

        __M_writer('\r\n        </ul>\r\n               <ul class="nav navbar-nav navbar-right">\r\n')
        if request.user.is_authenticated:
            __M_writer('                   <li class=" ')
            __M_writer(str( 'active' if request.dmp.page == 'cart' else '' ))
            __M_writer('">\r\n                       <a href="/catalog/cart">\r\n\r\n')
            if cmod.Order.objects.filter(user = request.user,status='cart').first() is not None:
                __M_writer('                                   ')
                __M_writer(str(cmod.Order.objects.filter(user = request.user,status='cart').first().num_items()))
                __M_writer('\r\n                                   <span class="glyphicon glyphicon-shopping-cart"></span></a>\r\n')
            __M_writer('\r\n                   </li>\r\n                        <li class="dropdown">\r\n                           <a class="dropdown-toggle" data-toggle="dropdown" href="#">\r\n                               Welcome ')
            __M_writer(str(request.user.first_name))
            __M_writer(' ')
            __M_writer(str(request.user.last_name))
            __M_writer('\r\n                           <span class="caret"></span></a>\r\n                           <ul class="dropdown-menu">\r\n                            <li><a href="#">My Account</a></li>\r\n                            <li><a href="/account/logout">Log Out</a></li>\r\n                           </ul>\r\n                         </li>\r\n')
        else:
            __M_writer('                        <li><a href="/account/signup">Sign Up</a></li>\r\n                        <li><a href="/account/login">Login</a></li>\r\n               </ul>\r\n')
        __M_writer('\r\n      </div>\r\n    </nav>\r\n\r\n\r\n</header>\r\n\r\n<main>\r\n\r\n    <div id="top">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_center'):
            context['self'].top_center(**pageargs)
        

        __M_writer('\r\n    </div>\r\n\r\n    <div id="middle">\r\n        <div id="left">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_left'):
            context['self'].content_left(**pageargs)
        

        __M_writer('\r\n        </div>\r\n\r\n        <div id="center">\r\n            <div id="content">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n            </div>\r\n        </div>\r\n\r\n        <div id="right">\r\n            ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\r\n        </div>\r\n    </div>\r\n\r\n    <div id="bottom">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'bottom'):
            context['self'].bottom(**pageargs)
        

        __M_writer('\r\n    </div>\r\n\r\n</main>\r\n\r\n<div class="text-center">\r\n    <footer>\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\r\n</footer>\r\n</div>\r\n\r\n\r\n</body>\r\n\r\n\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header_maintenance(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header_maintenance():
            return render_header_maintenance(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_skip(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def skip():
            return render_skip(context)
        __M_writer = context.writer()
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
        __M_writer('\r\n                   <li class="')
        __M_writer(str( 'active' if request.dmp.page == 'index' else '' ))
        __M_writer('"><a href="/">Home</a></li>\r\n                   <li class = "nav item ')
        __M_writer(str( 'active' if request.dmp.page == 'index' and request.dmp.app == 'catalog' else ''))
        __M_writer('"><a href="/catalog/">Catalog</a></li>\r\n                   <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'about' else '' ))
        __M_writer('"><a href="/about">About Us</a></li>\r\n                   <li class=" ')
        __M_writer(str('active' if request.dmp.page == 'faq' else '' ))
        __M_writer('"><a href="/faq">FAQ</a></li>\r\n                   <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'contact' else '' ))
        __M_writer('"><a href="/contact">Contact</a></li>\r\n                   <li class=" ')
        __M_writer(str( 'active' if request.dmp.page == 'terms' else '' ))
        __M_writer('"><a href="/terms">Terms</a></li>\r\n              ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_center():
            return render_top_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n            <!--Page Title-->\r\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_left():
            return render_content_left(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bottom(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def bottom():
            return render_bottom(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\r\n        ')
        __M_writer('\r\n        &copy; Copyright ')
        __M_writer(str( datetime.now().year))
        __M_writer('. All rights reserved.\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/mayaroney/desktop/fomo/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "20": 123, "22": 0, "48": 2, "49": 14, "50": 14, "51": 14, "52": 16, "53": 16, "54": 17, "55": 17, "56": 18, "57": 18, "58": 23, "59": 24, "60": 24, "61": 27, "62": 27, "63": 27, "68": 37, "73": 38, "74": 46, "75": 46, "80": 56, "81": 59, "82": 60, "83": 60, "84": 60, "85": 63, "86": 64, "87": 64, "88": 64, "89": 67, "90": 71, "91": 71, "92": 71, "93": 71, "94": 78, "95": 79, "96": 83, "101": 95, "106": 100, "111": 105, "116": 110, "121": 115, "126": 125, "132": 37, "143": 38, "154": 49, "161": 49, "162": 50, "163": 50, "164": 51, "165": 51, "166": 52, "167": 52, "168": 53, "169": 53, "170": 54, "171": 54, "172": 55, "173": 55, "179": 93, "185": 93, "191": 100, "202": 105, "213": 110, "224": 115, "235": 122, "241": 122, "242": 123, "243": 124, "244": 124, "250": 244}}
__M_END_METADATA
"""
