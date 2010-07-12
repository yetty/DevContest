# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1273866593.317647
_template_filename=u'/home/yetty/Work/Development/DevContest/devcontest/templates/edit.mako'
_template_uri=u'/edit.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<script src="/edit_area/edit_area_full.js"  language="Javascript" type="text/javascript"></script>\n<script src="/my.js"  language="Javascript" type="text/javascript"></script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


