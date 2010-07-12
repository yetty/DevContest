<%inherit file="/admin/base.mako"/>

<%def name="title()">${_('The List of Contests')}</%def>

<%def name="body()">
	<h2>${_('The List of Contests')}</h2>
	<table class="dark">
	% for contest in c.list:
			<tr>
				<td class="ns">${contest.id}</td>
				<td>
				% if contest.is_running:
					<img src="/running.gif" alt="${_('is running')}">
				% endif
				${contest.name}</td>
				<td class="ns">
				<a href=${h.url_for(id=contest.id, param="cp")}>
				%if contest.pilsprog_mode:
					${_('Pilsprog')}
				%else:
					${_('Normal')}
				%endif
				</a></td>
				<td class="ns">
				% if contest.is_running:
					<a href=${h.url_for(id=contest.id, param="stop")}><img src="/pause.png" alt="${_('Stop')}"></a>
				% else:
					<a href=${h.url_for(id=contest.id, param="start")}><img src="/play.png" alt="${_('Start')}"></a>
				% endif
				</td>
				<td class="ns"><a href=${h.url_for(id=contest.id)}><img src="/edit.png" alt="${_('Edit')}"></a></td>
				<td class="ns"><a href="#" ondblclick='remove("${h.url_for(id=contest.id, param="remove")}");'><img src="/remove.png" alt="${_('Remove')}"></a></td>

			</tr>
	%endfor
	</table>
	<hr>
	 ${h.form_start(h.url_for(id="_", param="create"), method="post")}
	 ${h.field("Název soutěže", h.text(name="name"))}
	 ${h.field("", h.submit("submit", "Vytvořit"))}
	 ${h.form_end()}
</%def>
