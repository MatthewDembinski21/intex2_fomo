# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523553341.8449745
_enable_loop = True
_template_filename = 'C:/Users/Linds/desktop/intex2_fomo/homepage/templates/base.htm'
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
        def skip():
            return render_skip(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def bottom():
            return render_bottom(context._locals(__M_locals))
        def top_center():
            return render_top_center(context._locals(__M_locals))
        def header_maintenance():
            return render_header_maintenance(context._locals(__M_locals))
        def nav_main():
            return render_nav_main(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        def content_left():
            return render_content_left(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def content_center():
            return render_content_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n\r\n\r\n<html>\r\n<meta charset="UTF-8">\r\n<head>\r\n\r\n    <title>FOMO</title>\r\n\r\n')
        __M_writer('    <!--<script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery-3.3.1.js"></script>-->\r\n    <script src="//ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>\r\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap3/js/bootstrap.min.js"></script>\r\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap3/css/bootstrap.min.css"/>\r\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap3/css/bootstrap-theme.min.css"/>\r\n    <link href=\'https://fonts.googleapis.com/css?family=Satisfy\' rel=\'stylesheet\'>\r\n    <link href=\'https://fonts.googleapis.com/css?family=Hammersmith One\' rel=\'stylesheet\'>\r\n    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">\r\n\r\n\r\n')
        __M_writer('    <script src="/django_mako_plus/dmp-common.min.js"></script>\r\n    ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\r\n\r\n')
        __M_writer('    <link rel="fluid icon" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('homepage/media/images/favicon.ico">\r\n\r\n\r\n</head>\r\n<body>\r\n<a href="#content" class="skip">Skip to content</a>\r\n\r\n<header>\r\n    <!--Maintenance Message-->\r\n    <div id="maintenance">\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header_maintenance'):
            context['self'].header_maintenance(**pageargs)
        

        __M_writer('\r\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'skip'):
            context['self'].skip(**pageargs)
        

        __M_writer('\r\n    </div>\r\n\r\n\r\n    <!--Make a navbar-->\r\n    <nav class="navbar navbar-inverse">\r\n      <div class="container-fluid">\r\n        <div class="navbar-header">\r\n          <a class="navbar-brand" href="index"><i class="fa fa-headphones" style="color:#3D5A67;"></i></a>\r\n        </div>\r\n          <ul class="nav navbar-nav">\r\n              ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'nav_main'):
            context['self'].nav_main(**pageargs)
        

        __M_writer('\r\n        </ul>\r\n               <ul class="nav navbar-nav navbar-right">\r\n')
        if request.user.is_authenticated:
            __M_writer('                       <li class=" ')
            __M_writer(str( 'active' if request.dmp.page == 'cart' else '' ))
            __M_writer('">\r\n                            <a href="/catalog/cart">\r\n\r\n')
            if cmod.Order.objects.filter(user = request.user,status='cart').first() is not None:
                __M_writer('                                       ')
                __M_writer(str(cmod.Order.objects.filter(user = request.user,status='cart').first().num_items()))
                __M_writer('\r\n                                       <span class="glyphicon glyphicon-shopping-cart"></span>\r\n')
            __M_writer('                            </a>\r\n                       </li>\r\n                        <li class="dropdown">\r\n                           <a class="dropdown-toggle" data-toggle="dropdown" href="#">\r\n                               Welcome ')
            __M_writer(str(request.user.first_name))
            __M_writer(' ')
            __M_writer(str(request.user.last_name))
            __M_writer('\r\n                           <span class="caret"></span></a>\r\n                           <ul class="dropdown-menu blue">\r\n                            <li><a href="#"><i class="fa fa-id-card" style="color:#3D5A67;"></i> My Account</a></li>\r\n                            <li><a href="/account/logout"><i class="fa fa-user-times" style="color:#3D5A67;"></i> Log Out</a></li>\r\n                           </ul>\r\n                         </li>\r\n')
        else:
            __M_writer('                        <li><a href="/account/signup"><i class="fa fa-user-plus"></i> Sign Up</a></li>\r\n                        <li><a href="/account/login"><i class="fa fa-sign-in"></i> Login</a></li>\r\n               </ul>\r\n')
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
        

        __M_writer('\r\n    </div>\r\n\r\n</main>\r\n\r\n<div class="footerstuff cen">\r\n    <footer>\r\n    ')
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
        def nav_main():
            return render_nav_main(context)
        request = context.get('request', UNDEFINED)
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
{"filename": "C:/Users/Linds/desktop/intex2_fomo/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"18": 2, "20": 125, "22": 0, "48": 2, "49": 14, "50": 14, "51": 14, "52": 16, "53": 16, "54": 17, "55": 17, "56": 18, "57": 18, "58": 25, "59": 26, "60": 26, "61": 29, "62": 29, "63": 29, "68": 39, "73": 40, "78": 58, "79": 61, "80": 62, "81": 62, "82": 62, "83": 65, "84": 66, "85": 66, "86": 66, "87": 69, "88": 73, "89": 73, "90": 73, "91": 73, "92": 80, "93": 81, "94": 85, "99": 97, "104": 102, "109": 107, "114": 112, "119": 117, "124": 127, "130": 39, "141": 40, "152": 51, "159": 51, "160": 52, "161": 52, "162": 53, "163": 53, "164": 54, "165": 54, "166": 55, "167": 55, "168": 56, "169": 56, "170": 57, "171": 57, "177": 95, "183": 95, "189": 102, "200": 107, "211": 112, "222": 117, "233": 124, "239": 124, "240": 125, "241": 126, "242": 126, "248": 242}}
__M_END_METADATA
"""
