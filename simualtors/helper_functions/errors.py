#import random
	
#def add_errors(input_dna, mstk_prsnt):
#	output_dna = ''
#	list_of_bases = ['A', 'T', 'G', 'C']
#	list_of_mistakes = ['adding', 'changing', 'decreasing']
#	x = random.choice(list_of_mistakes)
#	for i in input_dna:
#		if random.random() < mstk_prsnt:
#			if x == 'adding':
#				output_dna  += i
#				output_dna += random.choice(list_of_bases)
#			elif x == 'changing':
#				random.choice(list_of_bases) != i
#				output_dna += random.choice(list_of_bases)
#			elif x == 'decreasing':
#				continue
#		else:
#			output_dna += i
#	return output_dna

#def add_errors_multiple_inputs(dna_mols, mstk_prsnt):
#	return [add_errors(mol, mstk_prsnt) for mol in dna_mols]