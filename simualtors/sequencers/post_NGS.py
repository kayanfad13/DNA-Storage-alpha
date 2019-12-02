import random
import sys
import operator
sys.path.append('C:\\Users\\kayan\\Documents\\Projects\\DNA-Storage-alpha')
from simualtors.storage import storage
from encoding.bin2dna.two_bits import dna2bin


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


def post_sequencer(reads,index_length,seq_len,minimal_size,max_ind,padding):
	# split indices
	dna_seqs_and_ind = [(r[:index_length],r[index_length:]) for r in reads]
	# decode indices to binary and to int
	dna_seqs_and_bin_ind = []
	for i,seq in dna_seqs_and_ind:
		int_ind = int(dna2bin.dna_to_bin_two_bits(i),2)
		dna_seqs_and_bin_ind.append((int_ind,seq))
	# sort by index
	sorted_dna_seqs = sorted(dna_seqs_and_bin_ind)
	# work on each index group
	groups_with_ind = {}
	current_group = []
	current_i = sorted_dna_seqs[0][0]
	for i,seq in sorted_dna_seqs:
		if i == current_i:
			current_group.append(seq)
		else:
			# work on current group and then add to current group and update current i
			groups_with_ind[current_i] = current_group
			current_group = [seq,]
			current_i = i
	groups_with_ind[i] = current_group

	generated_sequences = []
	# go over indices and gnerate sequence from groups
	for i in range(max_ind):
		if i in groups_with_ind.keys():
			generated_sequences.append(consensus(groups_with_ind[i],seq_len,minimal_size))
		else:
			generated_sequences.append(''.join(['X',]*seq_len))
	# join all sequences to one long DNA seq (they are already sorted by the index)
	dna_strand = ''.join(generated_sequences)
	if padding > 0:
		dna_strand = dna_strand[0:-padding]
	return dna_strand
#post_sequencer(['AAACCTTCCC', 'AAAAAGGGCT', 'AAACTGATC', 'AAAGATGATC', 'AAAACCTTCG', 'AAAAAGGGCT', 'AAAAAACAGT', 'AAAAAGGGCT', 'AAAAATGATC', 'AAAACCTTCG', 'AAAAACGCAG', 'AAAACATTCT', 'AAAACCTTCG', 'AAAACCTTCG', 'AAAACATTCT'],4,6,5,10)
#post_sequencer(['AAATCCTTCG','AAATCCTTCG','AAATCCTTCG','AAATCCTTCG','AAATCCTTCG','AAATCCTTCG','AAATCCTTCG','AAATCCTTCG','AAACCTTCCC','AAACCTTCCC','AAACCTTCCC','AAACCTTCCC','AAACCTTCCC','AAACCTTCCC','AAACCTTCCC','AAACCTTCCC'],4,6,5,3)


