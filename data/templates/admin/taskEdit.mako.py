# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1275072836.4955299
_template_filename='/home/yetty/Work/Development/DevContest/devcontest/templates/admin/taskEdit.mako'
_template_uri='/admin/taskEdit.mako'
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
        # SOURCE LINE 74
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
        __M_writer(u'\n\t<script type="text/javascript">var LANG="html";</script>\n\t<a href=')
        # SOURCE LINE 7
        __M_writer(escape(h.url_for(controller="admin", action="contest", id=c.contest_id, param=None)))
        __M_writer(u' class="back">zp\u011bt na sout\u011b\u017e</a>\n\t<h2>')
        # SOURCE LINE 8
        __M_writer(escape(c.name))
        __M_writer(u'</h2>\n\t')
        # SOURCE LINE 9
        __M_writer(escape(h.form_start(h.url_for(id=c.id, param="save"), method="post")))
        __M_writer(u'\n\t')
        # SOURCE LINE 10
        __M_writer(escape(h.textarea(name="description", content=c.description, rows=20, cols=114)))
        __M_writer(u'\n\t')
        # SOURCE LINE 11
        __M_writer(escape(h.submit("submit", "Odeslat")))
        __M_writer(u'\n\t<table>\n\t\t<tr>\n\t\t\t<td class="strong">\n\t\t\tP\u0159\xedklad vstupu:\n\t\t\t</td>\n\t\t\t<td class="strong">\n\t\t\tP\u0159\xedklad v\xfdstupu:\n\t\t\t</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td class="strong">\n\t\t\t')
        # SOURCE LINE 23
        __M_writer(escape(h.textarea(name="example_in", id="", content=c.example_in, rows=15, cols=55)))
        __M_writer(u'\n\t\t\t</td>\n\t\t\t<td class="strong">\n\t\t\t')
        # SOURCE LINE 26
        __M_writer(escape(h.textarea(name="example_out", id="", content=c.example_out, rows=15, cols=55)))
        __M_writer(u'\n\t\t\t</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td class="strong">\n\t\t\tSkript pro vstup:\n\t\t\t</td>\n\t\t\t<td class="strong">\n\t\t\tZpracov\xe1n\xed:\n\t\t\t</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t\t\t<!-- lang="python" -->\n\t\t\t<td>\n\t\t\t<textarea name="data_in" id="data_in" rows=20 cols=55>')
        # SOURCE LINE 40
        __M_writer(escape(c.data_in))
        __M_writer(u'</textarea>\n\t\t\t</td>\n\t\t\t<td>\n\t\t\t<textarea name="data_out" id="data_out" rows=20 cols=55>')
        # SOURCE LINE 43
        __M_writer(escape(c.data_out))
        __M_writer(u'</textarea>\n\t\t\t</td>\n\t\t</tr>\n\t\t<tr><td colspan=2>')
        # SOURCE LINE 46
        __M_writer(escape(h.submit("submit", "Odeslat")))
        __M_writer(u'</td></tr>\n\t\t<tr>\n\t\t\t<td class="strong">\n\t\t\tAktu\xe1ln\xed vstup:\n\t\t\t</td>\n\t\t\t<td class="strong">\n\t\t\tAktu\xe1ln\xed v\xfdstup:\n\t\t\t</td>\n\t\t</tr>\n\t\t<tr>\n\t\t\t<td>\n\t\t\t\tstatus: ')
        # SOURCE LINE 57
        __M_writer(escape(c.run_in["status"]))
        __M_writer(u'<br>\n\t\t\t\tv\xfdstup:</br>\n\t\t\t\t<pre style="width: 350px;" wrap=hard>')
        # SOURCE LINE 59
        __M_writer(escape(c.run_in["return"]))
        __M_writer(u'</pre>\n\t\t\t\tchyby:</br>\n\t\t\t\t<pre style="width: 350px;" wrap=hard>')
        # SOURCE LINE 61
        __M_writer(escape(c.run_in["errors"]))
        __M_writer(u'</pre>\n\t\t\t</td>\n\t\t\t<td>\n\t\t\t\tstatus: ')
        # SOURCE LINE 64
        __M_writer(escape(c.run_out["status"]))
        __M_writer(u'<br>\n\t\t\t\tv\xfdstup:</br>\n\t\t\t\t<pre style="width: 350px;" wrap=hard>')
        # SOURCE LINE 66
        __M_writer(escape(c.run_out["return"]))
        __M_writer(u'</pre>\n\t\t\t\tchyby:</br>\n\t\t\t\t<pre style="width: 350px;" wrap=hard>')
        # SOURCE LINE 68
        __M_writer(escape(c.run_out["errors"]))
        __M_writer(u'</pre>\n\t\t\t</td>\n\t\t</tr>\n\t</table>\n\t')
        # SOURCE LINE 72
        __M_writer(escape(h.form_end()))
        __M_writer(u'\n\t')
        # SOURCE LINE 73
        runtime._include_file(context, u'/edit.mako', _template_uri)
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


