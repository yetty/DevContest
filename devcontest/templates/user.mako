<%inherit file="/base.mako"/>

<%def name="title()">${_('Profile')}</%def>

<%def name="body()">
<h2>${_('Profile')}</h2>

% if c.errors:
	<ol id="errors">
%	for error in c.errors:
		<li>${error}</li>
%	endfor
	</ol>
% endif
${h.form(h.url_for(controller="user", action="save"), method="post")}
<label for="login" class="strong">${_('Login')}:</label>
${c.user.login}<br/><br/>
<label for="password" class="strong">${_('Password')}:</label><br>
${h.password('password')} ${h.password('cpassword')} <span class="info">${_('twice for sure')}</span><br/>
<label for="mail" class="strong">${_('E-mail')}:</label><br/>
${h.text('mail', c.user.mail)}<br/>
<br>

<label for="fname">${_('First name')}:</label><br/>
${h.text('fname', c.user.fname)}<br/>
<label for="lname">${_('Last name')}:</label><br/>
${h.text('lname', c.user.lname)}<br/>
<label for="class">${_('Class')}:</label><br/>
${h.text('cls', c.user.cls)}<br/>
<br/>

${h.submit('submit', 'Upravit')}

<p class="info">
	${_('Strong items are obliged.')} <br>
</p>
${h.end_form()}

</%def>
