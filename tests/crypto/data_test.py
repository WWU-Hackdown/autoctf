#!/usr/bin/python3


from autoctf import get_found_flags
from autoctf.crypto import auto_check_flag_in_data
from autoctf.crypto.guess import auto_check_flag_in_data_by_guess_shift
from autoctf.crypto.pipes import auto_check_flag_in_data_by_pipes


def test_guess():
	data = [102, 109, 99, 106, 127, 53, 116, 95, 122, 113, 120, 118, 100, 55, 51, 103, 57, 128,]
	auto_check_flag_in_data_by_guess_shift(data)
	assert b"flag{0n_your_13f7}" in get_found_flags()

def test_b64():
	data = "eyJmbGFnIjoiZmxhZ3tmbDQ1a19zMzU1MTBuX2MwMGsxM3NfNHIzXzFuNTNjdXJlfSJ9.YFLMhA.xt_8C0BrPHl2HDm9yIRffDhK7Ow"
	auto_check_flag_in_data(data)
	assert b'flag{fl45k_s35510n_c00k13s_4r3_1n53cure}' in get_found_flags()

def test_chain():
	data=[65,141,40,66,144,40,67,70,40,66,70,40,65,141,40,63,63,40,67,64,40,67,64,40,66,62,40,65,67,40,63,61,40,66,66,40,66,63,40,64,65,40,64,61,40,66,142,40,66,64,40,64,67,40,64,66,40,63,71]
	#print(pipe_to_base64(pipe_str_combine(pipe_to_chr(pipe_to_hex(pipe_str_combine(pipe_to_chr(pipe_to_octal(data))))))))
	auto_check_flag_in_data_by_pipes(data)
	assert b"flag{mmm_p@$ta}" in get_found_flags()




if __name__ == "__main__":
    test_guess()
    test_chain()
    test_b64()
    print("Everything passed")