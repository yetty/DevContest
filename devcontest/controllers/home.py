import logging


from devcontest.lib.base import BaseController, render

log = logging.getLogger(__name__)


class HomeController(BaseController):
    def index(self):
        return render('/home.mako')
