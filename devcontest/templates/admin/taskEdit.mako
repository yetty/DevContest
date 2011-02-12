<%inherit file="/admin/base.mako"/>

<%def name="title()">${_('Editation of task')} ${c.task.name}</%def>

<%def name="body()">
	<script type="text/javascript">var LANG="html";</script>
	<a href=${h.url_for(controller="admin", action="contest", id=c.contest.id, param=None)} class="back">${_('back to the contest')}</a>
	<h2>${c.task.name}</h2>
	${h.form_start(h.url_for(id=c.id, param="save"), method="post",	multipart=True)}
	${h.textarea(name="description", content=c.task.description, rows=20, cols=114)}
	<table>
		<tr>
			<td class="strong">
			${_('Example of input')}:
			</td>
			<td class="strong">
			${_('Example of output')}:
			</td>
		</tr>
		<tr>
			<td class="strong">
			${h.textarea(name="example_in", id="", content=c.task.example_in, rows=15, cols=55)}
			</td>
			<td class="strong">
			${h.textarea(name="example_out", id="", content=c.task.example_out, rows=15, cols=55)}
			</td>
		</tr>
		<tr>
			<td>		
			${h.submit("submit", _("Submit"))}
			</td>
		</tr>
		
		<tr><td colspan=2><hr></td></tr>

		<script>

		function htmlJudge(id) {
			tr = document.createElement('tr')
			tr.appendChild(document.createElement('td'))

			% if c.contest.mode == 2: # codex
				points = document.createElement('td');
				points.innerHTML = '<input type="text" value="10" name="points['+id+']" size=5>';
				tr.appendChild(points);
			% endif

			file_in = document.createElement('td');
			file_in.innerHTML = '<input type="file" name="file_in['+id+']">';
			tr.appendChild(file_in);

			time_limit = document.createElement('td');
			time_limit.innerHTML = '<input type="text" value="1" name="time_limit['+id+']" size=10>';
			tr.appendChild(time_limit);

			memory_limit = document.createElement('td');
			memory_limit.innerHTML = '<input type="text" value="1024" size=10 name="memory_limit['+id+']">';
			tr.appendChild(memory_limit);

			return tr;
		}

		function addJudge() {
			judges = document.getElementById('judges');

			judges.appendChild(htmlJudge(id));
			id++;
			
			document.getElementById('count').value = id;
		}
		</script>

		% if c.task.source:
			<tr>
				<td>${_('Uploaded source file:')}</td>
				<td><a href="${h.url_for(param='download', num=None)}">
					${_('download')}
					(${c.task.filetype})
				</a></td>
			</tr>
		% endif
		
		<tr>
			<td>${_('Source file:')}</td>
			<td><input type="file" name="source"></td>
		</tr>
		<tr>
			<td>${_('File type:')}</td>
			<td>
				<select name="filetype">
					% if c.task.source:
						<option value="${c.task.filetype}">${c.task.filetype}</option>
					% endif
					
					% for runner in c.runners:
						<option value="${runner.lang}">${_(runner.lang)}</option>
					% endfor
				</select>
			</td>
		</tr>

		<tr><td>&nbsp;</td></tr>
		<tr>
			<td colspan=2>

			<table class="dark">
				<thead>
					<tr>
						<td class="ns"></td>
						% if c.contest.mode == 2: # codex
							<th>${_('Points')}</th>
						% endif
						<th>${_('File in')}</th>
						<th>${_('Time limit (seconds)')}</th>
						<th>${_('Memory limit (kB)')}</th>
						<th>${_('Status')}</th>
					</tr>
				</thead>
				<tbody id="judges">
				<% i = -1 %>
				% for i, judge in enumerate(c.task.judges):
					<tr>
						<td class="ns">
							<img style="cursor:pointer;" src="/remove.png" alt="${_('Remove')}" 
							title="${_('Remove')}"
							ondblclick='remove("${h.url_for(param="deljudge", num=judge.id)}");'>
						</td>
					% if c.contest.mode == 2: # codex
						<td><input type="text" name="points[${i}]"
						value="${judge.points}" size=5></td>
					% endif
						<td><a href="${h.url_for(param="download", num=judge.id)}">
						${judge.name}</a><input type="hidden" name="id[${i}]"
						value="${judge.id}"></td>
						<td><input type="text" name="time_limit[${i}]"
						value="${judge.time_limit}" size=10></td>
						<td><input type="text" name="memory_limit[${i}]"
						value="${judge.memory_limit}" size=10></td>
					% if c.task.source:
						<td>
						<% result = c.runner.exe(c.task, judge, onlyResult=True) %>
						% if result['status']:
							${_("OK")}
						% else:
							${result['message']}
						% endif
						</td>
					% endif
					</tr>
				% endfor
				</tbody>
			</table>


			</td>
		</tr>
		<tr>
			<td><input type="hidden" id="count" name="count" value="0"></td>
			<td style="text-align:right;">
				<img style="cursor:pointer;"
				onclick="javascript:addJudge();" src="/add.png" title="${_('Add judge')}" alt="${_('Add judge')}">
			</td>
	</table>
	<script>
	
	var id = ${i}+1;
	addJudge();
	
	</script>
	${h.submit("submit", _("Submit"))}
	${h.form_end()}
	<%include file="/edit.mako"/>
</%def>
