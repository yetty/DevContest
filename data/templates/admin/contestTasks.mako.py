# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1273948732.382642
_template_filename='/home/yetty/Work/Development/DevContest/devcontest/templates/admin/contestTasks.mako'
_template_uri='/admin/contestTasks.mako'
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
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n\t<h2>Seznam ot\xe1zek</h2>\n\t<table class="dark">\n')
        # SOURCE LINE 8
        for task in c.list:
            # SOURCE LINE 9
            __M_writer(u'\t\t\t<tr>\n\t\t\t\t<td>')
            # SOURCE LINE 10
            __M_writer(escape(task.name))
            __M_writer(u'</td>\n\t\t\t\t<td class="ns"><a href=')
            # SOURCE LINE 11
            __M_writer(escape(h.url_for(action="task", id=task.id)))
            __M_writer(u'><img src="/edit.png" alt="e"></a></td>\n\t\t\t\t<td class="ns"><a href="#" ondblclick=\'remove("')
            # SOURCE LINE 12
            __M_writer(escape(h.url_for(action="task", id=task.id, param="remove")))
            __M_writer(u'");\'><img src="/remove.png" alt="e"></a></td>\n\t\t\t</tr>\n')
            pass
        # SOURCE LINE 15
        __M_writer(u'\t</table>\n\t<hr>\n\t ')
        # SOURCE LINE 17
        __M_writer(escape(h.form_start(h.url_for(param="create_task"), method="post")))
        __M_writer(u'\n\t ')
        # SOURCE LINE 18
        __M_writer(escape(h.field("Název úkolu", h.text(name="name"))))
        __M_writer(u'\n\t ')
        # SOURCE LINE 19
        __M_writer(escape(h.field("", h.submit("submit", "Vytvořit"))))
        __M_writer(u'\n\t ')
        # SOURCE LINE 20
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
        __M_writer(u'Seznam ot\xe1zek')
        return ''
    finally:
        context.caller_stack._pop_frame()


