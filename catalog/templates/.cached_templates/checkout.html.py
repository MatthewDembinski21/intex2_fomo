# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1523321560.219288
_enable_loop = True
_template_filename = '/Users/matthewdembinski/Downloads/fomo/catalog/templates/checkout.html'
_template_uri = 'checkout.html'
_source_encoding = 'utf-8'
import django_mako_plus
import django_mako_plus
_exports = ['top_center', 'content_center']


from catalog import models as cmod

def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.ModuleNamespace('fl', context._clean_inheritance_tokens(), callables=None, calling_uri=_template_uri, module='formlib.tags')
    context.namespaces[(__name__, 'fl')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        fl = _mako_get_namespace(context, 'fl')
        def content_center():
            return render_content_center(context._locals(__M_locals))
        totalPrice = context.get('totalPrice', UNDEFINED)
        def top_center():
            return render_top_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_center'):
            context['self'].top_center(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n')
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
        __M_writer('\r\n<h2 id="shopTitle">Shopping Cart</h2>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        fl = _mako_get_namespace(context, 'fl')
        def content_center():
            return render_content_center(context)
        totalPrice = context.get('totalPrice', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <h3>Total Price: $')
        __M_writer(str( totalPrice ))
        __M_writer('</h3>\r\n\r\n   ')
        __M_writer('\r\n    ')
        def ccall(caller):
            def body():
                settings = context.get('settings', UNDEFINED)
                cart = context.get('cart', UNDEFINED)
                int = context.get('int', UNDEFINED)
                __M_writer = context.writer()
                __M_writer('\r\n  <div class="text-center">\r\n    <script\r\n        src="https://checkout.stripe.com/checkout.js"\r\n        class="stripe-button"\r\n        data-key="')
                __M_writer(str(settings.STRIPE_PUBLIC_KEY))
                __M_writer('"\r\n        data-amount="')
                __M_writer(str(int(cart.total_price * 100)))
                __M_writer('"\r\n        data-description="Please Enter Your Payment Information"\r\n        data-image="https://stripe.com/img/documentation/checkout/marketplace.png"\r\n        data-local="auto"\r\n        data-label="Pay Now">\r\n    </script>\r\n\r\n  </div>\r\n')
                return ''
            return [body]
        context.caller_stack.nextcaller = runtime.Namespace('caller', context, callables=ccall(__M_caller))
        try:
            __M_writer(str(fl.render()))
        finally:
            context.caller_stack.nextcaller = None
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/matthewdembinski/Downloads/fomo/catalog/templates/checkout.html", "uri": "checkout.html", "source_encoding": "utf-8", "line_map": {"18": 2, "27": 13, "33": 0, "44": 1, "45": 2, "50": 6, "55": 29, "61": 4, "67": 4, "73": 10, "81": 10, "82": 11, "83": 11, "84": 13, "91": 14, "92": 19, "93": 19, "94": 20, "95": 20, "100": 14, "103": 28, "109": 103}}
__M_END_METADATA
"""
