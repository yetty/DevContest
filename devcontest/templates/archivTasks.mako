<%inherit file="/base.mako"/>

<%def name="title()">${_('Archiv :: list of tasks')}</%def>

<%def name="body()">
	<h2>${_('Archiv :: list of tasks')}</h2>
	<table class="dark">
	<thead>
		<th class="ns"></th>
		<th width=80%>${_('Name')}</th>
		<th>${_('Resolvers')}</th>
		<th>${_('Success resolvers')}</th>
	</thead>
	% for i, task in enumerate(c.list):
		<tr>
			<td class="ns">${i+1}</td>
			<td><a href=${h.url_for(controller="task", action="show", id=task.id)}>${task.name}</a></td>
			<td style="text-align:center;">${c.allUsers(task.id)}</td>
			<td style="text-align:center;">${c.okUsers(task.id)}</td>
		</tr>
	%endfor
	</table>
</%def>
