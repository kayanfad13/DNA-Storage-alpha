#def bin_to_dna(msg):
	#dna = ""
	#translator = {'0':'A', '1':'G'}
	#for digit in msg:
		#dna += translator[digit]
	#return dna
##########################################################################
#פונקציה שמקבלת הודעה, עושה ממנה רשימה של כל שתי סיביות ביחד, מציבה את ההודעה בתוך משתנה שקוראים לו דנ"א ומחזירה את רצף הדנ"א
def bin_to_dna_two_bits(msg):
	dna = ''
	pad = False
	translator = {'00':'A', '01':'C', '10':'T', '11':'G'}
	list = [msg[i:i+2] for i in range(len(msg)) if i % 2 == 0]
	if len(list[-1]) == 1:
		list[-1] += '0'
		pad = True
	for char in list:
		dna += translator[char]
	return dna, pad
#################################################################################
#def bin_to_dna_one_bit(encoded_msg):
#	dna = ''
#	for i in encoded_msg:
#		if encoded_msg[i] == 0 and encoded_msg[i - 1] == 0:
#			dna += 'A'
#		elif encoded_msg [i] == 0 and encoded_msg[i - 1] == 1:
#			dna += 'C'
#		elif encoded_msg [i] == 1 and encoded_msg[i - 1] == 1:
#			dna += 'T'
#		else:
#			dna += 'G'
#	return dna