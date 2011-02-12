<%inherit file="/base.mako"/>

<%def name="title()">${_('Rank')}</%def>

<%def name="body()">
<h2>${_('Rank')}</h2>
<div >
    <table class="dark">
        <thead>
            <th class="ns"></th>
            <th>${_('Name')}</th>
            <th>${_('Count')}</th>
			% if (not c.contest) or (c.contest.mode != 2): # CODEX
            	<th>${_('Time')}</th>
        	% endif
		</thead>
    <% i = -1 %>
	<% j = 1 %>
	<% last = -1 %>
    % for i, b in enumerate(c.rank):
        <tr>
            <td class="ns">${j}</td>
            <td>&nbsp;${b['user'].fname + ' ' + b['user'].lname}</td>
            <td style="text-align:center;">${b['count']}</td>
			
			% if (not c.contest) or (c.contest.mode != 2): # CODEX
				<td style="text-align:center;">${b['time']}</td>
        	% endif

			% if (last != b['count']) or (c.contest.mode != 2):
				<% j += 1 %>
				<% last = b['count'] %>
			% endif
		</tr>
    % endfor
    % if i<0:
    <tr>
		<td class="ns"></td>
		<td class="ns info" colspan=3>${_('Nobody has any solutions. You can be the first.')}</td>
	</tr>
	% endif
    </table>
    </div>

</%def>
