# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1274959686.8502979
_template_filename='/home/yetty/Work/Development/DevContest/devcontest/templates/admin/user.mako'
_template_uri='admin/user.mako'
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
        # SOURCE LINE 36
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
        __M_writer(u'\n<h2>Po\u0159ad\xed</h2>\n<div >\n    <table class="dark">\n        <thead>\n            <th class="ns"></th>\n            <th>Jm\xe9no</th>\n            <th>T\u0159\xedda</th>\n        </thead>\n    ')
        # SOURCE LINE 14
        i = -1 
        
        __M_writer(u'\n')
        # SOURCE LINE 15
        for i, b in enumerate(c.users):
            # SOURCE LINE 16
            __M_writer(u'        <tr>\n            <td class="ns">')
            # SOURCE LINE 17
            __M_writer(escape(i+1))
            __M_writer(u'</td>\n            <td>\n')
            # SOURCE LINE 19
            if b.admin:
                # SOURCE LINE 20
                __M_writer(u'\t\t\t\t<img src="/running.gif" alt="is running">\n')
                pass
            # SOURCE LINE 22
            __M_writer(u'            &nbsp;')
            __M_writer(escape(b.fname + ' ' + b.lname))
            __M_writer(u'</td>\n            <td style="text-align:center;">')
            # SOURCE LINE 23
            __M_writer(escape(b.cls))
            __M_writer(u'</td>\n\t\t\t<td class="ns"><a href=')
            # SOURCE LINE 24
            __M_writer(escape(h.url_for(id="edit", param=b.id)))
            __M_writer(u'><img src="/edit.png" alt="e"></a></td>\n\t\t\t<td class="ns"><a href="#" ondblclick=\'remove("')
            # SOURCE LINE 25
            __M_writer(escape(h.url_for(id="remove", param=b.id)))
            __M_writer(u'");\'><img src="/remove.png" alt="e"></a></td>\n        </tr>\n')
            pass
        # SOURCE LINE 28
        if i<0:
            # SOURCE LINE 29
            __M_writer(u'    <tr>\n\t\t<td class="ns"></td>\n\t\t<td class="ns info" colspan=3>Nikdo?</td>\n\t</tr>\n')
            pass
        # SOURCE LINE 34
        __M_writer(u'    </table>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Po\u0159ad\xed')
        return ''
    finally:
        context.caller_stack._pop_frame()


