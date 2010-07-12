# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1278950469.070745
_template_filename='/home/yetty/Work/Development/DevContest/devcontest/templates/top.mako'
_template_uri='top.mako'
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
        # SOURCE LINE 33
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        _ = context.get('_', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(u'\n<h2>')
        # SOURCE LINE 6
        __M_writer(escape(_('Ranking')))
        __M_writer(u'</h2>\n<div >\n    <table class="dark">\n        <thead>\n            <th class="ns"></th>\n            <th>')
        # SOURCE LINE 11
        __M_writer(escape(_('Name')))
        __M_writer(u'</th>\n            <th>')
        # SOURCE LINE 12
        __M_writer(escape(_('Class')))
        __M_writer(u'</th>\n            <th>')
        # SOURCE LINE 13
        __M_writer(escape(_('Count')))
        __M_writer(u'</th>\n        </thead>\n    ')
        # SOURCE LINE 15
        i = -1 
        
        __M_writer(u'\n')
        # SOURCE LINE 16
        for i, b in enumerate(c.users):
            # SOURCE LINE 17
            __M_writer(u'        <tr>\n            <td class="ns">')
            # SOURCE LINE 18
            __M_writer(escape(i+1))
            __M_writer(u'</td>\n            <td>&nbsp;')
            # SOURCE LINE 19
            __M_writer(escape(b['user'].fname + ' ' + b['user'].lname))
            __M_writer(u'</td>\n            <td style="text-align:center;">')
            # SOURCE LINE 20
            __M_writer(escape(b['user'].cls))
            __M_writer(u'</td>\n            <td style="text-align:center;">')
            # SOURCE LINE 21
            __M_writer(escape(b['count']))
            __M_writer(u'</td>\n        </tr>\n')
            pass
        # SOURCE LINE 24
        if i<0:
            # SOURCE LINE 25
            __M_writer(u'    <tr>\n\t\t<td class="ns"></td>\n\t\t<td class="ns info" colspan=3>')
            # SOURCE LINE 27
            __M_writer(escape(_('Nobody?')))
            __M_writer(u'</td>\n\t</tr>\n')
            pass
        # SOURCE LINE 30
        __M_writer(u'    </table>\n    </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(escape(_('Ranking')))
        return ''
    finally:
        context.caller_stack._pop_frame()


