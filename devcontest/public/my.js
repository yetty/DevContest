// initialisation
var e = document.getElementsByTagName("textarea");

for(var i=0;i<e.length;i++){
	if (e[i].lang!="") {
		l = e[i].lang;

		editAreaLoader.init({
			id: e[i].id	// id of the textarea to transform
			,start_highlight: true	// if start with highlight
			,allow_resize: "both"
			,allow_toggle: false
			,word_wrap: true
			,language: "en"
			,replace_tab_by_spaces: 4
			,syntax: l
			,toolbar: "undo, redo, |, highlight, change_smooth_selection"
			,show_line_colors: true
		});
	}
}
