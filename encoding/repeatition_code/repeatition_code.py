import sys
sys.path.append('C:\\Users\\kayan\\Documents\\Projects\\DNA-Storage-alpha')
from simualtors.helper_functions.helper_functions import consensus

#התוכנית מקבלת הודעה ומשכפלת את כל סיבית בה פי 3 ןמחזירה את ההודעה המשוכפלת
def encode(msg,rep,chunk_size):
	encoded_msg = ''
	chunk_list = [msg[i:i+chunk_size] for i in range(len(msg)) if i % chunk_size == 0]
	pad = chunk_size - len(chunk_list[-1])
	if pad > 0:
		chunk_list[-1] += ''.join(chunk_list[-1][-1]* pad)
	for chunk in chunk_list:
		encoded_msg += rep * chunk
	return ''.join(encoded_msg), pad
####################################################
#הפונקציה מקבלת מילה שכל סיבית בה משוכפלת 3 פעמים ואז היא מחלקת אותה לקבוצות של שלושה ושמה אותם ברשימה
#אז בודקת את סכום המספרים בכל קבוצה, אם הסכום גדול מ- 1 אז מוסיפה 1 לרצף ואם ללא אז מוסיפה 0 ומחזירה את ההודעה המקורית.
# a= ra2em lmrat ele bene2sem elha lshosmo.
def decoding(msg_read,rep,chunk_size, pad):
	# break message to repeated chunks
	rep_chunk_s = rep*chunk_size
	list_of_repeated_chunks = [msg_read[i:i+rep_chunk_s] for i in range(len(msg_read)) if i % rep_chunk_s == 0]
	msg_decoded = ''
	for rep_chunk in list_of_repeated_chunks:
		# for letter in chunk - find consensus
		list_of_reps = [rep_chunk[i:i+chunk_size] for i in range(len(rep_chunk)) if i % chunk_size == 0 ]
		consensus_seq = consensus(list_of_reps,chunk_size,rep)
		msg_decoded += consensus_seq
	if pad > 0:
		msg_decoded = msg_decoded[:-pad]
	return msg_decoded

#msg = 'ACACCATTTACC'
#print(msg)
#enc_msg,pad = encode(msg,3,3)
#print(enc_msg)
#dec_msg = decoding(enc_msg,3,3,pad)
#print(dec_msg)
#print(msg == dec_msg)