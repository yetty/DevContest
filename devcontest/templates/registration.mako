<%inherit file="/base.mako"/>

<%def name="title()">Registrace</%def>

<%def name="body()">
<h2>Registrace</h2>

% if not c.success:
	% if c.errors:
		<ol id="errors">
	%	for error in c.errors:
			<li>${error}</li>
	%	endfor
		</ol>
	% endif
	${h.form(h.url_for(controller="registration", action="check"), method="post")}
	<label for="login" class="strong">Login:</label><br/>
	${h.text('login', c.form['login'])}<br/>
	<label for="password" class="strong">Heslo:</label><br/>
	${h.password('password', c.form['password'])} ${h.password('cpassword', c.form['cpassword'])} <span class="info">(dvakrát pro kontrolu)</span><br/>
	<label for="mail" class="strong">E-mail:</label><br/>
	${h.text('mail', c.form['mail'])}<br/>
	<br>

	<label for="fname">Jméno:</label><br/>
	${h.text('fname', c.form['fname'])}<br/>
	<label for="lname">Příjmení:</label><br/>
	${h.text('lname', c.form['lname'])}<br/>
	<label for="class">Třída:</label><br/>
	${h.text('cls', c.form['cls'])}<br/>
	<br/>

	${h.submit('submit', 'Zaregistrovat')}

	<p class="info">
		Tučně zvýrazněné položky jsou povinné.
	</p>
	${h.end_form()}
% else:
	<p>Registrace byla úspěšná. Nyní se můžete přihlásit formulářem vlevo.</p>
% endif
</%def>
