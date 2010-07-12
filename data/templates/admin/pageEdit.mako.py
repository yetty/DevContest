# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1273867725.859966
_template_filename='/home/yetty/Work/Development/DevContest/devcontest/templates/admin/pageEdit.mako'
_template_uri='admin/pageEdit.mako'
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
        # SOURCE LINE 15
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
        __M_writer(u'\n')
        # SOURCE LINE 6
        if c.lang:
            # SOURCE LINE 7
            __M_writer(u'\t\t<script type="text/javascript">var LANG="')
            __M_writer(escape(c.lang))
            __M_writer(u'";</script>\n\t\t')
            # SOURCE LINE 8
            runtime._include_file(context, u'/edit.mako', _template_uri)
            __M_writer(u'\n')
            pass
        # SOURCE LINE 10
        __M_writer(u'\t<h2>Editace str\xe1nky ')
        __M_writer(escape(c.name))
        __M_writer(u'</h2>\n\t')
        # SOURCE LINE 11
        __M_writer(escape(h.form_start(h.url_for(id=c.name, param="save"), method="post")))
        __M_writer(u'\n\t')
        # SOURCE LINE 12
        __M_writer(escape(h.textarea(name="area", content=c.content, rows=30, cols=100)))
        __M_writer(u'\n\t')
        # SOURCE LINE 13
        __M_writer(escape(h.submit("submit", "Odeslat")))
        __M_writer(u'\n\t')
        # SOURCE LINE 14
        __M_writer(escape(h.form_end()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Editace str\xe1nky ')
        __M_writer(escape(c.name))
        return ''
    finally:
        context.caller_stack._pop_frame()


