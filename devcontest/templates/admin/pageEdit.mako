<%inherit file="/admin/base.mako"/>

<%def name="title()">${_('Editation of page')} ${c.name}</%def>

<%def name="body()">

	% if c.lang:
		<script type="text/javascript">var LANG="${c.lang}";</script>
		<%include file="/edit.mako"/>
	% endif
	<h2>${_('Editation of page')} ${c.name}</h2>

	% if c.error:
		<div class="error">${c.error}</div>
	% endif

	% if c.success:
		<div class="success">${c.success}</div><br>
	% endif

	${h.form_start(h.url_for(id=c.name, param="save"), method="post")}
	${h.textarea(name="area", content=c.content, rows=30, cols=100)}
	${h.submit("submit", _("Submit"))}
	${h.form_end()}
</%def>
