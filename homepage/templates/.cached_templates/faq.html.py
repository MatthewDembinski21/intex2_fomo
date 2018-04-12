# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523514383.4138267
_enable_loop = True
_template_filename = 'C:/Users/Linds/desktop/intex2_fomo/homepage/templates/faq.html'
_template_uri = 'faq.html'
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
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_center'):
            context['self'].top_center(**pageargs)
        

        __M_writer('\r\n\r\n')
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
        __M_writer("\r\n<h1 class='cen'>Frequently Asked Questions</h1>\r\n")
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_center():
            return render_content_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n<h2>Questions:</h2>\r\n  <p>1. How many instruments do you have?</p>\r\n  <p>2. How long do I rent the instrument before I own it?</p>\r\n  <p>3. Do you have any other locations?</p>\r\n\r\n<h2>Answers:</h2>\r\n  <p>1. At least 12.</p>\r\n  <p>2. 18 months.</p>\r\n  <p>3. No, just this one.</p>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Linds/desktop/intex2_fomo/homepage/templates/faq.html", "uri": "faq.html", "source_encoding": "utf-8", "line_map": {"29": 0, "38": 1, "43": 6, "48": 19, "54": 4, "60": 4, "66": 8, "72": 8, "78": 72}}
__M_END_METADATA
"""
