window.onload = function() {
	var inline = /\$([^\$]+)\$/g
	var block = /\\\[([^\]]+)\\\]/gm

	var task = document.getElementById('task').innerHTML;
	task = task.replace(inline, "<span class='math'>$1</span>");
	task = task.replace(block, "<div class='math'>$1</div>");

	document.getElementById('task').innerHTML = task;

	if(typeof(jsMath) != 'undefined') {
		jsMath.styles['.typeset']['font-family'] = 'Verdana';
		jsMath.styles['.typeset']['font-size'] = '14px';
		jsMath.Message.Init = function () {};
		jsMath.Font.Message = function () {};
		jsMath.Controls.Button = function () {};
		jsMath.Process(document.getElementById('task'));
	}

	if (document.getElementById('jsMath_button')) {
		document.getElementById('jsMath_button').style.display = "none";
	}
	if (document.getElementById('jsMath_Warning')) {
		document.getElementById('jsMath_Warning').style.display = "none";
	}
}


