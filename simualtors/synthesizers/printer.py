
import random
import sys
sys.path.append('C:\\Users\\kayan\\Documents\\Projects\\DNA-Storage-alpha')
from simualtors.helper_functions.helper_functions import add_errors_multiple_inputs
from encoding.bin2dna.two_bits import bin2dna
import numpy as np

def printer(dna, mstk_prsnt, base_in_oligo, num_of_cps):
	# pad with AAAA
	if len(dna) % base_in_oligo == 0:
		padding_length = 0
		dna_padded = dna
	else:
		padding_length = base_in_oligo - len(dna) % base_in_oligo
		padding  = ['A',]* padding_length
		dna_padded = dna + ''.join(padding)
	# split the DNA sequence
	number_of_parts = len(dna_padded) // base_in_oligo
	dna_parts = [dna_padded[i*base_in_oligo:i*base_in_oligo+base_in_oligo] for i in range(number_of_parts)]
	# Add padded indices (limited to 2^12 parts)
	ind_as_int = range(number_of_parts)
	ind_as_binary = [bin(i)[2:].zfill(12) for i in ind_as_int]
	ind_as_DNA = [bin2dna.bin_to_dna_two_bits(i)[0] for i in ind_as_binary]
	oligos = [i+d for i,d in zip(ind_as_DNA,dna_parts)]
	# determine how mnay copies from each part
	mol_cnt = np.random.binomial(num_of_cps, 1.0/len(oligos), len(oligos))
	print(mol_cnt)
	# copy each oligo multiple times (gnerate list of lists)
	dna_mols_as_lists = [[oligo,]*cnt for oligo,cnt in zip(oligos,mol_cnt)]
	dna_mols = [mol for mol_list in dna_mols_as_lists for mol in mol_list]
	# add errors
	dna_mols_with_errors = add_errors_multiple_inputs(dna_mols,mstk_prsnt)
	# shuffle molecules
	shuffled_dna_mols = random.sample(dna_mols_with_errors,len(dna_mols_with_errors))
	return shuffled_dna_mols,padding_length, number_of_parts

#print(printer('CAGTGCAGGATCGGCTTTCTTTCGTCCCTC', 0, 4, 0, 20))