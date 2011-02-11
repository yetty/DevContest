<%inherit file="/base.mako"/>

<%def name="title()">${_('Ranking')}</%def>

<%def name="body()">
<h2>${_('Ranking')}</h2>
<div >
    <table class="dark">
        <thead>
            <th class="ns"></th>
            <th>${_('Name')}</th>
            <th>${_('Class')}</th>
            <th>${_('Count')}</th>
        </thead>
    <% i = -1 %>
    % for i, b in enumerate(c.users):
        <tr>
            <td class="ns" style="text-align:right;">${i+1}</td>
            <td>&nbsp;${b['user'].fname + ' ' + b['user'].lname}</td>
            <td style="text-align:center;">${b['user'].cls}</td>
            <td style="text-align:center;">${b['count']}</td>
        </tr>
    % endfor
    % if i<0:
    <tr>
		<td class="ns"></td>
		<td class="ns info" colspan=3>${_('Nobody?')}</td>
	</tr>
	% endif
    </table>
    </div>

</%def>
