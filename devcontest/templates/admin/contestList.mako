<%inherit file="/admin/base.mako"/>

<%def name="title()">${_('The List of Contests')}</%def>

<%def name="body()">
	<h2>${_('The List of Contests')}</h2>
	<table class="dark">
	% for contest in c.list:
			<tr>
				<td class="ns"><a href=${h.url_for(id=contest.id)}><img src="/edit.png" alt="${_('Edit')}"></a></td>
				<td>
				% if contest.is_running:
					<img src="/running.gif" alt="${_('is running')}">
					<strong>
				% endif
					${contest.name}
				% if contest.is_running:
					</strong>
				% endif
				</td>
				<td class="ns">
				% if contest.is_running:
					<a href=${h.url_for(id=contest.id, param="stop")}><img src="/pause.png" alt="${_('Stop')}"></a>
				% else:
					<a href=${h.url_for(id=contest.id, param="start")}><img src="/play.png" alt="${_('Start')}"></a>
				% endif
				</td>
				<td class="ns">
					<img style="cursor:pointer;" ondblclick='remove("${h.url_for(id=contest.id, param="remove")}");' src="/remove.png" alt="${_('Remove')}" title="${_('Remove')}">
				</td>
				<td class="ns">
					% if not contest.is_running and contest.timeStart!=None:
						<img style="cursor:pointer;"  ondblclick='remove("${h.url_for(id=contest.id, param="reset")}");' src="/reset.png" alt="${_('Clean up')}" title="${_('Clean up')}">
					% endif
				</td>
			</tr>
	%endfor
	</table>
	<hr>
	 ${h.form_start(h.url_for(id="_", param="create"), method="post")}
	 ${h.field(_("Name"), h.text(name="name"))}
	 ${h.field("", h.submit("submit", _("Create")))}
	 ${h.form_end()}
</%def>
