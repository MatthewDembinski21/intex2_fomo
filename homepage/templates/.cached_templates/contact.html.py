# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523514546.1491163
_enable_loop = True
_template_filename = 'C:/Users/Linds/desktop/intex2_fomo/homepage/templates/contact.html'
_template_uri = 'contact.html'
_source_encoding = 'utf-8'
import django_mako_plus
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
        def top_center():
            return render_top_center(context._locals(__M_locals))
        def content_center():
            return render_content_center(context._locals(__M_locals))
        csrf_input = context.get('csrf_input', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
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
        __M_writer("\r\n<h1 class='cen'>Contact Us</h1>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        csrf_input = context.get('csrf_input', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<br>\r\n  <form action="/contact/" method="POST" class="cen">\r\n    ')
        __M_writer(str( csrf_input ))
        __M_writer('\r\n    First name:\r\n    <input type="text" name="fname">\r\n    <br><br>\r\n    Last name:\r\n    <input type="text" name="lname">\r\n    <br><br>\r\n    What\'s up:\r\n    <input type="text" name="question">\r\n    <br><br>\r\n    <input type="submit" value="Submit" class="btn btn-md btn-info">\r\n  </form>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Linds/desktop/intex2_fomo/homepage/templates/contact.html", "uri": "contact.html", "source_encoding": "utf-8", "line_map": {"29": 0, "39": 1, "44": 5, "49": 23, "55": 3, "61": 3, "67": 8, "74": 8, "75": 11, "76": 11, "82": 76}}
__M_END_METADATA
"""
