
#parseGFF.py

#! /usr/bin/python3

#set up arg parse
import argparse

#parser description
parser = argparse.ArgumentParser(description='analyzes gff file, identifies sequence features, extracts sequence features from fsa files, and calculates g/c content')

#choose arguments for parse
parser.add_argument("gff_file_path", help="the path and name of the gff file")
parser.add_argument("fsa_file_path", help="the path and name of the fsa file")


#parse the command line arguments
args = parser.parse_args()

#Read in files
gff = open(args.gff_file_path, 'r')
fsa = open(args.fsa_file_path).read()       
#create a fuction to calculate gc content
def get_gc_content(substring, sig_figs = 2):
	length = len(substring)
	c_count = substring.upper().count('C')
	g_count = substring.upper().count('G')
	gc_content = (c_count + g_count) / length
	return round(gc_content, sig_figs)

#Read gff file line by line
#Remove line breaks and split on tabs
for line in gff:
	line = line.rstrip('\n')
	fields = line.split('\t')
#Identify start, stop and names adjusting for number scheme
	start = (int(fields[3])-1)	
	end = (int(fields[4])-1)
	name =(str(fields[8])[0:11])
	output = fsa[start:end]
	print(name, ': ',get_gc_content(output))
gff.close()

