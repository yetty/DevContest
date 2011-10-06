<%inherit file="/base.mako"/>

<%def name="title()">${_('Last sources')}</%def>

<%def name="body()">
<h2>${_('Last sources')}</h2>
<div >
    <table class="dark">
        <thead>
            <th class="ns"></th>
            <th>${_('Task')}</th>
            <th>${_('User')}</th>
            <th>${_('Date')}</th>
        	<th class="ns"></th>
		</thead>

	% for b in c.sources:
        <tr>
			<td class="ns">
				<a href=${h.url_for(id="source_view",param=b.id)}>
					<img src="/source.gif" alt="${_('view')}">
				</a>
			</td>
            <td>
				<a href=${h.url_for(id="source_view",param=b.id)}>
					${c.getTaskName(b.task_id)}
				</a>
			</td>
            <td>
				<a href=${h.url_for(id="sources", param=b.user_id)}>${c.getUser(b.user_id)}</a>
			</td>
            <td style="text-align:center;">${b.datetime.strftime("%d.%m.%Y")}</td>
        	<td class="ns">
			<img
			% if b.status:
				src="/true.png" alt="${_('Solved')}"
			% else:
				src="/remove.png" alt="${_('Not solved')}"
			% endif
			>
			</td>
		</tr>
    % endfor
	</table>
    </div>
</%def>
