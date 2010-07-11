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
        </thead>
    <% i = -1 %>
    % for i, b in enumerate(c.users):
        <tr>
            <td class="ns">${i+1}</td>
            <td>
			% if b.admin:
				<img src="/running.gif" alt="is running">
			% endif
            &nbsp;${b.fname + ' ' + b.lname}</td>
            <td style="text-align:center;">${b.cls}</td>
			<td class="ns"><a href=${h.url_for(id="edit", param=b.id)}><img src="/edit.png" alt="e"></a></td>
			<td class="ns"><a href="#" ondblclick='remove("${h.url_for(id="remove", param=b.id)}");'><img src="/remove.png" alt="e"></a></td>
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
