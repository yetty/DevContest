<%inherit file="/base.mako"/>

<%def name="title()">${_('The Archive')}</%def>

<%def name="body()">
	<h2>${_('The Archive')}</h2>
	<table class="dark">
	<thead>
		<th class="ns"></th>
		<th width=80% colspan=3>${_('Name')}</th>
		<th>${_('Started at')}</th>
	</thead>
	<% i = -1 %>
	% for i, contest in enumerate(c.list):
		<tr>
			<td class="ns">${i+1}</td>
			<td width=50%>${contest.name}</td>
			<td style="text-align:center;"><a href=${h.url_for(controller="archiv", action="contest", id=contest.id)}>${_('tasks')}</a></td>
			<td style="text-align:center;"><a href=${h.url_for(controller="contest", action="rank", id=contest.id)}>${_('rank')}</a></td>
			<td style="text-align:center;">${contest.timeStart.strftime(_("%d.%m.%Y"))}</td>
		</tr>
	%endfor
    % if i<0:
    <tr>
		<td class="ns"></td>
		<td class="ns info" colspan=3>${_('There are no contests in archive.')}</td>
	</tr>
	% endif
	</table>
</%def>
