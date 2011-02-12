import datetime

import sqlalchemy as sa
from sqlalchemy import func, orm

from devcontest.model import meta
from devcontest.model.db.user import *
from devcontest.model.db.source import *
from devcontest.model.meta import Session

contests_table = sa.Table('contests', meta.metadata,
	sa.Column('id', sa.types.Integer(), primary_key=True),
	sa.Column('name', sa.types.Unicode()),
	sa.Column('is_running', sa.types.Boolean(), default=False),
	sa.Column('timeStart', sa.types.DateTime()),
	sa.Column('mode', sa.types.Integer(), default=0),
	sa.Column('results', sa.types.Boolean(), default=True),
)

class Contest(object):
	timeStart = None
	
	modes = ['normal', 'pilsprog', 'codex'] 

	def __init__(self, name, is_running=False, pilsprog_mode=False):
		self.name = name
		self.is_running = is_running
		self.pilsprog_mode = pilsprog_mode
		if is_running:
			self.timeStart = self.getTimeStart()

	def start(self):
		self.is_running = True
		Session.execute(sources_table.delete().where(sources_table.c.contest_id==self.id))
		self.timeStart = self.getTimeStart()

	def stop(self):
		self.is_running = False

	def getTimeStart(self):
		return datetime.datetime.now()

	def getRank(self, showAdmin=False):
		ret = []

		if showAdmin:
			users = Session.query(User)
		else:
			users = Session.query(User).filter_by(admin=False)

		for user in users:
			points = 0
			time = 0
			count = Session.query(Source).filter_by(user_id=user.id, contest_id=self.id, status=True).count()
			points = Session.query(func.sum(Source.points)).filter_by(user_id=user.id, contest_id=self.id).scalar()
			if count>0:
				if self.mode == 1: # pilsprog
					sources = Session.query(Source).filter_by(user_id=user.id, contest_id=self.id, status=True).all()

					time = self.timeStart
					count = 0

					for source in sources:
						time = time+(source.datetime-self.timeStart)
						count = count+1
					time = time-self.timeStart
				else:
					last, = Session.query(Source.datetime).filter_by(user_id=user.id, contest_id=self.id, status=True).order_by(sources_table.c.datetime.desc()).first()
					time = last - self.timeStart
			if count > 0 or (points > 0 and self.mode == 2): # codex
				ret.append({'user':user, 'count':count, 'points':points, 'time':time})
	

		
		if self.mode == 2: #codex
			ret = sorted(ret, key = lambda user: user['points'], reverse=True)
		else:
			ret = sorted(ret, key = lambda user: user['time'])
			ret = sorted(ret, key = lambda user: user['count'], reverse=True)
		
		return ret
	
	def __unicode__(self):
		return "<Contest("+str(self.id)+": "+self.name+")"

	__str__ = __unicode__

orm.mapper(Contest, contests_table)
