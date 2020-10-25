import sys
from os import path

def path_init():
	path_list=['/home/pi/repos/PyTools/Email/', \
		'/home/pi/repos/PyTools/Socket/' \
	]
	
	for include_path in path_list:
		if path.exists(include_path):
			sys.path.append(include_path)
		else:
			print('[ERROR] '+include_path+' not found')
