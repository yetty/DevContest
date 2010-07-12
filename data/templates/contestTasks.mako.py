# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1274518324.5524421
_template_filename='/home/yetty/Work/Development/DevContest/devcontest/templates/contestTasks.mako'
_template_uri='/contestTasks.mako'
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
        # SOURCE LINE 21
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
        __M_writer(u'\n\t<h2>Seznam ot\xe1zek</h2>\n\t<table class="dark">\n\t<thead>\n\t\t<th class="ns"></th>\n\t\t<th>N\xe1zev</th>\n\t\t<th>\u010cas vy\u0159e\u0161en\xed</th>\n\t</thead>\n')
        # SOURCE LINE 13
        for i, task in enumerate(c.list):
            # SOURCE LINE 14
            __M_writer(u'\t\t<tr>\n\t\t\t<td class="ns">')
            # SOURCE LINE 15
            __M_writer(escape(i+1))
            __M_writer(u'</td>\n\t\t\t<td><a href=')
            # SOURCE LINE 16
            __M_writer(escape(h.url_for(controller="task", action="show", id=task.id)))
            __M_writer(u'>')
            __M_writer(escape(task.name))
            __M_writer(u'</a></td>\n\t\t\t<td style="text-align:center;">')
            # SOURCE LINE 17
            __M_writer(escape(c.timeSolved(task.id)))
            __M_writer(u'</td>\n\t\t</tr>\n')
            pass
        # SOURCE LINE 20
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


