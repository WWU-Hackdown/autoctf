from autoctf import check_flag
from autoctf.web_exploit.html_scan import check_flag_in_html
import base64
from tqdm import tqdm


def pipe_str_combine(data):
	for s in [" ",",",";",":",""]:
		if s in data:
			return ''.join(data).split(s)
	return data

def pipe_to_str(data):
	nd = []
	for d in data:
		nd.append(str(d))
	return nd



def pipe_to_chr(data):
	nd = []
	for d in data:
		nd.append(chr(d))
	return nd

def pipe_to_octal(data):
	nd = []
	for d in data:
		nd.append(int(str(d), 8))
	return nd

def pipe_to_hex(data):
	nd = []
	for d in data:
		nd.append(int(str(d),16))
	return nd

def pipe_to_int(data):
	nd = []
	for d in data:
		nd.append(int(str(d)))
	return nd

def pipe_to_chr(data):
	nd = []
	for d in data:
		nd.append(chr(d))
	return nd

def pipe_to_base64(data):
	p = data
	try:
		p = base64.b64decode(data + b'=' * (-len(data) % 4))
	except:
		p = base64.b64decode(''.join(data) + '=' * (-len(data) % 4))
	return p

def pipe_to_base32(data):
	p = data
	try:
		p = base64.b32decode(data+ b'=' * (-len(data) % 8))
	except:
		p = base64.b32decode(''.join(data)+ '=' * (-len(data) % 8))
	#print(p)
	return p


def auto_check_flag_in_data_by_pipes(data,layer=10):
	try:
		check_flag(''.join(pipe_to_str(data)).encode())
	except:
		check_flag(data)
	if layer ==0:
		return data
	for p in tqdm([pipe_to_base32,pipe_to_base64,pipe_to_chr,pipe_to_octal, pipe_to_chr,pipe_to_int,pipe_to_hex,pipe_str_combine,pipe_to_str], disable = layer!= 10):
		try:
			auto_check_flag_in_data_by_pipes(p(data),layer-1)
		except:
			pass
	return data