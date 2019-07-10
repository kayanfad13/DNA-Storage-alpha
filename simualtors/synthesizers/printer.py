def print_dna(seq):
	return [seq for _ in range(10)]
#:it recieve a dna srtrig (str) that is the seq and a parameter a (float)
#:a= mistakes percentage
#:seq= dna to print
#:printed_dna= where the dna would be printed
#:it gives a random number to every base and if:
#:it was under the mistake percentage then it'll replace it
#:- it picks randomly from the mistake list:
#:-- if it picks adding then it'll add that base and it'll add a random base
#:-- if it picks changing it'll add a base that is not like the previous one
#:-- if it picks decreasing it'll continue and not add anything
#:if the number is bigger than the mistake percentage then it will add the original base
#: the function print it 100 times

def printer(dna, a):
	printed_dna = ''
	import random
	list_of_bases = ['A', 'T', 'G', 'C']
	list_of_mistakes = ['adding', 'changing', 'decreasing']
	x = random.choice(list_of_mistakes)
	for times in range (100):
		for parts in dna:
			for i in parts:
				y = random.random()
				if y < a:
					if x == 'adding':
						printed_dna += i
						printed_dna += random.choice(list_of_bases)
					elif x == 'changing':
						random.choice(list_of_bases) != i
						prinrted_dna += random.choice(list_of_bases)
					elif x == 'decreasing':
						continue
			else:
				printed_dna += i
	return printed_dna