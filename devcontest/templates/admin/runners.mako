<%inherit file="/admin/base.mako"/>

<%def name="title()">${_('The Settings of Compilators and Starters')}</%def>

<%def name="body()">
	<h2>${_('The Settings of Compilators and Starters')}</h2>

	<table class="dark">
	% for item in c.list:
			<tr>
				<td><strong>${item.lang}</strong></td>
				<td>${item.compile}</td>
				<td>${item.run}</td>
				<td class="ns"><img style="cursor:pointer;" src="/remove.png" ondblclick='remove("${h.url_for(id=item.id, param="remove")}");' alt="${_('Remove')}"></td>
			</tr>
	%endfor
	</table>
	<hr>
	 ${h.form_start(h.url_for(id="save", param=None), method="post")}
	 ${h.field(_("Language (extension)"), h.text(name="lang"))}
	 ${h.field(_("Compilator"), h.text(name="compile", size=50))}
	 ${h.field(_("Starter"), h.text(name="run", size=50))}
	 ${h.field("", h.submit("submit", _("Create")))}
	 <p class="info" style="float:right;"><br>%f ${_('for input')}<br>%o ${_('for output')}</p>
	 ${h.form_end()}
</%def>
