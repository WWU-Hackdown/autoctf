import os 
import validators

rflag = b'flag{[^{}]*}'
stop = False

def set_flag_regex(rfl):
	global rflag
	rflag = rfl
def get_flag_regex():
	global rflag
	return rflag

def set_stop(s):
	global stop
	stop = s
def get_stop():
	global stop
	return stop

def is_file(s:str):
	return os.path.isfile(s)

def is_url(s:str):
	return validators.url(s)

