import sys, random
sys.path.append('C:\\Users\\kayan\\Documents\\Projects\\DNA-Storage-alpha')
from simualtors.helper_functions.helper_functions import add_errors_multiple_inputs

# dilution
# dilution rate is a number in [0,1] representing the % of molecules to keep
def dilute(dna_mols,dilution_rate):
	to_keep = random.sample(dna_mols, int(len(dna_mols)*dilution_rate))
	to_return = to_keep * int(1 / dilution_rate)
	return to_return


def sequencer(dna_mols, dillution_rate ,mstk_prsnt):
	# dilute
	diluted_dna = dilute(dna_mols, dillution_rate)
	# add errors
	dna_seqs_with_errors = add_errors_multiple_inputs(diluted_dna,mstk_prsnt)
	return dna_seqs_with_errors

#print(sequencer(['AAACCTTCCC', 'AAAAAGGGCT', 'AAACTGATC', 'AAAGATGATC', 'AAAACCTTCG', 'AAAAAGGGCT', 'AAAAAACAGT', 'AAAAAGGGCT', 'AAAAATGATC', 'AAAACCTTCG', 'AAAAACGCAG', 'AAAACATTCT', 'AAAACCTTCG', 'AAAACCTTCG', 'AAAACATTCT'],1,0))