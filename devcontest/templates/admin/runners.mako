<%inherit file="/admin/base.mako"/>

<%def name="title()">Nastavení spouštěčů a kompilátorů</%def>

<%def name="body()">
	<script type="text/javascript">var LANG="html";</script>
	<h2>Nastavení spouštěčů a kompilátorů</h2>

	<table class="dark">
	% for item in c.list:
			<tr>
				<td class="ns">${item.id}</td>
				<td>${item.lang}</td>
				<td>${item.compile}</td>
				<td>${item.run}</td>
				<td class="ns"><a href="#" ondblclick='remove("${h.url_for(id=item.id, param="remove")}");'><img src="/remove.png" alt="e"></a></td>
			</tr>
	%endfor
	</table>
	<hr>
	 ${h.form_start(h.url_for(id="save", param=None), method="post")}
	 ${h.field("Jazyk (přípona)", h.text(name="lang"))}
	 ${h.field("Kompilátor", h.text(name="compile", size=50))}
	 ${h.field("Spouštěč", h.text(name="run", size=50))}
	 ${h.field("", h.submit("submit", "Vytvořit"))}
	 <p class="info" style="float:right;"><br>%f pro vstup<br>%o pro výstup</p>
	 ${h.form_end()}
</%def>
