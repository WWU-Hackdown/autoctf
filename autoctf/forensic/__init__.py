from autoctf import combine
from .plain import *

def auto_check_flag_in_file(url):
	return combine(auto_check_flag_in_file_with_grep(url),
	auto_check_flag_in_file_with_strings(url))