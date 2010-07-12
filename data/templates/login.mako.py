# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1278415027.1491721
_template_filename=u'/home/yetty/Work/Development/DevContest/devcontest/templates/login.mako'
_template_uri=u'/login.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['login_box']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 16
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_login_box(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        if not request.environ.get('REMOTE_USER'):
            # SOURCE LINE 3
            if c.error:
                # SOURCE LINE 4
                __M_writer(u'\t\t\t<span class="strong">')
                __M_writer(escape(c.error))
                __M_writer(u'</span><br/>\n')
                pass
            # SOURCE LINE 6
            __M_writer(u'        ')
            __M_writer(escape(h.form(h.url_for(controller="auth", action="signin"), method="post")))
            __M_writer(u'\n        <label for="login">Login:</label>')
            # SOURCE LINE 7
            __M_writer(escape(h.text('login')))
            __M_writer(u'<br/>\n        <label for="password">Heslo:</label>')
            # SOURCE LINE 8
            __M_writer(escape(h.password('password')))
            __M_writer(u'<br/>\n        ')
            # SOURCE LINE 9
            __M_writer(escape(h.submit('submit', 'Přihlásit')))
            __M_writer(u'\n        ')
            # SOURCE LINE 10
            __M_writer(escape(h.end_form()))
            __M_writer(u'\n\n        <p><a href=')
            # SOURCE LINE 12
            __M_writer(escape(h.url_for(controller="registration", action="index")))
            __M_writer(u'>&rang; Registrace</a></p>\n')
            # SOURCE LINE 13
        else:
            # SOURCE LINE 14
            __M_writer(u'        Jste p\u0159ihl\xe1\u0161en jako <strong>')
            __M_writer(escape(request.environ.get('REMOTE_USER').fname))
            __M_writer(u' ')
            __M_writer(escape(request.environ.get('REMOTE_USER').lname))
            __M_writer(u' </strong>.\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


