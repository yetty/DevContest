<%inherit file="/base.mako"/>

<%def name="title()">${_('Users')}</%def>

<%def name="body()">
<h2>${_('Users')}</h2>
<div >
    <table class="dark">
        <thead>
            <th class="ns" colspan=2></th>
            <th>${_('Name')}</th>
            <th>${_('Class')}</th>
        </thead>
    <% i = -1 %>
    % for i, b in enumerate(c.users):
        <tr>
			<td class="ns"><a href=${h.url_for(id="edit", param=b.id)}><img src="/edit.png" alt="${_('edit')}"></a></td>
			<td class="ns"><a href=${h.url_for(id="sources", param=b.id)}><img
			src="/source.gif" alt="${_('sources')}"></a></td>
            <td>
			% if b.admin:
				<img src="/running.gif" alt="${_('is administrator')}">
			% endif
            &nbsp;${b.fname + ' ' + b.lname}</td>
            <td style="text-align:center;">${b.cls}</td>
			<td class="ns">
				<img style="cursor:pointer;" ondblclick='remove("${h.url_for(id="remove", param=b.id)}");' src="/remove.png" alt="${_('remove')}">
			</td>
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
