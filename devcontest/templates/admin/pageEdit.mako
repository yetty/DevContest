<%inherit file="/admin/base.mako"/>

<%def name="title()">Editace stránky ${c.name}</%def>

<%def name="body()">
	% if c.lang:
		<script type="text/javascript">var LANG="${c.lang}";</script>
		<%include file="/edit.mako"/>
	% endif
	<h2>Editace stránky ${c.name}</h2>
	${h.form_start(h.url_for(id=c.name, param="save"), method="post")}
	${h.textarea(name="area", content=c.content, rows=30, cols=100)}
	${h.submit("submit", "Odeslat")}
	${h.form_end()}
</%def>
