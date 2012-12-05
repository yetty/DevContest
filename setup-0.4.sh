#!/usr/bin/env bash

path="/usr/share/devcontest"


# create root directory
if [ -d $path ]; then
	echo ">> There is some old installation. Cleaning..."
	cd $path

	rm -fvr data/sessions data/tmp
	rm -v *.egg
else
	mkdir -v $path
fi

echo ">> Opening $path"
cd $path

echo ">> Creating base data structure"
mkdir -v data data/pages data/sessions data/sources data/tasks data/templates data/tmp data/judges

echo ">> Running easy_install"
easy_install --always-unzip -O2 DevContest
pip install webob==1.0.8

echo ">> Creating config"
paster make-config DevContest config.ini

echo ">> Setting application"
paster setup-app config.ini

echo ">> Creating special user"
adduser -p python python
useradd -p python python
echo "ALL     ALL = (python) NOPASSWD:ALL" >> /etc/sudoers


echo "
>>>
>> Installation was finished.
>>>

>> You can edit setting by:

		vim $path/config.ini

>> Start serve by:

		cd $path
		paster serve config.ini

"
