# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1275074455.525445
_template_filename='/home/yetty/Work/Development/DevContest/devcontest/templates/task.mako'
_template_uri='task.mako'
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
        # SOURCE LINE 45
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n\t<a href=')
        # SOURCE LINE 6
        __M_writer(escape(h.url_for(controller="contest", action="tasks", id=c.task.contest_id)))
        __M_writer(u' class="back">zp\u011bt na sout\u011b\u017e</a>\n\t<h2>')
        # SOURCE LINE 7
        __M_writer(escape(c.task.name))
        __M_writer(u'</h2>\n\t')
        # SOURCE LINE 8
        __M_writer(c.task.description )
        __M_writer(u'\n\n\t<hr style="visibility:hidden;">\n\n\t<div id="example_in"><h3>P\u0159\xedklad vstupu:</h3><pre>')
        # SOURCE LINE 12
        __M_writer(escape(c.task.example_in))
        __M_writer(u'</pre></div>\n\t<div id="example_out"><h3>P\u0159\xedklad v\xfdstupu:</h3><pre>')
        # SOURCE LINE 13
        __M_writer(escape(c.task.example_out))
        __M_writer(u'</pre></div>\n')
        # SOURCE LINE 14

        from devcontest.model import Contest
        from devcontest.model.meta import Session
        
        
        # SOURCE LINE 17
        __M_writer(u'\n')
        # SOURCE LINE 18
        if Session.query(Contest.is_running).filter_by(id=c.task.contest_id).first()[0]:
            # SOURCE LINE 19
            __M_writer(u'\t<hr>\n')
            # SOURCE LINE 20
            if not c.status or request.environ.get('REMOTE_USER').admin:
                # SOURCE LINE 21
                __M_writer(u'\t ')
                __M_writer(escape(h.form_start(h.url_for(param="upload"), method="post", multipart=True)))
                __M_writer(u'\n\t ')
                # SOURCE LINE 22
                __M_writer(escape(h.field("Zdroják", h.file(name="source"))))
                __M_writer(u'\n\t ')
                # SOURCE LINE 23
                __M_writer(escape(h.field("", h.submit("submit", "Nahrát"))))
                __M_writer(u'\n\t ')
                # SOURCE LINE 24
                __M_writer(escape(h.form_end()))
                __M_writer(u'\n')
                pass
            # SOURCE LINE 26
            if c.status:
                # SOURCE LINE 27
                __M_writer(u'\t\t<div class="success">\xdaloha vy\u0159e\u0161ena</div>\n')
                pass
            # SOURCE LINE 29
            __M_writer(u'\n')
            # SOURCE LINE 30
            if c.source:
                # SOURCE LINE 31
                __M_writer(u'\t<h3>Posledn\xed verze</h3>\n\t')
                # SOURCE LINE 32

                from pygments import highlight
                from pygments.lexers import guess_lexer
                from pygments.formatters import HtmlFormatter
                
                
                # SOURCE LINE 36
                __M_writer(u'\n')
                # SOURCE LINE 37
                if c.source.errors:
                    # SOURCE LINE 38
                    __M_writer(u'\t<pre>')
                    __M_writer(escape(c.source.errors))
                    __M_writer(u'</pre>\n')
                    pass
                # SOURCE LINE 40
                __M_writer(u'\n\t')
                # SOURCE LINE 41
                __M_writer(highlight(c.source.source, guess_lexer(c.source.source), HtmlFormatter(linenos=True)) )
                __M_writer(u'\n\n')
                pass
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(escape(c.task.name))
        return ''
    finally:
        context.caller_stack._pop_frame()


