<%namespace name="menu" file="/menu.mako"/>\
<%namespace name="login" file="/login.mako"/>\
<html>
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8" />
    <title>DevContest - ${next.title()}</title>
    <link rel="shortcut icon" href="/icon.png">
    ${h.stylesheet_link("/style.css")}
    ${h.stylesheet_link("/highlighter.css")}
</head>
<body>
<script language="Javascript" type="text/javascript">
function remove(url) {
	window.location.href = url;
}
</script>

% if session.get('flash'):
    <div id="flash">
        ${session.get('flash')}
    <%
        del session['flash']
        session.save()
    %>
    </div>

% elif session.get('error_flash'):
    <div id="error">
        ${session.get('error_flash')}
    <%
        del session['error_flash']
        session.save()
    %>
     </div>
% endif

    <div id="header">
    <h1><a href=${h.url_for(controller="home", action="index")}>DevContest</a></h1>
    </div>
    <div id="left_nav">
    <div id="menu">
        ${menu.menu()}
    </div>

    <div id="login_box">
        ${login.login_box()}
    </div>
    <br/>
    <a href="http://python.org" alt="Python"><img src="/python-powered-w-70x28.png" alt="Python powered"/></a>
    </div>

    <div id="content">
        ${next.body()}
    </div>
</body>
</html>
