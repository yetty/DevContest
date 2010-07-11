<%inherit file="/base.mako"/>

<%def name="title()">Profil</%def>

<%def name="body()">
<h2>Profil</h2>

% if not c.success:
	% if c.errors:
		<ol id="errors">
	%	for error in c.errors:
			<li>${error}</li>
	%	endfor
		</ol>
	% endif
	${h.form(h.url_for(controller="user", action="save"), method="post")}
	<label for="login" class="strong">Login:</label>
	${c.user.login}<br/><br/>
	<label for="password" class="strong">Heslo:</label><br>
	${h.password('password')} ${h.password('cpassword')} <span class="info">(dvakrát pro kontrolu)</span><br/>
	<label for="mail" class="strong">E-mail:</label><br/>
	${h.text('mail', c.user.mail)}<br/>
	<br>

	<label for="fname">Jméno:</label><br/>
	${h.text('fname', c.user.fname)}<br/>
	<label for="lname">Příjmení:</label><br/>
	${h.text('lname', c.user.lname)}<br/>
	<label for="class">Třída:</label><br/>
	${h.text('cls', c.user.cls)}<br/>
	<br/>

	${h.submit('submit', 'Upravit')}

	<p class="info">
		Tučně zvýrazněné položky jsou povinné.
	</p>
	${h.end_form()}
% else:
	<p>Registrace byla úspěšná. Nyní se můžete přihlásit formulářem vlevo.</p>
% endif
</%def>
