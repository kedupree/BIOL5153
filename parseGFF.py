
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


#create a fuction to calculate gc content
def get_gc_content(substring, sig_figs = 2):
	length = len(substring)
	c_count = substring.upper().count('C')
	g_count = substring.upper().count('G')
	gc_content = (c_count + g_count) / length
	return round(gc_content, sig_figs)


def parse_fasta():
	# open the FASTA file
	genome = SeqIO.read('watermelon.fsa', 'fasta')

	# print(genome.seq)
	print(genome)

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
			name =(str(fields[8])[0:11])
	
		# extract the DNA sequence from the genome for this feature
			output = genome[start:end]
	
		# print the DNA sequence for this feature
		# calculate the GC content for this feature, and print it to the screen
			return get_gc_content(output)
			gff.close()

def main():
	genome = parse_fasta() 
	g_c = get_genome_feat()
	print_output(g_c)

	# get the arguments before calling main
	args = get_args()


	# execute the program by calling main
if __name__ == "__main__":
	main()

