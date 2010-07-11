<%def name="menu()">
    % if request.environ.get('REMOTE_USER'):
    <ul>
		<%
		from devcontest.model import Contest
		from devcontest.model.meta import Session
		%>
		% for contest in Session.query(Contest).filter_by(is_running=True).all():
			<li class="h">${contest.name}<hr></li>
			<li><a href=${h.url_for(controller="contest", action="tasks", id=contest.id, param=None)}>Úkoly</a></li>
			<li><a href=${h.url_for(controller="contest", action="rank", id=contest.id, param=None)}>Pořadí</a></li>
			<li class="break"></li>
		% endfor
        <li><a href=${h.url_for(controller="archiv", action="index", id=None, param=None)}>Archiv</a></li>
        <li><a href=${h.url_for(controller="page", action="documentation", id=None, param=None)}>Dokumentace</a></li>
        <li><a href=${h.url_for(controller="page", action="FAQ", id=None, param=None)}>FAQ</a></li>
        <li class="break"></li>
        % if request.environ.get('REMOTE_USER').admin:
            <li>
				<a href="#">Administrace</a>
				<ul>
					<li><a href=${h.url_for(controller="admin", action="contest", id=None, param=None)}>Soutěže</a></li>
					<li><a href=${h.url_for(controller="admin", action="page", id=None, param=None)}>Stránky</a></li>
					<li><a href=${h.url_for(controller="admin", action="users", id=None, param=None)}>Uživatelé</a></li>
					<li><a href=${h.url_for(controller="admin", action="runners", id=None, param=None)}>Spouštěče</a></li>
				</ul>
            </li>
            <li class="break"></li>
        % endif
        <li><a href=${h.url_for(controller="user", action="top", id="10", param=None)}>TOP10</a></li>
        <li><a href=${h.url_for(controller="user", action="index", id=None, param=None)}>Profil</a></li>
        <li><a href=${h.url_for(controller="auth", action="signout", id=None, param=None)}>Odhlásit</a></li>
    </ul>
    % endif
</%def>
