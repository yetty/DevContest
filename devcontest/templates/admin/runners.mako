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

	<h3>${_('Examples of runners')}</h3>
	<p>${_('Little help with settings of runners. Can be depended on the server.')}</p>
	<table class="dark">
		<tr>
			<td><strong>c</strong></td>
			<td>gcc -std=gnu99 -O2 -g -lm -o %o %f</td>
			<td>%f</td>
		</tr>
		<tr>
			<td><strong>c++</strong></td>
			<td>g++ -std=gnu++98 -O2 -g -lm -o %o %f</td>
			<td>%f</td>
		</tr>
		<tr>
			<td><strong>pas</strong></td>
			<td>fpc -g -O2 -Sg -Ci -Cr -Ct -ve -o%o %f</td>
			<td>%f</td>
		</tr>
		<tr>
			<td><strong>java</strong></td>
			<td>javac %f</td>
			<td>cd %p; java %c</td>
		</tr>
		<tr>
			<td><strong>py</strong></td>
			<td></td>
			<td>python %f</td>
		</tr>

	</table>
</%def>
