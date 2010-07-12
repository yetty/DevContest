# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1278952252.6873159
_template_filename='/home/yetty/Work/Development/DevContest/devcontest/templates/admin/userEdit.mako'
_template_uri='admin/userEdit.mako'
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
    return runtime._inherit_from(context, u'base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n<a href=')
        # SOURCE LINE 6
        __M_writer(escape(h.url_for(controller="admin", action="users", id=None, param=None)))
        __M_writer(u' class="back">')
        __M_writer(escape(_('back to the list')))
        __M_writer(u'</a>\n<h2>')
        # SOURCE LINE 7
        __M_writer(escape(_('Editation of profile')))
        __M_writer(u'</h2>\n\n')
        # SOURCE LINE 9
        __M_writer(escape(h.form(h.url_for(controller="admin", action="users", id="save", param=c.user.id), method="post")))
        __M_writer(u'\n<label for="login" class="strong">')
        # SOURCE LINE 10
        __M_writer(escape(_('Login')))
        __M_writer(u':</label>\n')
        # SOURCE LINE 11
        __M_writer(escape(c.user.login))
        __M_writer(u'<br/><br/>\n<label for="password" class="strong">')
        # SOURCE LINE 12
        __M_writer(escape(_('Password')))
        __M_writer(u':</label><br>\n')
        # SOURCE LINE 13
        __M_writer(escape(h.password('password')))
        __M_writer(u' ')
        __M_writer(escape(h.password('cpassword')))
        __M_writer(u' <span class="info">(')
        __M_writer(escape(_('twice for sure')))
        __M_writer(u')</span><br/>\n<label for="mail" class="strong">')
        # SOURCE LINE 14
        __M_writer(escape(_('E-mail')))
        __M_writer(u':</label><br/>\n')
        # SOURCE LINE 15
        __M_writer(escape(h.text('mail', c.user.mail)))
        __M_writer(u'<br/>\n<br>\n\n<label for="fname">')
        # SOURCE LINE 18
        __M_writer(escape(_('First name')))
        __M_writer(u':</label><br/>\n')
        # SOURCE LINE 19
        __M_writer(escape(h.text('fname', c.user.fname)))
        __M_writer(u'<br/>\n<label for="lname">')
        # SOURCE LINE 20
        __M_writer(escape(_('Last name')))
        __M_writer(u':</label><br/>\n')
        # SOURCE LINE 21
        __M_writer(escape(h.text('lname', c.user.lname)))
        __M_writer(u'<br/>\n<label for="class">')
        # SOURCE LINE 22
        __M_writer(escape(_('Class')))
        __M_writer(u':</label><br/>\n')
        # SOURCE LINE 23
        __M_writer(escape(h.text('cls', c.user.cls)))
        __M_writer(u'<br/>\n<br/>\n\n<label for="class">')
        # SOURCE LINE 26
        __M_writer(escape(_('Administrator')))
        __M_writer(u':</label>\n')
        # SOURCE LINE 27
        __M_writer(escape(h.checkbox('admin', checked=c.user.admin)))
        __M_writer(u'<br/>\n\n\n')
        # SOURCE LINE 30
        __M_writer(escape(h.submit('submit', _('Submit'))))
        __M_writer(u'\n')
        # SOURCE LINE 31
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(escape(_('Profile')))
        return ''
    finally:
        context.caller_stack._pop_frame()


