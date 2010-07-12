# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1278951711.733983
_template_filename=u'/home/yetty/Work/Development/DevContest/devcontest/templates/menu.mako'
_template_uri=u'/menu.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['menu']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 35
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        request = context.get('request', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        if request.environ.get('REMOTE_USER'):
            # SOURCE LINE 3
            __M_writer(u'    <ul>\n\t\t')
            # SOURCE LINE 4

            from devcontest.model import Contest
            from devcontest.model.meta import Session
            
            
            # SOURCE LINE 7
            __M_writer(u'\n')
            # SOURCE LINE 8
            for contest in Session.query(Contest).filter_by(is_running=True).all():
                # SOURCE LINE 9
                __M_writer(u'\t\t\t<li class="h">')
                __M_writer(escape(contest.name))
                __M_writer(u'<hr></li>\n\t\t\t<li><a href=')
                # SOURCE LINE 10
                __M_writer(escape(h.url_for(controller="contest", action="tasks", id=contest.id, param=None)))
                __M_writer(u'>')
                __M_writer(escape(_('Tasks')))
                __M_writer(u'</a></li>\n\t\t\t<li><a href=')
                # SOURCE LINE 11
                __M_writer(escape(h.url_for(controller="contest", action="rank", id=contest.id, param=None)))
                __M_writer(u'>')
                __M_writer(escape(_('Ranks')))
                __M_writer(u'</a></li>\n\t\t\t<li class="break"></li>\n')
                pass
            # SOURCE LINE 14
            __M_writer(u'        <li><a href=')
            __M_writer(escape(h.url_for(controller="archiv", action="index", id=None, param=None)))
            __M_writer(u'>')
            __M_writer(escape(_('Archive')))
            __M_writer(u'</a></li>\n        <li><a href=')
            # SOURCE LINE 15
            __M_writer(escape(h.url_for(controller="page", action="documentation", id=None, param=None)))
            __M_writer(u'>')
            __M_writer(escape(_('Documentation')))
            __M_writer(u'</a></li>\n        <li><a href=')
            # SOURCE LINE 16
            __M_writer(escape(h.url_for(controller="page", action="FAQ", id=None, param=None)))
            __M_writer(u'>')
            __M_writer(escape(_('FAQ')))
            __M_writer(u'</a></li>\n        <li class="break"></li>\n')
            # SOURCE LINE 18
            if request.environ.get('REMOTE_USER').admin:
                # SOURCE LINE 19
                __M_writer(u'            <li>\n\t\t\t\t<a href="#">')
                # SOURCE LINE 20
                __M_writer(escape(_('Administration')))
                __M_writer(u'</a>\n\t\t\t\t<ul>\n\t\t\t\t\t<li><a href=')
                # SOURCE LINE 22
                __M_writer(escape(h.url_for(controller="admin", action="contest", id=None, param=None)))
                __M_writer(u'>')
                __M_writer(escape(_('Contests')))
                __M_writer(u'</a></li>\n\t\t\t\t\t<li><a href=')
                # SOURCE LINE 23
                __M_writer(escape(h.url_for(controller="admin", action="page", id=None, param=None)))
                __M_writer(u'>')
                __M_writer(escape(_('Pages')))
                __M_writer(u'</a></li>\n\t\t\t\t\t<li><a href=')
                # SOURCE LINE 24
                __M_writer(escape(h.url_for(controller="admin", action="users", id=None, param=None)))
                __M_writer(u'>')
                __M_writer(escape(_('Users')))
                __M_writer(u'</a></li>\n\t\t\t\t\t<li><a href=')
                # SOURCE LINE 25
                __M_writer(escape(h.url_for(controller="admin", action="runners", id=None, param=None)))
                __M_writer(u'>')
                __M_writer(escape(_('Starters')))
                __M_writer(u'</a></li>\n\t\t\t\t</ul>\n            </li>\n            <li class="break"></li>\n')
                pass
            # SOURCE LINE 30
            __M_writer(u'        <li><a href=')
            __M_writer(escape(h.url_for(controller="user", action="top", id="10", param=None)))
            __M_writer(u'>')
            __M_writer(escape(_('TOP10')))
            __M_writer(u'</a></li>\n        <li><a href=')
            # SOURCE LINE 31
            __M_writer(escape(h.url_for(controller="user", action="index", id=None, param=None)))
            __M_writer(u'>')
            __M_writer(escape(_('Profile')))
            __M_writer(u'</a></li>\n        <li><a href=')
            # SOURCE LINE 32
            __M_writer(escape(h.url_for(controller="auth", action="signout", id=None, param=None)))
            __M_writer(u'>')
            __M_writer(escape(_('Log out')))
            __M_writer(u'</a></li>\n    </ul>\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


