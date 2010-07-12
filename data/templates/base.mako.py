# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1278950440.1073771
_template_filename=u'/home/yetty/Work/Development/DevContest/devcontest/templates/base.mako'
_template_uri=u'/base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.Namespace(u'menu', context._clean_inheritance_tokens(), templateuri=u'/menu.mako', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'menu')] = ns

    # SOURCE LINE 2
    ns = runtime.Namespace(u'login', context._clean_inheritance_tokens(), templateuri=u'/login.mako', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'login')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        next = context.get('next', UNDEFINED)
        session = context.get('session', UNDEFINED)
        menu = _mako_get_namespace(context, 'menu')
        login = _mako_get_namespace(context, 'login')
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'')
        # SOURCE LINE 2
        __M_writer(u'')
        # SOURCE LINE 3
        __M_writer(u'<html>\n<head>\n    <meta http-equiv="content-type" content="text/html; charset=utf-8" />\n    <title>')
        # SOURCE LINE 6
        __M_writer(escape(_('DevContest')))
        __M_writer(u' - ')
        __M_writer(escape(next.title()))
        __M_writer(u'</title>\n    <link rel="shortcut icon" href="/icon.png">\n    ')
        # SOURCE LINE 8
        __M_writer(escape(h.stylesheet_link("/style.css")))
        __M_writer(u'\n    ')
        # SOURCE LINE 9
        __M_writer(escape(h.stylesheet_link("/highlighter.css")))
        __M_writer(u'\n</head>\n<body>\n<script language="Javascript" type="text/javascript">\nfunction remove(url) {\n\twindow.location.href = url;\n}\n</script>\n\n')
        # SOURCE LINE 18
        if session.get('flash'):
            # SOURCE LINE 19
            __M_writer(u'    <div id="flash">\n        ')
            # SOURCE LINE 20
            __M_writer(escape(session.get('flash')))
            __M_writer(u'\n    ')
            # SOURCE LINE 21

            del session['flash']
            session.save()
                
            
            # SOURCE LINE 24
            __M_writer(u'\n    </div>\n\n')
            # SOURCE LINE 27
        elif session.get('error_flash'):
            # SOURCE LINE 28
            __M_writer(u'    <div id="error">\n        ')
            # SOURCE LINE 29
            __M_writer(escape(session.get('error_flash')))
            __M_writer(u'\n    ')
            # SOURCE LINE 30

            del session['error_flash']
            session.save()
                
            
            # SOURCE LINE 33
            __M_writer(u'\n     </div>\n')
            pass
        # SOURCE LINE 36
        __M_writer(u'\n    <div id="header">\n    <h1><a href=')
        # SOURCE LINE 38
        __M_writer(escape(h.url_for(controller="home", action="index")))
        __M_writer(u'>')
        __M_writer(escape(_('DevContest')))
        __M_writer(u'</a></h1>\n    </div>\n    <div id="left_nav">\n    <div id="menu">\n        ')
        # SOURCE LINE 42
        __M_writer(escape(menu.menu()))
        __M_writer(u'\n    </div>\n\n    <div id="login_box">\n        ')
        # SOURCE LINE 46
        __M_writer(escape(login.login_box()))
        __M_writer(u'\n    </div>\n    <br/>\n    <a href="http://python.org" alt="Python"><img src="/python-powered-w-70x28.png" alt="')
        # SOURCE LINE 49
        __M_writer(escape(_('Python powered')))
        __M_writer(u'"/></a>\n    </div>\n\n    <div id="content">\n        ')
        # SOURCE LINE 53
        __M_writer(escape(next.body()))
        __M_writer(u'\n    </div>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


