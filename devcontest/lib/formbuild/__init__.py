# -*- coding: utf-8 -*-

"""\

FormBuild 2.0 is a complete re-write of FormBuild 0.1 with a vastly simplified
API focusing on the core use case and with automatic variable escaping< built in
to help prevent XSS attacks. The new API supports all the features of the old
one but is easier to understand.

There is no support for default values. To handle default values you should pass
the values you want to use as defaults as the argument to Form() for the case
where the defaults should be displayed.
"""

#? Maybe use the terminology of form template for forms?

import warnings
import helpers
import webhelpers.html.tags
from webhelpers.html.builder import HTML, literal

# Deprecated but needed for backwards compatibility with the Pylons Book.
from helpers import *
from webhelpers.html.tags import *

import logging
log = logging.getLogger(__name__)

class LayoutHelpers:

    def __init__(self, table_class='formbuild'):
        self.table_class = table_class

    def start(self, url, method="post", multipart=False, **attrs):
        return helpers.start_form(url, method, multipart, **attrs)
    start.__doc__ = helpers.start_form.__doc__

    def end(self):
        return end_form()
    end.__doc__ = helpers.end_form.__doc__

    def start_layout(self, table_class=None):
        return helpers.start_layout(table_class or self.table_class)
    start_layout.__doc__ = helpers.start_layout.__doc__

    def end_layout(self):
        return helpers.end_layout()
    end_layout.__doc__ = helpers.end_layout.__doc__

    def start_with_layout(self, url, method="post", multipart=False, table_class=None, **attrs):
        return helpers.start_with_layout(url, method, multipart, table_class or self.table_class, **attrs)
    start_with_layout.__doc__ = helpers.start_with_layout.__doc__

    def end_with_layout(self):
        return helpers.end_with_layout()
    end_with_layout.__doc__ = helpers.end_with_layout.__doc__

    def action_bar(self, fields):
        """\
        Generate an action bar containing submit buttons from the list of fields
        """
        return literal('<tr><td></td><td colspan="2">')+literal('').join(fields)+literal('</td></tr>')

    def hidden_fields(self, *fields):
        output = [literal('<tr><td></td><td colspan="2">')]
        output.append(literal('</td></tr>'))
        for field in fields:
            output.append(webhelpers.html.tags.hidden(field, value=self.values[field]))
        return literal('').join(output)

    def title(self, content, escape=False):
        if escape:
            content = literal(content)
        return literal('<tr><td colspan="3">')+content+literal('</td></tr>')

class FieldHelper:
    def field(
        self,
        label='',
        field='',
        required=False,
        label_desc='',
        field_desc='',
        help='',
        error='',
        name=None,
        field_pre='',
        field_extra='',
    ):
        """\
	Generate a field row in the form but use the dictionary of arguments
        passed as the ``field`` argument to build the field itself, replacing the field
        value and the error message as appropriate.

        The following will be checked in order of preference when determining the value to
        use:

        1. The value corresponding to a ``value`` key in the dictionary passed as the ``field`` argument.
        2. A suitable value passed as an argument to the constructor as the ``defualts`` argument
        For choosing error messages, the ``error`` argument passed as an argument to this method is used if it exists, otherwise any error message passed to the class itself is used.
        """
        if isinstance(field, dict):
            if field.has_key('default'):
                raise Exception("FormBuild no longer supports direct defaults, set some values instead")
            for arg in ['name', 'type']:
                if not field.has_key(arg):
                    raise Exception('No %r key passed in the "field" argument'%arg)
            type = field['type']
            del field['type']
            if not hasattr(self, type):
                raise Exception('No such field %r associated with this form'%type)
            name = field['name']
            if type in ['checkbox_group', 'radio_group', 'combo', 'dropdown']:
                selected_values = []
                if field.has_key('value'):
                    raise Exception("%s fields take a 'selected_values' argument, not a 'value' argument"%type)
                if field.has_key('selected_values'):
                    selected_values = field['selected_values']
                elif self.values.has_key(name):
                    selected_values = self.values.get(name)
                field['selected_values'] = selected_values
                if field.has_key('options'):
                    field['options'] = self.options[name]
                elif self.options.has_key(name):
                    field['options'] = self.options[name]
                else:
                    require_options = field.get('require_options')
                    if require_options is None:
                        # Just don't set any options
                        log.warning('No options were specified for the checkbox group %r', name)
                        del field['require_options']
                        field['options'] = []
                    # Use == in case someone sets to 0
                    elif require_options == True:
                        raise Exception('No options were specified for the checkbox group %r' % name)
                    else:
                        field['options'] = []
                        del field['require_options']
                if field.has_key('require_options'):
                    del field['require_options']
            else:
                value = None
                if field.has_key('value'):
                    value = field['value']
                elif self.values.has_key(name):
                    value = self.values.get(name)
                field['value'] = value
            field_html = getattr(self, type)(**field)
            error_html = error or self.errors.get(name)
        else:
            # Handling it explicitly with no errors:
            # XXX Should raise a warning?
            field_html = field
            error_html = error or self.errors.get(name)
        return helpers.field(
            label=label,
            field=field_html+field_extra,
            required=required,
            label_desc=label_desc,
            field_desc=field_desc,
            help=help,
            error=error_html,
            field_pre=field_pre,
        )

class BaseForm:
    def __init__(self, values=None, errors=None, state=None, options=None):
        if values is None:
            self.values = {}
        else:
            self.values = values
        if errors is None:
            self.errors = {}
        else:
            self.errors = errors
        if options is None:
            self.options = {}
        else:
            self.options = options
        self.state = state


class SingleValueFields:
    """\
    These are methods which represent helpers which take single value arguments. When called
    directly they will take the ``value`` argument passed to them or the default from the Form
    class constructor.
    """

    def file(self, name, value=None, id=None, **options):
        if value is None:
            value = self.values.get(name)
        return webhelpers.html.tags.file(name, value=value, id=id, **options)

    def password(self, name="password", value=None, id=None, **options):
        """Creates a password field
           Takes the same options as text"""
        if value is None:
            value = self.values.get(name)
        return webhelpers.html.tags.password(name, value, id=id, **options)

    def textarea(self, name, value=None, id=None, rows=3, cols=16, **options):
        """Creates a text input area"""
        if value is None:
            value = self.values.get(name)
        return webhelpers.html.tags.textarea(name, content=value, id=id, rows=rows, cols=cols, **options)

    def checkbox(self, name, value=None, checked=False, id=None, **options):
        """Creates a check box."""
        if value is None:
            value = self.values.get(name)
        elif value == self.values.get(name) or self.values.get(name) == True:
            checked=True
        return webhelpers.html.tags.checkbox(name, value=value, checked=checked, id=id, **options)

    def radio(self, name, value, checked=False, id=None, **options):
        """Creates a radio button."""
        return webhelpers.html.tags.radio(name, value, checked, id=id, **options)

    def image_button(self, name='commit', value="", id=None, **options):
        """\
        Creates an image button with the text ``<tt>value</tt>`` as the
        caption.
        """
        if value is None:
            value = self.values.get(name)
        return image_button(value=value, name=name, id=id, **options)

    def submit(self, name='commit', value="", id=None, **options):
        """\
        Creates a submit button with the text ``<tt>value</tt>`` as the
        caption.
        """
        if value is None:
            value = self.values.get(name)
        return webhelpers.html.tags.submit(value=value, name=name, id=id, **options)

    def dropdown(self, name, options, value=None, id=None, **attrs):
        if value is None:
            value = self.values.get(name)
        if value is None and not attrs.has_key('selected_values'):
            attrs['selected_values']=[value]
        return webhelpers.html.tags.select(name, options=options, id=id, **attrs)

    def text(self, name, value=None, id=None, **options):
        if value is None:
            value = self.values.get(name)
        return webhelpers.html.tags.text(name, value, id=id, **options)

    def hidden(self, name, value=None, id=None, **options):
        if value is None:
            value = self.values.get(name)
        return webhelpers.html.tags.hidden(name, value, id=id, **options)

    def radio_group(self, name, options, value=None, align='horiz', cols=4):
        if value is None:
            value = self.values.get(name)
        #if value is None:
        #    selected_values = []
        #else:
        #    selected_values = [value]
        #return helpers.radio_group(name, value=selected_values, options=options, align=align, cols=cols)
        return helpers.radio_group(name, value=value, options=options, align=align, cols=cols)

    def static(self, name, value=None):
        """
        Return the static value instead of an HTML field.
        """
        if value is None:
            value = self.values.get(name)
        return str(value)

    #
    # Deprecated Methods
    #

    def text_area(self, name, value=None, id=None, **options):
        warnings.warn(
            "text_area() is deprecated, use textarea() instead",
            DeprecationWarning, stacklevel=2
        )
        return self.textarea(name, value=value, id=id, **options)

    def check_box(self, name, value=None, id=None, **options):
        warnings.warn(
            "check_box() is deprecated, use checkbox() instead",
            DeprecationWarning, stacklevel=2
        )
        return self.checkbox(name, value=value, id=id, **options)

    def radio_button(self, name, value=None, id=None, **options):
        warnings.warn(
            "radio_button() is deprecated, use radio() instead",
            DeprecationWarning, stacklevel=2
        )
        return self.radio(name, value=value, id=id, **options)

    def date(self, *k, **p):
        warnings.warn(
            "date() is deprecated, use text() instead, they are the same",
            DeprecationWarning, stacklevel=2
        )
        return self.text(*k, **p)


    #
    # Removed
    #

    def select(self, name, option_tags='', id=None, **options):
        raise Exception('select() has been deprecated for over a year and is now removed. Please use dropdown() or combo() instead')
        # XXX Should distinguish between single and combo and take different values
        warnings.warn(
            "formbuild.builder.field.basic.select has been deprecated; please "
            "use formbuild.builder.field.basic.dropdown instead.",
            DeprecationWarning, 2
        )
        return select(name, option_tags, id=id, **options)

class MultipleValueFields:
    """\
    These are methods which represent helpers which take multiple value arguments. When called
    directly they will take the ``value`` argument passed to them or the default from the Form
    class constructor.
    """
    def combo(self, name, options=None, selected_values=None, id=None, size=4, **attrs):
        if selected_values is None:
            selected_values = self.values.get(name)
        if options is None:
            options = self.options.get(name)
        return webhelpers.html.tags.select(name, selected_values=selected_values, options=options, size=size, multiple=True, id=id, **attrs)

    def checkbox_group(self, name, options=None, selected_values=None, align='horiz', cols=4, sub_name=None):
        if selected_values is None:
            if sub_name:
                selected_values = []
                for k, v in self.values.items():
                    if k.startswith(name+'.') or k.startswith(name+'['):
                        selected_values.append(v)
            else:
                selected_values = self.values.get(name)
        if options is None:
            options = self.options.get(name)
        return checkbox_group(name, selected_values=selected_values, options=options, align=align, cols=cols, sub_name=sub_name)

    def radio_group(self, name, options, selected_values=None, align='horiz', cols=4, sub_name=None):
        if selected_values is None:
            selected_values = self.values.get(name)
        return radio_group(name, selected_values=selected_values, options=options, align=align, cols=cols, sub_name=sub_name)

class Form(BaseForm, FieldHelper, LayoutHelpers, SingleValueFields, MultipleValueFields):
    def __init__(self, values=None, errors=None, state=None, table_class='formbuild', options=None):
        BaseForm.__init__(self, values=values, errors=errors, state=state, options=options)
        LayoutHelpers.__init__(self, table_class=table_class)

#def handle(schema, template, form=None, data=None, params=None, context=None, render_response=None, fragment=False):
#    if data == None:
#        data = {}
#    else:
#        if not isinstance(data, dict):
#            raise TypeError('Expected data to be a dictionary')
#            #~ values = {}
#            #~ for k in data.c.keys():
#                #~ values[k] = getattr(data, k)
#            #~ data = values
#    import formencode
#    if params == None:
#        from pylons import request
#        params = {}
#        for k in request.params.keys():
#            v = request.params.getall(k)
#            if len(v) == 1:
#                params[k] = v[0]
#            else:
#                params[k] = v
#    if context == None:
#        from pylons import c as context
#    if not form:
#        form = Form
#    if not render_response:
#        from pylons.templating import render_response
#    c = context
#    errors = {}
#    data.update(params)
#    results=data
#    if len(params):
#        try:
#            results = schema.to_python(results, state=c)
#        except formencode.Invalid, e:
#            errors = e.error_dict or {}
#    c.form = form(results, errors)
#    if not len(params) or errors:
#        return results, errors, render_response(template, fragment=fragment)
#    return results, errors, ''

class ValidationException(Exception):
    pass

def errors_to_dict(exception, allow_empty_keys=False):
    log.info('Converting errors %r', exception)
    import formencode.variabledecode
    errors = exception.unpack_errors() or {}
    if not allow_empty_keys:
        if not isinstance(errors, dict):
            raise ValidationException(errors)
        for k, v in errors.items():
            if not k:
                raise ValidationException(v)
    return formencode.variabledecode.variable_encode(errors)

def values_to_dict(result):
    log.info('Converting values %r', result)
    import formencode.variabledecode
    return formencode.variabledecode.variable_encode(result)

def params_to_dict(params):
    result = {}
    for k in params.keys():
        v = params.getall(k)
        if len(v) == 1:
            result[k] = v[0]
        else:
            result[k] = v
    return result

class FormEncodeState(object):
    pass

class ValidationState(object):
    """
    Wraps a PowerPack state so that attribute FormEncode needs can still be
    set. Also provides a .validation_state attribute for setting per
    instance attributes on.
    """

    def __init__(self, state=None, key='validation'):
        if state is not None:
            self.__dict__['_state'] = state
        self.__dict__['_formencode_state'] = FormEncodeState()
        self.__dict__['validation_state'] = FormEncodeState()

    def __setattr__(self, name, value):
        if name in ['full_list', 'full_dict', 'key', 'index', 'validation_state']:
            setattr(self.__dict__['_formencode_state'], name, value)
        else:
            setattr(self.__dict__['_state'], name, value)

    def __getattr__(self, name):
        if name in ['full_dict', 'key']:
            return getattr(self.__dict__['_formencode_state'], name)
        else:
            return getattr(self.__dict__['_state'], name)
