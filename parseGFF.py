
#parseGFF.py

#! /usr/bin/python3

#set up arg parse
import argparse
import csv


# open the output file
with open('watermelon_gff.out', 'w') as tabout:

	# open the data file
	with open('watermelon_gff', 'r') as gff:

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

def get_args():
#parser description
	parser = argparse.ArgumentParser(description='analyzes gff file, identifies sequence features, extracts sequence features from fsa files, and calculates g/c content')

#choose arguments for parse
	parser.add_argument("gff_file_path", help="the path and name of the gff file")
	parser.add_argument("fsa_file_path", help="the path and name of the fsa file")

#parse the command line arguments
	args = parser.parse_args()

#create a fuction to calculate gc content
def get_gc_content(substring, sig_figs = 2):
	length = len(substring)
	c_count = substring.upper().count('C')
	g_count = substring.upper().count('G')
	gc_content = (c_count + g_count) / length
	return round(gc_content, sig_figs)

#Read in files
gff = open(args.gff_file_path, 'r')
fsa = open(args.fsa_file_path).read()       

# specify the input files
gff_file   = 'watermelon_gff.out'
fasta_file = 'watermelon.fsa'


# open the FASTA file
fasta = open(fasta_file, 'r')

#create a line counter
line_counter = 1
for line in fasta_file:
	if line_counter == 2:
		sequence = line.rstrip('\n')
	line_counter += 1

# open the FASTA file
fasta_contents = fasta.read()
# skip first line in fasta file
header   = fasta_contents.split('\n')[0]
sequence = fasta_contents.split('\n')[1]
fasta.close()


#create the genome in a list form
file_in_list = []
with open(fasta_file) as fasta:
	file_in_list = fasta.read().splitlines()
	file_in_list = fasta.splitlines()

genome = file_in_list[1]

print(genome)

# open the GFF file
gff = open(gff_file, 'r')

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
		print(name, ': ',get_gc_content(output))
		gff.close()

