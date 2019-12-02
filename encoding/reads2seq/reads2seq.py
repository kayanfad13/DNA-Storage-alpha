#def read(seq_dna):
#	dna_seq_read = seq_dna
#	return dna_seq_read
################################################################################
#def dilutor (dna_mol, n, ec, replicate):
#	import random
#	shuffled = random.shuffle(dna_mol)
#	list_dna_mol = []
#	list_of_bases = ['A', 'T', 'G', 'C']
#	list_of_mistakes = ['adding', 'changing', 'decreasing']
#	x = random.choice(list_of_mistakes)
#	for times in range (0,n) :
#		for parts in dna_mol:
#			while replicate != 0:
#				for i in parts:
#					if i == 'A':
#						y = random.random()
#						if y < ec:
#							if x == 'adding':
#									new_dna_mol += i
#									new_dna_mol += random.choice(list_of_bases)
#							elif x == 'changing':
#								random.choice(list_of_bases) != i
#								new_dna_mol += random.choice(list_of_bases)
#							elif x == 'decreasing':
#								continue 
#						else:
#							new_dna_mol += 'A'
#					if i == 'T':
#						y = random.random()
#						if y < ec:
#							if x == 'adding':
#									new_dna_mol += i
#									new_dna_mol += random.choice(list_of_bases)
#							elif x == 'changing':
#								random.choice(list_of_bases) != i
#								new_dna_mol += random.choice(list_of_bases)
#							elif x == 'decreasing':
#								continue
#						else:
#							new_dna_mol += 'T'
#					if i == 'C':
#						y = random.random()
#						if y < ec:
#							if x == 'adding':
#									new_dna_mol += i
#									new_dna_mol += random.choice(list_of_bases)
#							elif x == 'changing':
#								random.choice(list_of_bases) != i
#								new_dna_mol += random.choice(list_of_bases)
#							elif x == 'decreasing':
#								continue
#						else:
#							new_dna_mol += 'C'
#					if i == 'G':
#						y = random.random()
#						if y < ec:
#							if x == 'adding':
#									new_dna_mol += i
#									new_dna_mol += random.choice(list_of_bases)
#							elif x == 'changing':
#								random.choice(list_of_bases) != i
#								new_dna_mol += random.choice(list_of_bases)
#							elif x == 'decreasing':
#								continue
#						else:
#							new_dna_mol += 'G'
#					replicate -= 1
#				list_dna_mol.append (new_dna_mol)
#	return (list_dna_mol)
####################################################################################################

