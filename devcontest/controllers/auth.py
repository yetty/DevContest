#!/usr/bin/env python
#-*- coding:utf-8 -*-
import logging

from pylons import request, session, tmpl_context as c, url
from pylons.controllers.util import redirect
from pylons.i18n import _

from devcontest.lib.base import BaseController, render
from devcontest.model import User
from devcontest.model.meta import Session

log = logging.getLogger(__name__)


class AuthController(BaseController):
    def index(self):
        return redirect(url(controller="home", action="index"))

    def signin(self):
        try:
            login = request.params['login']
            password = request.params['password']
        except:
            return self.index()

        user = Session.query(User). \
                filter_by(login=login, password=hash(password)).first()

        if user:
            session['user'] = user
            session.save()
            return self.index()
        else:
            c.error = _('Login failed')
            return render('/home.mako')

    def signout(self):
        try:
            del session['user']
            session.save()
        except:
            pass
        return self.index()
