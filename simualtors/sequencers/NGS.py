#def dna_sequence(dna_mol):
	#return dna_mol
###################################################################
def storage(printed_dna, b):
	stored_dna = ''
	import random
	list_of_bases = ['A', 'T', 'G', 'C']
	list_of_mistakes = ['adding', 'changing', 'decreasing']
	x = random.choice(list_of_mistakes)
	for i in printed_dna:
		if random() < b:
			if x == 'adding':
				stored_dna += i
				stored_dna += random.choice(list_of_bases)
			elif x == 'changing':
				random.choice(list_of_bases) != i
				stored_dna += random.choice(list_of_bases)
			elif x == 'decreasing':
				continue
		else:
			stored_dna += i
	return stored_dna
#######################################################################
def sequencer(stored_dna):
	seq_dna = stored_dna
	return seq_dna
#######################################################################
def dna_sequence(stored_dna,c):
	seq_dna = ''
	for sequece in stored_dna:
		if len(sequece) == c:
			for i in sequence:
				if i == 'A':
					A_count += 1
				elif i == 'T':
					T_count += 1
				elif i == 'C':
					C_count += 1
				else:
					G_count += 1
				i += 1
				for times in sequece:
					if A_count > C_count and A_count > T_count and A_count > G_count:
						seq_dna += 'A'
					elif T_count > C_count and T_count > A_count and T_count > G_count:
						seq_dna += 'T'
					elif C_count > T_count and C_count > A_count and C_count > G_count:
						seq_dna += 'C'
					else:
						seq_dna += 'G'
	return seq_dna