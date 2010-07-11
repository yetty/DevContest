<%inherit file="/base.mako"/>

<%def name="title()">Pořadí</%def>

<%def name="body()">
<h2>Pořadí</h2>
<div >
    <table class="dark">
        <thead>
            <th class="ns"></th>
            <th>Jméno</th>
            <th>Třída</th>
            <th>Počet</th>
        </thead>
    <% i = -1 %>
    % for i, b in enumerate(c.users):
        <tr>
            <td class="ns">${i+1}</td>
            <td>&nbsp;${b['user'].fname + ' ' + b['user'].lname}</td>
            <td style="text-align:center;">${b['user'].cls}</td>
            <td style="text-align:center;">${b['count']}</td>
        </tr>
    % endfor
    % if i<0:
    <tr>
		<td class="ns"></td>
		<td class="ns info" colspan=3>Nikdo?</td>
	</tr>
	% endif
    </table>
    </div>

</%def>
