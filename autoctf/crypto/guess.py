from autoctf import check_flag
from tqdm import tqdm 
import numpy as np

def auto_check_flag_in_data_by_guess_shift(data):
	try:
		for j in tqdm(range(1,np.max(data))):
			try:
				s = ""
				for e,i in enumerate(data):
					s += chr(i-e%j)
				check_flag(s.encode())
			except:
				pass
	except:
		pass