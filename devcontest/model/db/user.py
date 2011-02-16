import hashlib

import sqlalchemy as sa
from sqlalchemy import orm

from devcontest.model import meta


users_table = sa.Table('users', meta.metadata,
	sa.Column('id', sa.types.Integer(), primary_key=True),
	sa.Column('login', sa.types.Unicode(), unique=True),
	sa.Column('password', sa.types.Unicode()),
	sa.Column('mail', sa.types.Unicode()),
	sa.Column('fname', sa.types.Unicode()),
	sa.Column('lname', sa.types.Unicode()),
	sa.Column('cls', sa.types.Unicode()),
	sa.Column('rank', sa.types.Integer()),
	sa.Column('admin', sa.types.Boolean()),
)

def hash(password):
	return hashlib.sha256(password).hexdigest()

class User(object):		
	def __init__(self, login, password, mail="", fname="", lname="", cls="", rank=0, admin=False, donthash=False):
		self.login = login
		if donthash:
			self.password = password
		else:
			self.password = hash(password)
		self.mail = mail
		self.fname = fname
		self.lname = lname
		self.cls = cls
		self.rank = rank
		self.admin = admin

	def getName(self):
		return "%s %s" % (self.fname, self.lname)

	def __unicode__(self):
		return "<User("+str(self.id)+": "+self.login+")"

	__str__ = __unicode__

orm.mapper(User, users_table)
