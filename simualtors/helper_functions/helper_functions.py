import random
	
def add_errors(input_dna, mstk_prsnt):
	output_dna = ''
	list_of_bases = ['A', 'T', 'G', 'C']
	list_of_mistakes = ['adding', 'changing', 'decreasing']
	for i in input_dna:
		x = random.choice(list_of_mistakes)
		if random.random() < mstk_prsnt:
			if x == 'adding':
				output_dna  += i
				output_dna += random.choice(list_of_bases)
			elif x == 'changing':
				random.choice(list_of_bases) != i
				output_dna += random.choice(list_of_bases)
			elif x == 'decreasing':
				continue
		else:
			output_dna += i
	return output_dna

def add_errors_multiple_inputs(dna_mols, mstk_prsnt):
	return [add_errors(mol, mstk_prsnt) for mol in dna_mols]

def verify_group(group,seq_len,minimal_size):
	good_group = []
	for seq in group:
		if len(seq) == seq_len:
			good_group.append(seq)
	if len(good_group) >= minimal_size:
		return good_group
	else:
		return [''.join(['X',]*seq_len),]

def consensus(group,seq_len,minimal_size):
	cnts = {l:0 for l in 'ACGTX'}
	seq_to_add = ''
	verified = verify_group(group,seq_len,minimal_size)
	if verified[0] ==  ''.join(['X',]*seq_len):
		seq_to_add = verified[0]
	else:
		for i in range(seq_len):
			for seq in verified:
				cnts[seq[i]] += 1
			max_letter = max(cnts.items(),key = lambda pair: pair[1])[0]
			seq_to_add += max_letter
			cnts = {l:0 for l in 'ACGTX'}
	return seq_to_add