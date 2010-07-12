# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1274518259.8353381
_template_filename='/home/yetty/Work/Development/DevContest/devcontest/templates/archiv.mako'
_template_uri='archiv.mako'
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
        # SOURCE LINE 30
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n\t<h2>Seznam sout\u011b\u017e\xed</h2>\n\t<table class="dark">\n\t<thead>\n\t\t<th class="ns"></th>\n\t\t<th width=80% colspan=3>N\xe1zev</th>\n\t\t<th>Zah\xe1jen\xed</th>\n\t</thead>\n\t')
        # SOURCE LINE 13
        i = -1 
        
        __M_writer(u'\n')
        # SOURCE LINE 14
        for i, contest in enumerate(c.list):
            # SOURCE LINE 15
            __M_writer(u'\t\t<tr>\n\t\t\t<td class="ns">')
            # SOURCE LINE 16
            __M_writer(escape(i+1))
            __M_writer(u'</td>\n\t\t\t<td width=50%>')
            # SOURCE LINE 17
            __M_writer(escape(contest.name))
            __M_writer(u'</td>\n\t\t\t<td style="text-align:center;"><a href=')
            # SOURCE LINE 18
            __M_writer(escape(h.url_for(controller="archiv", action="contest", id=contest.id)))
            __M_writer(u'>\xfalohy</a></td>\n\t\t\t<td style="text-align:center;"><a href=')
            # SOURCE LINE 19
            __M_writer(escape(h.url_for(controller="contest", action="rank", id=contest.id)))
            __M_writer(u'>po\u0159ad\xed</a></td>\n\t\t\t<td style="text-align:center;">')
            # SOURCE LINE 20
            __M_writer(escape(contest.timeStart.strftime("%d.%m.%Y")))
            __M_writer(u'</td>\n\t\t</tr>\n')
            pass
        # SOURCE LINE 23
        if i<0:
            # SOURCE LINE 24
            __M_writer(u'    <tr>\n\t\t<td class="ns"></td>\n\t\t<td class="ns info" colspan=3>Je\u0161t\u011b nem\xe1me \u017e\xe1dnou sout\u011b\u017e v archivu!</td>\n\t</tr>\n')
            pass
        # SOURCE LINE 29
        __M_writer(u'\t</table>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Seznam ot\xe1zek')
        return ''
    finally:
        context.caller_stack._pop_frame()


