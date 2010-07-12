<%inherit file="base.mako"/>

<%def name="title()">${_('Profile')}</%def>

<%def name="body()">
<a href=${h.url_for(controller="admin", action="users", id=None, param=None)} class="back">${_('back to the list')}</a>
<h2>${_('Editation of profile')}</h2>

${h.form(h.url_for(controller="admin", action="users", id="save", param=c.user.id), method="post")}
<label for="login" class="strong">${_('Login')}:</label>
${c.user.login}<br/><br/>
<label for="password" class="strong">${_('Password')}:</label><br>
${h.password('password')} ${h.password('cpassword')} <span class="info">(${_('twice for sure')})</span><br/>
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

<label for="class">${_('Administrator')}:</label>
${h.checkbox('admin', checked=c.user.admin)}<br/>


${h.submit('submit', _('Submit'))}
${h.end_form()}
</%def>
