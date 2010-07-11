<%inherit file="/admin/base.mako"/>

<%def name="title()">Seznam otázek</%def>

<%def name="body()">
	<h2>Seznam otázek</h2>
	<table class="dark">
	% for task in c.list:
			<tr>
				<td>${task.name}</td>
				<td class="ns"><a href=${h.url_for(action="task", id=task.id)}><img src="/edit.png" alt="e"></a></td>
				<td class="ns"><a href="#" ondblclick='remove("${h.url_for(action="task", id=task.id, param="remove")}");'><img src="/remove.png" alt="e"></a></td>
			</tr>
	%endfor
	</table>
	<hr>
	 ${h.form_start(h.url_for(param="create_task"), method="post")}
	 ${h.field("Název úkolu", h.text(name="name"))}
	 ${h.field("", h.submit("submit", "Vytvořit"))}
	 ${h.form_end()}
</%def>
