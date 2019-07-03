def dna_to_bin(dna):
	msg = ""
	reader = {'A':'0', 'G':'1', 'C':'0', 'T':'1'}
	for letter in dna:
		msg =+ reader[letter]
	return msg