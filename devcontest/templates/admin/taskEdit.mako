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
		<tr><td>&nbsp;</td></tr>
		<tr>
			<td>
			${_('Time limit (seconds)')}: <input type="text" name="time_limit" value="${c.time_limit}">
			</td>
			<td>
			${_('Memory limit (kB)')}: <input type="text" name="memory_limit" value="${c.memory_limit}">
			</td>
		</tr>
		<tr>
			<td colspan=2>
			${_('Count of test script execution')}: <input type="text" name="run_count" value="${c.run_count}">
			</td>
		</tr>
		<tr>
			<td class="strong">
			${_('Script for generating input')}:

			<select name="script_in_lang">
				<option value="${c.script_in_lang}">${c.script_in_lang}</option>
				<option disabled>---</option>

				% for runner in c.runners:
					<option value="${runner.lang}">${runner.lang}</option>
				% endfor
			</select>
			</td>
			<td class="strong">
			${_('Script for process')}:

			<select name="script_out_lang">
				<option name="${c.script_out_lang}">${c.script_out_lang}</option>
				<option disabled>---</option>

				% for runner in c.runners:
					<option name="${runner.lang}">${runner.lang}</option>
				% endfor
				</select>
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
				<pre style="width: 350px;" wrap=hard>${c.run_in["compile"]}
${c.run_in["errors"]}</pre>
			</td>
			<td>
				${_('status')}: ${c.run_out["status"]}<br>
				${_('output')}:</br>
				<pre style="width: 350px;" wrap=hard>${c.run_out["return"]}</pre>
				${_('errors')}:</br>
				<pre style="width: 350px;" wrap=hard>${c.run_out["compile"]}
${c.run_out["errors"]}</pre>
			</td>
		</tr>
	</table>
	${h.form_end()}
	<%include file="/edit.mako"/>
</%def>
