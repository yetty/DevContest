import cgi

from paste.urlparser import PkgResourcesParser
from pylons import request
from pylons.controllers.util import forward
from pylons.middleware import error_document_template
from webhelpers.html.builder import literal

from devcontest.lib.base import BaseController, render

class ErrorController(BaseController):

	"""Generates error documents as and when they are required.

	The ErrorDocuments middleware forwards to ErrorController when error
	related status codes are returned from the application.

	This behaviour can be altered by changing the parameters to the
	ErrorDocuments middleware in your config/middleware.py file.

	"""
	def index(self):
		return self.document

	def document(self):
		"""Render the error document"""
		resp = request.environ.get('pylons.original_response')
		content = literal(resp.body) or cgi.escape(request.GET.get('message', ''))
		page = error_document_template % \
		dict(prefix=request.environ.get('SCRIPT_NAME', ''),
		code=cgi.escape(request.GET.get('code', str(resp.status_int))),
		message=content)
		#return page
		return render('error.mako')

	def img(self, id):
		"""Serve Pylons' stock images"""
		return self._serve_file('/'.join(['media/img', id]))

	def style(self, id):
		"""Serve Pylons' stock stylesheets"""
		return self._serve_file('/'.join(['media/style', id]))

	def _serve_file(self, path):
		"""Call Paste's FileApp (a WSGI application) to serve the file
		at the specified path
		"""
		request.environ['PATH_INFO'] = '/%s' % path
		return forward(PkgResourcesParser('pylons', 'pylons'))
