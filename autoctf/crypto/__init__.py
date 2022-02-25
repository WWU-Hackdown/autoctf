from autoctf import combine
from autoctf.crypto.guess import auto_check_flag_in_data_by_guess_shift
from autoctf.crypto.pipes import auto_check_flag_in_data_by_pipes


def auto_check_flag_in_data(data):
	return combine(auto_check_flag_in_data_by_guess_shift(data),
			auto_check_flag_in_data_by_pipes(data)
	)