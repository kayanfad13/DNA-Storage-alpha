def success(original_msg, output_msg):
	wrong_digit = 0
	i = 0
	for char1,char2 in zip(original_msg,output_msg):
		if original_msg[i] != output_msg[i]:
			wrong_digit += 1
		i += 1
	success_percentage = wrong_digit / len(original_msg) * 100
	return success_percentage