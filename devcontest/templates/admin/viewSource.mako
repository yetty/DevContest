<%inherit file="/base.mako"/>

<%def name="title()">${c.source.id}</%def>

<%def name="body()">
	
	<h3>${c.user.getName()}</h3> 
	<h2>
		<a href=${h.url_for(id="source_rerun")}>
			<img style="float: right;" src="/repeat.png" alt="${_('re-run this source')}">
		</a>
		${c.task_name}</h2>
	<p>${c.source.errors | n}</p>
<%
from pygments import highlight
from pygments.lexers import guess_lexer
from pygments.formatters import HtmlFormatter
%>
	<% source = c.source.getFile().read() %>
	${highlight(source, guess_lexer(source), HtmlFormatter(linenos=True)) | n}

</%def>
