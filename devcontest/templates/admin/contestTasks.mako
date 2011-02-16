<%inherit file="/admin/base.mako"/>

<%def name="title()">${_('The List of Tasks')}</%def>

<%def name="body()">
	<h2>${_('The List of Tasks')}</h2>
	<table class="dark">
	% for task in c.list:
			<tr>
				<td class="ns"><a href=${h.url_for(action="task", id=task.id)}><img src="/edit.png" alt="${_('Edit')}"></a></td>
				<td>${task.name}</td>
				<td class="ns">
					<img style="cursor:pointer;" ondblclick='remove("${h.url_for(action="task", id=task.id, param="remove")}");' src="/remove.png" alt="${_('Remove')}">
				</td>
			</tr>
	%endfor
	</table>
	
	<br>

	 ${h.form_start(h.url_for(param="create_task"), method="post")}
	 ${h.field(_("Name of task"), h.text(name="name"))}
	 ${h.field("", h.submit("submit", _("Create")))}
	 ${h.form_end()}

	<hr>

	 <h3>${_('Settings of the Contest')}</h3>
	 <form action="${h.url_for(param='save')}" method="post">
	 <table>
	 	<tr>
			<td>${_('Contest name:')}</td>
			<td><input type="text" name="contest_name" value="${c.contest.name}"></td>
		</tr>
	 	<tr>
			<td>${_('Contest mode:')}</td>
			<td>
				 <select name="mode">
					<option	value="${c.contest.mode}">${c.contest.modes[c.contest.mode]}</option>
					<option disabled>---</option>

					%for i, mode in enumerate(c.contest.modes):
						<option value="${i}">${mode}</option
					%endfor
				</select>
			</td>
		</tr>
		<tr>
			<td>${_('Show results:')}</td>
			<td><input type="checkbox" name="results" value="true" 
			%if c.contest.results:
				checked
			%endif			
			> ${_('Yes')}</td>
		</tr>

		<tr>
			<td colspan=2><input type="submit" value="${_('Save')}"></td>
		</tr>
	</table>
	</form>
</%def>
