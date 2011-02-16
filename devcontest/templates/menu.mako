<%def name="menu()">
    % if request.environ.get('REMOTE_USER'):
    <ul>
		<%
		from devcontest.model import Contest
		from devcontest.model.meta import Session
		%>
		% for contest in Session.query(Contest).filter_by(is_running=True).all():
			<li class="h">${contest.name}<hr></li>
			<li><a href=${h.url_for(controller="contest", action="tasks", id=contest.id, param=None)}>${_('Tasks')}</a></li>
			% if contest.results or request.environ.get('REMOTE_USER').admin:
				<li><a href=${h.url_for(controller="contest", action="rank", id=contest.id, param=None)}>${_('Ranks')}</a></li>
			% endif
			<li class="break"></li>
		% endfor
		% if request.environ.get('REMOTE_USER').admin:
			<% exists = False %>
			% for contest in Session.query(Contest).filter_by(is_running=False, timeStart=None).all():
				<li><a style="font-style: italic;" href=${h.url_for(controller="contest", action="tasks", id=contest.id, param=None)}>${contest.name}</a></li>
				<% exists = True %>
			% endfor
			% if exists:
				<li class="break"></li>
			% endif
		% endif
        <li><a href=${h.url_for(controller="archiv", action="index", id=None, param=None)}>${_('Archive')}</a></li>
        <li><a href=${h.url_for(controller="page", action="documentation", id=None, param=None)}>${_('Documentation')}</a></li>
        <li><a href=${h.url_for(controller="page", action="FAQ", id=None, param=None)}>${_('FAQ')}</a></li>
        <li class="break"></li>
        % if request.environ.get('REMOTE_USER').admin:
            <li>
				<a href="#">${_('Administration')}</a>
				<ul>
					<li><a href=${h.url_for(controller="admin", action="contest", id=None, param=None)}>${_('Contests')}</a></li>
					<li><a href=${h.url_for(controller="admin", action="page", id=None, param=None)}>${_('Pages')}</a></li>
					<li><a href=${h.url_for(controller="admin", action="users", id=None, param=None)}>${_('Users')}</a></li>
					<li><a href=${h.url_for(controller="admin", action="runners", id=None, param=None)}>${_('Starters')}</a></li>
				</ul>
            </li>
            <li class="break"></li>
        % endif
        <li><a href=${h.url_for(controller="user", action="top", id="10", param=None)}>${_('TOP10')}</a></li>
        <li><a href=${h.url_for(controller="user", action="index", id=None, param=None)}>${_('Profile')}</a></li>
        <li><a href=${h.url_for(controller="auth", action="signout", id=None, param=None)}>${_('Log out')}</a></li>
    </ul>
    % endif
</%def>
