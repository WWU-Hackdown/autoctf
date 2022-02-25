import subprocess
from autoctf.args import get_flag_regex
from autoctf import check_flag


def auto_check_flag_in_file_with_grep(file):
	#print(str(get_flag_regex()),file)
	process = subprocess.Popen(['egrep', '-ia' ,get_flag_regex().decode('utf-8') , file],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
	stdout, stderr = process.communicate()
	#print(stdout,stderr)
	return check_flag(stdout)


def auto_check_flag_in_file_with_strings(file):
	#print(str(get_flag_regex()),file)
	process = subprocess.Popen(['strings', file],
                     stdout=subprocess.PIPE, 
                     stderr=subprocess.PIPE)
	stdout, stderr = process.communicate()
	#print(stdout,stderr)
	return check_flag(stdout)