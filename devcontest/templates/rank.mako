<%inherit file="/base.mako"/>

<%def name="title()">Pořadí</%def>

<%def name="body()">
<h2>Pořadí</h2>
<div >
    <table class="dark">
        <thead>
            <th class="ns"></th>
            <th>Jméno</th>
            <th>Počet</th>
            <th>Čas</th>
        </thead>
    <% i = -1 %>
    % for i, b in enumerate(c.rank):
        <tr>
            <td class="ns">${i+1}</td>
            <td>&nbsp;${b['user'].fname + ' ' + b['user'].lname}</td>
            <td style="text-align:center;">${b['count']}</td>
            <td style="text-align:center;">${b['time']}</td>
        </tr>
    % endfor
    % if i<0:
    <tr>
		<td class="ns"></td>
		<td class="ns info" colspan=3>Nikdo ještě nic nevyřešil. Můžeš být první!</td>
	</tr>
	% endif
    </table>
    </div>

</%def>
