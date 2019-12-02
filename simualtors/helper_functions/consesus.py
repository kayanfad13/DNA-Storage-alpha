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
	cnts = {l:0 for l in 'ACGT'}
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
			cnts = {l:0 for l in 'ACGT'}
	return seq_to_add