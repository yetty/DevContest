<%inherit file="/admin/base.mako"/>

<%def name="title()">${_('The List of Pages')}</%def>

<%def name="body()">
	<h2>${_('The List of Pages')}</h2>
	<table class="dark">
	% for page in c.list:
			<tr>
				<td class="ns"><a href=${h.url_for(id=page)}><img src="/edit.png" alt="${_('Edit')}"></a></td>
				<td>${page}</td>
				<td class="ns"><img ondblclick='remove("${h.url_for(id=page,
				param="remove")}");' src="/remove.png" alt="${_('Remove')}"
				style="cursor:pointer;" ></td>
			</tr>
	%endfor
	</table>
	<hr>
	 ${h.form_start(h.url_for(id="_", param="create"), method="post")}
	 ${h.field(_("URL"), h.text(name="url"))}
	 ${h.field("", h.submit("submit", _("Create")))}
	 ${h.form_end()}
</%def>
