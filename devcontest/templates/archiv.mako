<%inherit file="/base.mako"/>

<%def name="title()">Seznam otázek</%def>

<%def name="body()">
	<h2>Seznam soutěží</h2>
	<table class="dark">
	<thead>
		<th class="ns"></th>
		<th width=80% colspan=3>Název</th>
		<th>Zahájení</th>
	</thead>
	<% i = -1 %>
	% for i, contest in enumerate(c.list):
		<tr>
			<td class="ns">${i+1}</td>
			<td width=50%>${contest.name}</td>
			<td style="text-align:center;"><a href=${h.url_for(controller="archiv", action="contest", id=contest.id)}>úlohy</a></td>
			<td style="text-align:center;"><a href=${h.url_for(controller="contest", action="rank", id=contest.id)}>pořadí</a></td>
			<td style="text-align:center;">${contest.timeStart.strftime("%d.%m.%Y")}</td>
		</tr>
	%endfor
    % if i<0:
    <tr>
		<td class="ns"></td>
		<td class="ns info" colspan=3>Ještě nemáme žádnou soutěž v archivu!</td>
	</tr>
	% endif
	</table>
</%def>
