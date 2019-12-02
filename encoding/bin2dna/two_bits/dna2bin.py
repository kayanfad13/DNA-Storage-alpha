# פונקציה שמקבלת רצף דנ"א וקוראת ומפענחת אותו להודעה בבסיס בינארי
def dna_to_bin_two_bits(dna_seq_read):
	msg_read = ''
	reader = {'A':'00', 'C':'01', 'T':'10', 'G':'11', 'X':'XX'}
	for char in dna_seq_read:
		msg_read += reader[char]
	return msg_read
