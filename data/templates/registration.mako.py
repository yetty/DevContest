# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1273679805.092298
_template_filename='/home/yetty/Work/Development/DevContest/devcontest/templates/registration.mako'
_template_uri='/registration.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['body', 'title']


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
    return runtime._inherit_from(context, u'/base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 42
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n<h2>Registrace</h2>\n\n')
        # SOURCE LINE 8
        if not c.success:
            # SOURCE LINE 9
            if c.errors:
                # SOURCE LINE 10
                __M_writer(u'\t\t<ol id="errors">\n')
                # SOURCE LINE 11
                for error in c.errors:
                    # SOURCE LINE 12
                    __M_writer(u'\t\t\t<li>')
                    __M_writer(escape(error))
                    __M_writer(u'</li>\n')
                    pass
                # SOURCE LINE 14
                __M_writer(u'\t\t</ol>\n')
                pass
            # SOURCE LINE 16
            __M_writer(u'\t')
            __M_writer(escape(h.form(h.url_for(controller="registration", action="check"), method="post")))
            __M_writer(u'\n\t<label for="login" class="strong">Login:</label><br/>\n\t')
            # SOURCE LINE 18
            __M_writer(escape(h.text('login', c.form['login'])))
            __M_writer(u'<br/>\n\t<label for="password" class="strong">Heslo:</label><br/>\n\t')
            # SOURCE LINE 20
            __M_writer(escape(h.password('password', c.form['password'])))
            __M_writer(u' ')
            __M_writer(escape(h.password('cpassword', c.form['cpassword'])))
            __M_writer(u' <span class="info">(dvakr\xe1t pro kontrolu)</span><br/>\n\t<label for="mail" class="strong">E-mail:</label><br/>\n\t')
            # SOURCE LINE 22
            __M_writer(escape(h.text('mail', c.form['mail'])))
            __M_writer(u'<br/>\n\t<br>\n\n\t<label for="fname">Jm\xe9no:</label><br/>\n\t')
            # SOURCE LINE 26
            __M_writer(escape(h.text('fname', c.form['fname'])))
            __M_writer(u'<br/>\n\t<label for="lname">P\u0159\xedjmen\xed:</label><br/>\n\t')
            # SOURCE LINE 28
            __M_writer(escape(h.text('lname', c.form['lname'])))
            __M_writer(u'<br/>\n\t<label for="class">T\u0159\xedda:</label><br/>\n\t')
            # SOURCE LINE 30
            __M_writer(escape(h.text('cls', c.form['cls'])))
            __M_writer(u'<br/>\n\t<br/>\n\n\t')
            # SOURCE LINE 33
            __M_writer(escape(h.submit('submit', 'Zaregistrovat')))
            __M_writer(u'\n\n\t<p class="info">\n\t\tTu\u010dn\u011b zv\xfdrazn\u011bn\xe9 polo\u017eky jsou povinn\xe9.\n\t</p>\n\t')
            # SOURCE LINE 38
            __M_writer(escape(h.end_form()))
            __M_writer(u'\n')
            # SOURCE LINE 39
        else:
            # SOURCE LINE 40
            __M_writer(u'\t<p>Registrace byla \xfasp\u011b\u0161n\xe1. Nyn\xed se m\u016f\u017eete p\u0159ihl\xe1sit formul\xe1\u0159em vlevo.</p>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Registrace')
        return ''
    finally:
        context.caller_stack._pop_frame()


