<%inherit file="/base.mako"/>

<%def name="title()">${_('Source codes')}</%def>

<%def name="body()">
<h2>${_('Source codes')}</h2>
<div >
    <table class="dark">
        <thead>
            <th class="ns"></th>
            <th>${_('Task')}</th>
            <th>${_('Date')}</th>
        	<th>${_('Status')}</th>
		</thead>
    
	% for b in c.sources:
        <tr>
			<td class="ns"><a
			href=${h.url_for(action="source",id=b.id, param=None)}><img src="/source.gif" alt="${_('view')}"></a></td>
            <td>${c.getTaskName(b.task_id)}</td>
            <td style="text-align:center;">${b.datetime.strftime("%d.%m.%Y %H:%m:%S")}</td>
        	<td class="ns" style="text-align:center;"> 
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
