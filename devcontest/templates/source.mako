<%inherit file="/base.mako"/>

<%def name="title()">${c.source.id}</%def>

<%def name="body()">
	<a href="${h.url_for(action='sources', id=None)}" class="back">${_('back to the list of sources')}</a>
	<h2>${c.task_name}</h2>
<%
from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import HtmlFormatter
%>
	<% source = c.source.getFile().read() %>
	${highlight(source, guess_lexer(source), HtmlFormatter(linenos=True)) | n}

</%def>
