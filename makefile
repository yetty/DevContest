# Himio, 2012
#
# Author: Juda Kaleta
# License: GNU GPL v3
#


# VENV PATHS
PYTHON=./venv/bin/python
PIP=./venv/bin/pip

# PROJECT PATHS
MANAGE=./devcontest/manage.py

localhost:
	${PYTHON} ${MANAGE} runserver

freeze:
	rm -f requirements.txt
	${PIP} freeze > requirements.txt

clean:
	rm -f devcontest/**/*.pyc

