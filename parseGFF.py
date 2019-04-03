#parseGFF.py

#! /usr/bin/python3

#Read in files
gff = open('watermelon.gff', 'r')

#open fsa file as list
with open('watermelon.fsa') as f:
    lines = f.read().splitlines()

#create a variable to hold sequence
genome = str(lines[1:])
print(len(genome))
       
#create a fuction to calculate gc content
def get_gc_content(substring, sig_figs = 2):
	length = len(substring)
	c_count = substring.upper().count('C')
	g_count = substring.upper().count('G')
	gc_content = ((c_count + g_count) / length)*100
	print(round(gc_content, sig_figs))

#Read gff file line by line
#Remove line breaks and split on tabs
for line in gff:
	line = line.rstrip('\n')
	fields = line.split('\t')
#Identify start, stop and names adjusting for number scheme
	start = (int(fields[3])-1)	
	end = (int(fields[4])-1)
	name =(str(fields[8])[0:11])
	get_gc_content(genome[start:stop])

