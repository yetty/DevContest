<%inherit file="/admin/base.mako"/>

<%def name="title()">${_('The List of Tasks')}</%def>

<%def name="body()">
	<h2>${_('The List of Tasks')}</h2>
	<table class="dark">
	% for task in c.list:
			<tr>
				<td class="ns"><a href=${h.url_for(action="task", id=task.id)}><img src="/edit.png" alt="${_('Edit')}"></a></td>
				<td>${task.name}</td>
				<td class="ns"><a href="#" ondblclick='remove("${h.url_for(action="task", id=task.id, param="remove")}");'><img src="/remove.png" alt="${_('Remove')}"></a></td>
			</tr>
	%endfor
	</table>
	<hr>
	 ${h.form_start(h.url_for(param="create_task"), method="post")}
	 ${h.field(_("Name of task"), h.text(name="name"))}
	 ${h.field("", h.submit("submit", _("Create")))}
	 ${h.form_end()}
</%def>
