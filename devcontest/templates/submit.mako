<%inherit file="base.mako"/>

<%def name="title()">Odeslat řešení</%def>

<%def name="body()">

<script language="javascript" type="text/javascript" src="/edit_area/edit_area_full.js"></script>
<script language="javascript" type="text/javascript">
editAreaLoader.init({
    id : "source_code",       // textarea id
    min_height: 500,
    min_width: 600,
    replace_tab_by_spaces: 4,
    syntax: "python",          // syntax to be uses for highgliting
    start_highlight: true      // to display with highlight mode on start-up
});
</script>


    ${h.form_start(h.url_for(controller="submit", action="submit"), method="post", multipart=True)}
        ${h.field("Úloha", h.select("task", "", c.tasks))}
        ${h.field("Zdrojový kód", h.textarea("source_code"))}
        ${h.field("Anebo soubor", h.file("file"))}
        ${h.field("", h.submit("submit", "Odeslat řešení"))}
    ${h.form_end()}
</%def>

