# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517947061.3193831
_enable_loop = True
_template_filename = 'C:/Users/mayaroney/PycharmProjects/fomo/account/templates/formtest.html'
_template_uri = 'formtest.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['top_center']


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
        csrf_input = context.get('csrf_input', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_center'):
            context['self'].top_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_center():
            return render_top_center(context)
        csrf_input = context.get('csrf_input', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <!--<form action="/account/formtest/" method="POST">-->\r\n        <!--')
        __M_writer(str( csrf_input ))
        __M_writer('-->\r\n        <!--')
        __M_writer(str( form.as_p() ))
        __M_writer('-->\r\n        <!--<input type="submit" value="Submit" />-->\r\n    <!--</form>-->\r\n    ')
        __M_writer(str( form ))
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/mayaroney/PycharmProjects/fomo/account/templates/formtest.html", "uri": "formtest.html", "source_encoding": "utf-8", "line_map": {"28": 0, "37": 1, "42": 12, "48": 3, "56": 3, "57": 6, "58": 6, "59": 7, "60": 7, "61": 10, "62": 10, "68": 62}}
__M_END_METADATA
"""
