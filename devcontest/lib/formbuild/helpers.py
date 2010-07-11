"""\
Functions to help in the formatting of forms.

Author: James Gardner
"""

from webhelpers.html.tags import form as start_form, end_form
from webhelpers.html import HTML, literal

def start_with_layout(url, method="post", multipart=False, table_class=None, **attrs):
    """\
    Start a form the way you would with ``start_form()`` but include the HTML
    necessary for the use of the ``fields()`` helper. 
    
    >>> start_with_layout('/action', method='post')
    literal(u'<form action="/action" method="post"><table>')
    >>> start_with_layout('/action', method='post', table_class='form')
    literal(u'<form action="/action" method="post"><table class="form">')
    """
    if table_class:
         return start_form(url, method, multipart, **attrs)+HTML.table(
             _closed=False, 
             class_=table_class,
         )
    else:
         return start_form(url, method, multipart, **attrs)+literal('<table>')

def end_with_layout():
    """\
    End a form started with ``start_with_layout()``
    >>> end_with_layout()
    literal(u'</table></form>')
    """
    return literal("</table>")+end_form()

def start_layout(table_class=None):
    """\
    Start a layout without adding the form tag
    >>> start_layout()
    literal(u'<table>')
    >>> start_layout(table_class='form')
    literal(u'<table class="form">')
    """
    if table_class is None:
        return HTML.table(
             _closed=False,
        )
    else:
        return HTML.table(
             _closed=False,
             class_=table_class,
        )

def end_layout():
    """\
    End a layout without adding the end form tag
    >>> end_layout()
    literal(u'</table>')
    """
    return literal('</table>')

def field(
    label='', 
    field='',
    required=False, 
    label_desc='', 
    field_desc='',
    help='',
    error='',
    field_pre='',
):
    """\
    Format a field with a label. 

    ``label``
        The label for the field

    ``field``
        The HTML representing the field, wrapped in ``literal()``

    ``required``
         Can be ``True`` or ``False`` depending on whether the label should be 
         formatted as required or not. By default required fields have an
         asterix.

    ``label_desc``
        Any text to appear underneath the label, level with ``field_desc`` 

    ``field_desc``
        Any text to appear underneath the field

    ``help``
        Any HTML or JavaScript to appear imediately to the right of the field 
        which could be used to implement a help system on the form

    ``error``
        Any text to appear immediately before the HTML field, usually used for
        an error message.

        It should be noted that when used with FormEncode's ``htmlfill`` module, 
        errors appear immediately before the HTML field in the position of the
        ``error`` argument. No ``<form:error>`` tags are added automatically by
        this helper because errors are placed there anyway and adding the tags
        would lead to this helper generating invalid HTML.

    ``field_pre``
        Any HTML to appear immediately above the field.

    TIP: For future compatibility, always specify arguments explicitly and do
    not rely on their order in the function definition.

    Here are some examples:

    >>> print field('email >', literal('<input type="text" name="test" value="" />'), required=True)
    <tr class="field">
    <td class="label" valign="top"><span class="required">*</span><label>email &gt;:</label></td>
    <td class="field" colspan="2" valign="top"><input type="text" name="test" value="" /></td>
    </tr>
    >>> print field(
    ...     label='email >',
    ...     field=literal('<input type="text" name="test" value="" />'), 
    ...     label_desc='including the @ sign',
    ...     field_desc='Please type your email carefully',
    ...     error='This is an error message <br />',
    ...     help = 'No help available for this field',
    ...     required=True,
    ... )
    ...
    <tr class="field">
    <td class="label" valign="top"><span class="required">*</span><label>email &gt;:</label></td>
    <td class="field" valign="top"><div class="error">This is an error message &lt;br /&gt;</div><input type="text" name="test" value="" /></td>
    <td class="help" valign="top">No help available for this field</td>
    </tr>
    <tr class="description">
    <td class="label_desc" valign="top"><span class="small">including the @ sign</span></td>
    <td class="field_desc" colspan="2" valign="top"><span class="small">Please type your email carefully</span></td>
    </tr>

    An appropriate stylesheet to use to style forms generated with field() when
    the table class is specified as "formbuild" would be::

        table.formbuild span.error-message, table.formbuild div.error, table.formbuild span.required {
            font-weight: bold;
            color: #f00;
        }
        table.formbuild span.small {
            font-size: 85%;
        }
        table.formbuild form {
            margin-top: 20px;
        }
        table.formbuild form table td {
            padding-bottom: 3px;
        }

    """
    if error:
        field = HTML.div(class_='error', c=error)+field
    if label:
        label = label + literal(':')
    if field_pre:
        field = HTML.div(c=field_pre) + field
    rows = []
    if required:
        required_html = HTML.span(class_="required", c='*')
    else:
        required_html = HTML.span(style="visibility: hidden", c='*')
    label_html = HTML.td(valign="top", class_="label", c=required_html+HTML.label(c=label))
    if help:
        field_html = HTML.td(valign="top", class_="field", c=field)
        help_html = HTML.td(valign="top", class_="help", c=help)+'\n'
    else:
        field_html = HTML.td(valign="top", class_="field", colspan="2", c=field)
        help_html = ''
    rows.append(HTML.tr(class_='field', c='\n'+label_html+'\n'+field_html+'\n'+help_html))
    if label_desc or field_desc:
        label_desc_html = HTML.td(valign="top", class_="label_desc", c=HTML.span(class_="small", c=label_desc))
        field_desc_html = HTML.td(valign="top", class_="field_desc", colspan="2", c=HTML.span(class_="small", c=field_desc))    
        rows.append(HTML.tr(class_="description", c='\n'+label_desc_html+'\n'+field_desc_html+'\n'))
    return literal('\n').join(rows)

def _format_values(values):
    if not isinstance(values, list) and not isinstance(values, tuple):
        return [unicode(values)]
    else:
        values_ = []
        for value in values:
            values_.append(unicode(value))
        return values_

def _group(name, selected_values, options, group_type, align='horiz', cols=4, sub_name=None):
    if not group_type in ['checkbox','radio']:
        raise Exception('Invalid group type %s'%group_type)
    if len(options):
        counter = 0
        for pair in options:
            if not isinstance(pair, (tuple, list)):
                raise Exception('Expected option item %s to be a list of tuples, not %r' % (counter, pair))
            if not len(pair) == 2:
                raise Exception('Expected option item %s to have be a (value, label) pair, not %r' % (counter, pair))
        counter += 1
    values = _format_values(selected_values)
    output = u''
    item_counter = 0
    actual_name = name
    if len(options) > 0:
        if align <> 'table':
            for option in options:
                if sub_name:
                    actual_name = '%s[%s].%s' % (name, item_counter, sub_name)
                if len(option):
                    v=option[0]
                    k=option[1]
                else:
                    k, v = option, option
                checked=literal(u'')
                if unicode(v) in values:
                    checked=literal(' checked="checked"')
                break_ = u''
                if align == 'vert':
                    break_=literal(u'<br />')
                output+=literal('<input type="')+literal(group_type)+literal('" name="')+actual_name+literal('" value="')+unicode(v)+literal('"')+checked+literal(' /> ')+unicode(k)+break_+literal('\n')
                item_counter += 1
        else:
            output += literal(u'<table border="0" width="100%" cellpadding="0" cellspacing="0">\n    <tr>\n')
            counter = -1
            for option in options:
                counter += 1
                if sub_name:
                    actual_name = '%s[%s].%s' % (name, item_counter, sub_name)
                if ((counter % cols) == 0) and (counter <> 0):
                    output += literal(u'    </tr>\n    <tr>\n')
                output += literal('      <td>')
                checked=literal(u'')
                align=literal(u'')
                if len(option):
                    v=option[0]
                    k=option[1]
                else:
                    k, v = option, option
                if unicode(v) in values:
                    checked=literal(' checked="checked"')
                output+=literal('<input type="')+literal(group_type)+literal('" name="')+actual_name+literal('" value="')+unicode(v)+literal('"')+checked+literal(' /> ')+unicode(k)
                #output += u'<input type="checkbox" name="%s" value="%s"%s />%s%s'%(name, v, checked, k, align)
                item_counter += 1
                output += literal(u'</td>\n      <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>\n')
            counter += 1
            while (counter % cols):
                counter += 1
                output += literal(u'      <td></td>\n      <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>\n')
            output += literal(u'    </tr>\n</table>\n')
    if not type(output) in [unicode, literal]:
        raise Exception('Unexpected output type %r'%type(output))
    return output[:-1]

def radio_group(name, value, options, align='horiz', cols=4, sub_name=None):
    """Radio Group Field.

    ``value``
        The value of the selected option, or ``None`` if no radio button
        is selected

    ``options``
	an iterable of ``(value, label)`` pairs. The value is what's returned to
        the application if this option is chosen; the label is what's shown in the 
        form. You can also pass an iterable of strings in which case the labels will
        be identical to the values.

    ``align``
        can be ``'horiz'`` (default), ``'vert'`` or ``table``. If table layout is 
        chosen then you can also use the ``cols`` argument to specify the number
        of columns in the table, the default is 4.

    Examples (deliberately including some '>' characters to check they are properly escaped)

    >>> print radio_group('fruit', '1', [('1', 'Bananas'), ('2>', 'Apples <>'), ('3', 'Pears')])
    <input type="radio" name="fruit" value="1" checked="checked" /> Bananas
    <input type="radio" name="fruit" value="2&gt;" /> Apples &lt;&gt;
    <input type="radio" name="fruit" value="3" /> Pears
    >>> print radio_group('fruit', '1', [('1', 'Bananas'), ('2>', 'Apples <>'), ('3', 'Pears')], align='vert')
    <input type="radio" name="fruit" value="1" checked="checked" /> Bananas<br />
    <input type="radio" name="fruit" value="2&gt;" /> Apples &lt;&gt;<br />
    <input type="radio" name="fruit" value="3" /> Pears<br />
    >>> print radio_group('fruit', '1', [('1', 'Bananas'), ('2>', 'Apples <>'), ('3', 'Pears')], align='table', cols=2)
    <table border="0" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td><input type="radio" name="fruit" value="1" checked="checked" /> Bananas</td>
          <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
          <td><input type="radio" name="fruit" value="2&gt;" /> Apples &lt;&gt;</td>
          <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
        </tr>
        <tr>
          <td><input type="radio" name="fruit" value="3" /> Pears</td>
          <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
          <td></td>
          <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
        </tr>
    </table>

    """
    selected_values = value and [value] or []
    return _group(name, selected_values, options, 'radio', align, cols, sub_name)

def checkbox_group(name, selected_values, options, align='horiz', cols=4, sub_name=None):
    """Check Box Group Field.

    ``selected_values``
        A list of strings of values of options which should be ticked.

    ``options``
	an iterable of ``(value, label)`` pairs. The value is what's returned to
        the application if this option is chosen; the label is what's shown in the 
        form. You can also pass an iterable of strings in which case the labels will
        be identical to the values.

    ``align``
        can be ``'horiz'`` (default), ``'vert'`` or ``table``. If table layout is 
        chosen then you can also use the ``cols`` argument to specify the number
        of columns in the table, the default is 4.

    Examples (deliberately including some '>' characters to check they are properly escaped)

    >>> print checkbox_group('fruit', ['1', '3'], [('1', 'Bananas'), ('2>', 'Apples <>'), ('3', 'Pears')])
    <input type="checkbox" name="fruit" value="1" checked="checked" /> Bananas
    <input type="checkbox" name="fruit" value="2&gt;" /> Apples &lt;&gt;
    <input type="checkbox" name="fruit" value="3" checked="checked" /> Pears
    >>> print checkbox_group('fruit', ['1', '3'], [('1', 'Bananas'), ('2>', 'Apples <>'), ('3', 'Pears')], align='vert')
    <input type="checkbox" name="fruit" value="1" checked="checked" /> Bananas<br />
    <input type="checkbox" name="fruit" value="2&gt;" /> Apples &lt;&gt;<br />
    <input type="checkbox" name="fruit" value="3" checked="checked" /> Pears<br />
    >>> print checkbox_group('fruit', ['1', '3'], [('1', 'Bananas'), ('2>', 'Apples <>'), ('3', 'Pears')], align='table', cols=2)
    <table border="0" width="100%" cellpadding="0" cellspacing="0">
        <tr>
          <td><input type="checkbox" name="fruit" value="1" checked="checked" /> Bananas</td>
          <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
          <td><input type="checkbox" name="fruit" value="2&gt;" /> Apples &lt;&gt;</td>
          <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
        </tr>
        <tr>
          <td><input type="checkbox" name="fruit" value="3" checked="checked" /> Pears</td>
          <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
          <td></td>
          <td>&nbsp;&nbsp;&nbsp;&nbsp;</td>
        </tr>
    </table>

    """
    return _group(name, selected_values, options, 'checkbox', align, cols, sub_name)

def image_button(name, value, id=None, **attrs):
    return HTML.input(name=name, value=value, type='image', **attrs)



