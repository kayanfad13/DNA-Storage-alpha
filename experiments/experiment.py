#print('enter your message')
#	input = (msg)
#	print('encode message')
#	encoded_msg = repeatition_code.repeatition_code(msg)
#	print('convert to dna')
#	dna = bin2dna. bin_to_dna_two_bits(encoded_msg)
#	print('synthesize dna')
#	printed_dna = printer.printer(dna,a)
#	print('store dna')
#	stored_dna = storage.store(printed_dna,b)
#	print('sequence dna')
#	seq_dna = NGS.dna_sequence(stored_dna)
#	print('infer dna sequence')
#	dna_seq_read = reads2seq.read(seq_dna)
#	print('convert to binary')
#	msg_read = dna2bin. dna_to_bin_two_bits(dna_seq_read)
#	print('decode message')
#	msg_decoded = repeatition_code.decode(msg_read)
#	print('done:')
#	print(msg,msg_decoded)
##############################################################
import sys
sys.path.append('C:\\Users\\kayan\\Documents\\Projects\\DNA-Storage-alpha')
from encoding.repeatition_code import repeatition_code
from encoding.bin2dna.two_bits import dna2bin
from encoding.bin2dna.two_bits import bin2dna
from simualtors.synthesizers import printer
from simualtors.storage import storage
from simualtors.sequencers import NGS
from simualtors.sequencers.post_NGS import post_sequencer
from encoding.reads2seq import reads2seq
from encoding.repeatition_code import percentage_of_success
import random

def main(msg,rep,chunk_size,mstk_prsnt,oligo_len,num_of_cps, dillution_rate):
	print('message: {}'.format(msg))
	print('translating to dna')
	translated_msg,pad_bin_to_dna = bin2dna.bin_to_dna_two_bits(msg)
	print('DNA message: {}'.format(translated_msg))
	print('adding error correction code')
	msg_with_error_correction_code, pad_rep = repeatition_code.encode(translated_msg,rep,chunk_size)
	print('DNA message with EC: {}'.format(msg_with_error_correction_code))
	print('synthesizing the dna strands')
	dna_mols, pad_printer, max_ind = printer.printer(msg_with_error_correction_code, mstk_prsnt, oligo_len, num_of_cps)
	print('synthesized DNA molecules: {}'.format(dna_mols))
	print('storing dna')
	stored_dna_mols = storage.storage_all(dna_mols, mstk_prsnt)
	print('stored DNA molecules: {}'.format(stored_dna_mols))
	print('sequencing the dna mols and returning the dna reads')
	dna_reads = NGS.sequencer(stored_dna_mols, dillution_rate ,mstk_prsnt)
	print('DNA reads: {}'.format(dna_reads))
	print('joining all the reads to one message')
	msg_in_dna_post_storage = post_sequencer(dna_reads,6,oligo_len,3,max_ind,pad_printer)
	print('DNA message: {}'.format(msg_in_dna_post_storage))
	print('error correction')
	decoded_DNA_msg = repeatition_code.decoding(msg_in_dna_post_storage,rep,chunk_size,pad_rep)
	print('decoding the dna message to binary message')
	print('DNA message after EC: {}'.format(decoded_DNA_msg))
	decoded_msg = dna2bin.dna_to_bin_two_bits(decoded_DNA_msg)
	print('done :)')
	print(msg == decoded_msg)
	print(msg,decoded_msg)

if __name__ == '__main__':
	l = 100
	rep = 3
	chunk_size = 2
	mstk_prsnt = 0.1
	oligo_len = 10
	num_of_cps = 2000*l/oligo_len
	dillution_rate = 1
	msg = ''.join(random.choices('01',k=l))
	main(msg,rep, chunk_size,mstk_prsnt,oligo_len,num_of_cps, dillution_rate)
