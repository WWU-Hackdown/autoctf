from .args import *
import re

def combine(*args):
	r = []
	for a in args:
		if a is not None:
			r.append(a)
	if len(r) == 1:
		return r[0]
	return r

def auto_check_flag(chal):
	from autoctf.web_exploit import auto_check_flag_in_url
	from autoctf.forensic import auto_check_flag_in_file
	from autoctf.args import  is_file, is_url
	if is_file(chal):
		return auto_check_flag_in_file(chal)
	elif is_url(chal):
		return auto_check_flag_in_url(chal)
	else:
		pass

def check_flag(s:str):
	from autoctf.args import get_flag_regex
	m = re.search(get_flag_regex(),s)
	if m:
		print(m.group(0))
		return m.group(0)
	return None