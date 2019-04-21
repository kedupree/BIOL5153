
#parseGFF.py

#! /usr/bin/python3

#set up arg parse
import argparse
import csv
from Bio import SeqIO

# specify the input files
gff_file_path   = 'watermelon.gff'
fasta_file_path = 'watermelon.fsa'

def get_args():
#parser description
	parser = argparse.ArgumentParser(description='analyzes gff file, identifies sequence features, extracts sequence features from fsa files, and calculates g/c content')

#choose arguments for parse
	parser.add_argument("gff_file_path", help="the path and name of the gff file")
	parser.add_argument("fsa_file_path", help="the path and name of the fsa file")

#parse the command line arguments
	return parser.parse_args()


def parse_gff():
# open the output file
	with open('watermelon_gff.out', 'w') as tabout:

	# open the data file
		with open(args.gff_file_path, 'r') as gff:

		# create a csv reader object
			csvreader = csv.reader(gff, delimiter='\n')

			header = next(reader)

		# read in the file, line by line
			for line in reader:

			# skip blank lines
				if not line:
					continue

				else:
					linewriter = csv.writer(tabout, delimiter='\n', quotechar='"')
					linewriter.writerow(line)

def parse_fasta():
	# open the FASTA file
	genome = SeqIO.read('watermelon.fsa', 'fasta')

	# print(genome.seq)
	return genome.seq

def get_genome_feat():
	# open the GFF file
	gff = open('watermelon_gff.out', 'r')

	# read GFF file, line by line
	for line in gff:
		# skip blank lines
		if not line:
			continue
		else:
		# remove line breaks
			line = line.rstrip('\n')
	
		# sequence, source, feature, begin, end, length, strand, phase, attributes = line.split('\t')
			fields = line.split('\t')
	
		# get fields[3] and fields[4]
			start = (int(fields[3])-1)	
			end = (int(fields[4])-1)
				
		# extract the DNA sequence from the genome for this feature
			output = genome[start:end]
			return output
	gff.close()

#create a fuction to calculate gc content
def get_gc_content(output, sig_figs = 2):
	length = len(output)
	c_count = output.upper().count('C')
	g_count = output.upper().count('G')
	gc_content = (c_count + g_count) / length
	return round(gc_content, sig_figs)

def rev_compliment():
	 genome = SeqIO.read('watermelon.fsa', 'fasta')
	 
	 for line in gff:
		# skip blank lines
		if not line:
			continue
		else:
		# remove line breaks
			line = line.rstrip('\n')
	
		# sequence, source, feature, begin, end, length, strand, phase, attributes = line.split('\t')
			fields = line.split('\t')
			strand = fields[6]
			
		#get reverse compliment of - strands	
			if strand == '-':
				return output.reverse_complement


def main():
	genome = parse_fasta() 
	output = get_genome_feat()
	g_c = get_gc_content()
	rev_compliment = rev_compliment()
	print_output(output, g_c, rev_compliment)

	# get the arguments before calling main
	args = get_args()


	# execute the program by calling main
if __name__ == "__main__":
	main()

