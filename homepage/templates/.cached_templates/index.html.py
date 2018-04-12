# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523513106.033213
_enable_loop = True
_template_filename = 'C:/Users/Linds/desktop/intex2_fomo/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['skip', 'top_center', 'content_right', 'content_center']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top_center():
            return render_top_center(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        def content_right():
            return render_content_right(context._locals(__M_locals))
        def skip():
            return render_skip(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'skip'):
            context['self'].skip(**pageargs)
        

        __M_writer('\r\n    <a href="#content" class="skip">Skip to content</a>\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_center'):
            context['self'].top_center(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_right'):
            context['self'].content_right(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_center'):
            context['self'].content_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_skip(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def skip():
            return render_skip(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def top_center():
            return render_top_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="row">\r\n        <img class="img-responsive background_img" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/Images/record_fit.png" alt="Black Piano"/>\r\n        <div class="title">\r\n            <a name="main-content" tabindex="-1"></a>\r\n            <h1>Family-Oriented Music Organization</h1>\r\n            <a href="/catalog/" id="shop" type="button" class="btn btn-sm btn-success">SHOP NOW</a><br/><br/>\r\n        </div>\r\n\r\n</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_right():
            return render_content_right(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div id="content">\r\n    <h2>Buy or rent from our collection!</h2>\r\n</div>\r\n\r\n\r\n    </br>\r\n    </br>\r\n    </br>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Linds/desktop/intex2_fomo/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"29": 0, "43": 1, "48": 4, "53": 17, "58": 23, "63": 34, "69": 3, "75": 3, "81": 6, "88": 6, "89": 8, "90": 8, "96": 21, "102": 21, "108": 25, "114": 25, "120": 114}}
__M_END_METADATA
"""
