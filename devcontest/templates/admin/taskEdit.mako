<%inherit file="/admin/base.mako"/>

<%def name="title()">${_('Editation of task')} ${c.name}</%def>

<%def name="body()">
	<script type="text/javascript">var LANG="html";</script>
	<a href=${h.url_for(controller="admin", action="contest", id=c.contest_id, param=None)} class="back">${_('back to the contest')}</a>
	<h2>${c.name}</h2>
	${h.form_start(h.url_for(id=c.id, param="save"), method="post")}
	${h.textarea(name="description", content=c.description, rows=20, cols=114)}
	${h.submit("submit", _("Submit"))}
	<table>
		<tr>
			<td class="strong">
			${_('Example of input')}:
			</td>
			<td class="strong">
			${_('Example of output')}:
			</td>
		</tr>
		<tr>
			<td class="strong">
			${h.textarea(name="example_in", id="", content=c.example_in, rows=15, cols=55)}
			</td>
			<td class="strong">
			${h.textarea(name="example_out", id="", content=c.example_out, rows=15, cols=55)}
			</td>
		</tr>
		<tr>
			<td class="strong">
			${_('Script for generating input')}:
			</td>
			<td class="strong">
			${_('Script for process')}:
			</td>
		</tr>
		<tr>
					<!-- lang="python" -->
			<td>
			<textarea name="data_in" id="data_in" rows=20 cols=55>${c.data_in}</textarea>
			</td>
			<td>
			<textarea name="data_out" id="data_out" rows=20 cols=55>${c.data_out}</textarea>
			</td>
		</tr>
		<tr><td colspan=2>${h.submit("submit", _("Submit"))}</td></tr>
		<tr>
			<td class="strong">
			${_('Actually input')}:
			</td>
			<td class="strong">
			${_('Actually output')}:
			</td>
		</tr>
		<tr>
			<td>
				${_('status')}: ${c.run_in["status"]}<br>
				${_('output')}:</br>
				<pre style="width: 350px;" wrap=hard>${c.run_in["return"]}</pre>
				${_('errors')}:</br>
				<pre style="width: 350px;" wrap=hard>${c.run_in["errors"]}</pre>
			</td>
			<td>
				${_('status')}: ${c.run_out["status"]}<br>
				${_('output')}:</br>
				<pre style="width: 350px;" wrap=hard>${c.run_out["return"]}</pre>
				${_('errors')}:</br>
				<pre style="width: 350px;" wrap=hard>${c.run_out["errors"]}</pre>
			</td>
		</tr>
	</table>
	${h.form_end()}
	<%include file="/edit.mako"/>
</%def>
