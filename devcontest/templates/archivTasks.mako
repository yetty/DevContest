<%inherit file="/base.mako"/>

<%def name="title()">Seznam otázek</%def>

<%def name="body()">
	<h2>Seznam soutěží</h2>
	<table class="dark">
	<thead>
		<th class="ns"></th>
		<th width=80%>Název</th>
		<th>Řešitelů</th>
	</thead>
	% for i, task in enumerate(c.list):
		<tr>
			<td class="ns">${i+1}</td>
			<td><a href=${h.url_for(controller="task", action="show", id=task.id)}>${task.name}</a></td>
			<td style="text-align:center;">${c.okUsers(task.id)}</td>
		</tr>
	%endfor
	</table>
</%def>
