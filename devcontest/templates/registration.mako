<%inherit file="/base.mako"/>

<%def name="title()">${_('Registration')}</%def>

<%def name="body()">
<h2>${_('Registration')}</h2>

% if not c.success:
	% if c.errors:
		<ol id="errors">
	%	for error in c.errors:
			<li>${error}</li>
	%	endfor
		</ol>
	% endif
	${h.form(h.url_for(controller="registration", action="check"), method="post")}
	<label for="login" class="strong">${_('Login')}:</label><br/>
	${h.text('login', c.form['login'])}<br/>
	<label for="password" class="strong">${_('Password')}:</label><br/>
	${h.password('password', c.form['password'])} ${h.password('cpassword', c.form['cpassword'])} <span class="info">(${_('twice for sure')})</span><br/>
	<label for="mail" class="strong">${_('E-mail')}:</label><br/>
	${h.text('mail', c.form['mail'])}<br/>
	<br>

	<label for="fname">${_('First name')}:</label><br/>
	${h.text('fname', c.form['fname'])}<br/>
	<label for="lname">${_('Last name')}:</label><br/>
	${h.text('lname', c.form['lname'])}<br/>
	<label for="class">${_('Class')}:</label><br/>
	${h.text('cls', c.form['cls'])}<br/>
	<br/>

	${h.submit('submit', _('Submit'))}

	<p class="info">
		${_('Strong items are obliged.')}
	</p>
	${h.end_form()}
% else:
	<p>${_('Registration was succesful. You can log in by the box on the left.')}</p>
% endif
</%def>
