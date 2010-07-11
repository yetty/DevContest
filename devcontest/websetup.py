"""Setup the DevContest application"""
import logging

from devcontest import model
from devcontest.config.environment import load_environment
from devcontest.model import meta

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
	"""Place any commands to setup quickwiki here"""
	load_environment(conf.global_conf, conf.local_conf)

	# Create the tables if they don't already exist
	log.info("Creating tables...")
	meta.metadata.create_all(bind=meta.engine)
	log.info("Successfully set up.")

	admin = {}
	admin['login'] = "admin"
	# through model.db.user.hash()
	admin['password'] = "8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918"
	admin['mail'] = ""
	admin['fname'] = "Administrator"
	admin['lname'] = ""
	admin['class'] = ""
	admin['rank'] = 100
	admin['admin'] = True

	log.info("Adding front page data...")
	user = model.User(
		admin['login'], admin['password'], admin['mail'],
		admin['fname'], admin['lname'], admin['class'],
		admin['rank'], admin['admin'], True
	)
	meta.Session.add(user)

	exs = [
		model.Runner('c',    compile='gcc -o %o %f', 			  run='%f'),
		model.Runner('cpp',  compile='g++ -o %o %f', 			  run='%f'),
		model.Runner('pas',  compile='fpc %f -o%o', 			  run='%f'),
		model.Runner('java', compile='gcj -o %o --main=%c %f',  run='%f'),
		model.Runner('py',   compile='', 						  run='python %f'),
		model.Runner('php',  compile='', 						  run='php %f'),
		model.Runner('rb',   compile='', 						  run='ruby %f'),
	]

	for ex in exs:
		meta.Session.add(ex)

	meta.Session.commit()
	log.info("Successfully set up.")
