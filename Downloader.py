#!/usr/bin/python3

"""
Script to download urls from specified file
"""

__author__      =           'Donald Whitfield'
__copyright__   =           '(c) 2021, S-Box Security'
__version__     =           '2.0.0'
__maintainer__  =           'Donald Whitfield'
__email__       =           'donaldwhitfield@icloud.com'
__status__      =           'Development'

import subprocess

file_list = list()
file = ""

cmd = '/usr/local/bin/youtube-dl'
#run_command = subprocess.call([cmd, file])

urlfile = open ("url_list.txt", "r")
file_list = urlfile.readlines()

for file in file_list:
	print(file)
	subprocess.call([cmd, file])
	
urlfile.close()
