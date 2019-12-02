import sys
sys.path.append('..')
import unittest
from encoding.bin2dna.one_bit import bin2dna

class test_one_bit(unittest.TestCase):
	
	def test_binary_to_dna(self):
		converted = bin2dna.bin_to_dna('00010001')
		self.assertEqual(converted,'AAAGAAAG')
	def test_dna_to_binary(self):
		converted = dna2bin.dna_to_bin('AGCTATCGAGCT')
		self.assertEqual(converted, '010101010101')


if __name__ == '__main__':
	unittest.main()

