<%inherit file="/admin/base.mako"/>

<%def name="title()">Seznam stránek</%def>

<%def name="body()">
	<h2>Seznam stránek</h2>
	<table class="dark">
	% for page in c.list:
			<tr>
				<td>${page}</td>
				<td class="ns"><a href=${h.url_for(id=page)}><img src="/edit.png" alt="e"></a></td>
				<td class="ns"><a href="#" ondblclick='remove("${h.url_for(id=page, param="remove")}");'><img src="/remove.png" alt="e"></a></td>
			</tr>
	%endfor
	</table>
	<hr>
	 ${h.form_start(h.url_for(id="_", param="create"), method="post")}
	 ${h.field("Url stránky", h.text(name="url"))}
	 ${h.field("", h.submit("submit", "Vytvořit"))}
	 ${h.form_end()}
</%def>
