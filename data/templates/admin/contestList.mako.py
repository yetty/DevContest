# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1274964964.6698649
_template_filename='/home/yetty/Work/Development/DevContest/devcontest/templates/admin/contestList.mako'
_template_uri='/admin/contestList.mako'
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
    return runtime._inherit_from(context, u'/admin/base.mako', _template_uri)
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
        __M_writer(u'\n\t<h2>Seznam sout\u011b\u017e\xed</h2>\n\t<table class="dark">\n')
        # SOURCE LINE 8
        for contest in c.list:
            # SOURCE LINE 9
            __M_writer(u'\t\t\t<tr>\n\t\t\t\t<td class="ns">')
            # SOURCE LINE 10
            __M_writer(escape(contest.id))
            __M_writer(u'</td>\n\t\t\t\t<td>\n')
            # SOURCE LINE 12
            if contest.is_running:
                # SOURCE LINE 13
                __M_writer(u'\t\t\t\t\t<img src="/running.gif" alt="is running">\n')
                pass
            # SOURCE LINE 15
            __M_writer(u'\t\t\t\t')
            __M_writer(escape(contest.name))
            __M_writer(u'</td>\n\t\t\t\t<td class="ns">\n\t\t\t\t<a href=')
            # SOURCE LINE 17
            __M_writer(escape(h.url_for(id=contest.id, param="cp")))
            __M_writer(u'>\n')
            # SOURCE LINE 18
            if contest.pilsprog_mode:
                # SOURCE LINE 19
                __M_writer(u'\t\t\t\t\tPilsprog\n')
                # SOURCE LINE 20
            else:
                # SOURCE LINE 21
                __M_writer(u'\t\t\t\t\tNormal\n')
                pass
            # SOURCE LINE 23
            __M_writer(u'\t\t\t\t</a></td>\n\t\t\t\t<td class="ns">\n')
            # SOURCE LINE 25
            if contest.is_running:
                # SOURCE LINE 26
                __M_writer(u'\t\t\t\t\t<a href=')
                __M_writer(escape(h.url_for(id=contest.id, param="stop")))
                __M_writer(u'><img src="/pause.png" alt="stop"></a>\n')
                # SOURCE LINE 27
            else:
                # SOURCE LINE 28
                __M_writer(u'\t\t\t\t\t<a href=')
                __M_writer(escape(h.url_for(id=contest.id, param="start")))
                __M_writer(u'><img src="/play.png" alt="start"></a>\n')
                pass
            # SOURCE LINE 30
            __M_writer(u'\t\t\t\t</td>\n\t\t\t\t<td class="ns"><a href=')
            # SOURCE LINE 31
            __M_writer(escape(h.url_for(id=contest.id)))
            __M_writer(u'><img src="/edit.png" alt="e"></a></td>\n\t\t\t\t<td class="ns"><a href="#" ondblclick=\'remove("')
            # SOURCE LINE 32
            __M_writer(escape(h.url_for(id=contest.id, param="remove")))
            __M_writer(u'");\'><img src="/remove.png" alt="e"></a></td>\n\n\t\t\t</tr>\n')
            pass
        # SOURCE LINE 36
        __M_writer(u'\t</table>\n\t<hr>\n\t ')
        # SOURCE LINE 38
        __M_writer(escape(h.form_start(h.url_for(id="_", param="create"), method="post")))
        __M_writer(u'\n\t ')
        # SOURCE LINE 39
        __M_writer(escape(h.field("Název soutěže", h.text(name="name"))))
        __M_writer(u'\n\t ')
        # SOURCE LINE 40
        __M_writer(escape(h.field("", h.submit("submit", "Vytvořit"))))
        __M_writer(u'\n\t ')
        # SOURCE LINE 41
        __M_writer(escape(h.form_end()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Seznam sout\u011b\u017e\xed')
        return ''
    finally:
        context.caller_stack._pop_frame()


