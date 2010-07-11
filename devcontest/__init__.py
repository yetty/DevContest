import os

def clean():
	for file in os.listdir("data/tmp/"):
		os.remove("data/tmp/"+file)

clean()
