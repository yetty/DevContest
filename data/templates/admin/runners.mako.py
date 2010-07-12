# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1274199379.5988541
_template_filename='/home/yetty/Work/Development/DevContest/devcontest/templates/admin/runners.mako'
_template_uri='/admin/runners.mako'
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
        # SOURCE LINE 28
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
        __M_writer(u'\n\t<script type="text/javascript">var LANG="html";</script>\n\t<h2>Nastaven\xed spou\u0161t\u011b\u010d\u016f a kompil\xe1tor\u016f</h2>\n\n\t<table class="dark">\n')
        # SOURCE LINE 10
        for item in c.list:
            # SOURCE LINE 11
            __M_writer(u'\t\t\t<tr>\n\t\t\t\t<td class="ns">')
            # SOURCE LINE 12
            __M_writer(escape(item.id))
            __M_writer(u'</td>\n\t\t\t\t<td>')
            # SOURCE LINE 13
            __M_writer(escape(item.lang))
            __M_writer(u'</td>\n\t\t\t\t<td>')
            # SOURCE LINE 14
            __M_writer(escape(item.compile))
            __M_writer(u'</td>\n\t\t\t\t<td>')
            # SOURCE LINE 15
            __M_writer(escape(item.run))
            __M_writer(u'</td>\n\t\t\t\t<td class="ns"><a href="#" ondblclick=\'remove("')
            # SOURCE LINE 16
            __M_writer(escape(h.url_for(id=item.id, param="remove")))
            __M_writer(u'");\'><img src="/remove.png" alt="e"></a></td>\n\t\t\t</tr>\n')
            pass
        # SOURCE LINE 19
        __M_writer(u'\t</table>\n\t<hr>\n\t ')
        # SOURCE LINE 21
        __M_writer(escape(h.form_start(h.url_for(id="save", param=None), method="post")))
        __M_writer(u'\n\t ')
        # SOURCE LINE 22
        __M_writer(escape(h.field("Jazyk (přípona)", h.text(name="lang"))))
        __M_writer(u'\n\t ')
        # SOURCE LINE 23
        __M_writer(escape(h.field("Kompilátor", h.text(name="compile", size=50))))
        __M_writer(u'\n\t ')
        # SOURCE LINE 24
        __M_writer(escape(h.field("Spouštěč", h.text(name="run", size=50))))
        __M_writer(u'\n\t ')
        # SOURCE LINE 25
        __M_writer(escape(h.field("", h.submit("submit", "Vytvořit"))))
        __M_writer(u'\n\t <p class="info" style="float:right;"><br>%f pro vstup<br>%o pro v\xfdstup</p>\n\t ')
        # SOURCE LINE 27
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
        __M_writer(u'Nastaven\xed spou\u0161t\u011b\u010d\u016f a kompil\xe1tor\u016f')
        return ''
    finally:
        context.caller_stack._pop_frame()


