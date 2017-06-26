import sys
import re
from Bio.Seq import Seq

def count_occurrences(p1, sequence, rs):
#	print(sequence.count(rs))
	test = re.split(rs,sequence)
	occurs = 0
	for fragment in test:	
		if p1 in fragment:
			print("found it")
			occurs += 1
	if occurs == 0:
		seq = Seq(p1).reverse_complement()
		seqstr = seq._get_seq_str_and_check_alphabet(seq)
		#print(seqstr)
		for fragment in test:
			if seqstr in fragment:
				print("found it reverse complemented")
				occurs += 1
	
	return occurs

def get_bands(p1, sequence, rs):
	cut_DNA = re.split(rs,sequence)
	bands = ["test"]
	bands = [s for s in cut_DNA if p1 in s]
	band_len = []
	print(bands)
	for band in bands:
		band_len.append(len(band))
	return band_len

print("Restriction site code:")
site = input()
siteu = site.upper()
print("Enter the sequence of your probe:")
probe = input()
probeu = probe.upper()

fname = 'tvirens_genome2.fasta'

with open(fname, "r") as myfile:
	genome = myfile.read().replace('\n','')
	print(count_occurrences(probeu, genome, siteu))
	print(get_bands(probeu, genome, siteu))
