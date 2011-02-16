<%inherit file="/base.mako"/>

<%def name="title()">${c.source.id}</%def>

<%def name="body()">
	<h3>${c.user.getName()}</h3> 
	<h2>${c.task_name}</h2>
<%
from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import HtmlFormatter
%>
	<% source = c.source.getFile().read() %>
	${highlight(source, guess_lexer(source), HtmlFormatter(linenos=True)) | n}

</%def>
