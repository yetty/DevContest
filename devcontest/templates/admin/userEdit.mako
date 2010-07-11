<%inherit file="base.mako"/>

<%def name="title()">Profil</%def>

<%def name="body()">
<a href=${h.url_for(controller="admin", action="users", id=None, param=None)} class="back">zpět na seznam</a>
<h2>Editace</h2>

${h.form(h.url_for(controller="admin", action="users", id="save", param=c.user.id), method="post")}
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

<label for="class">Administrátor:</label>
${h.checkbox('admin', checked=c.user.admin)}<br/>


${h.submit('submit', 'Upravit')}
${h.end_form()}
</%def>
