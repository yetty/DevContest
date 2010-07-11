<%inherit file="/base.mako"/>

<%def name="title()">${c.name}</%def>

<%def name="body()">
${c.content | n}
</%def>
