import os
from os import path
import sys
import argparse
#infile=open(sys.argv[1])

#os.system("cd /aw19/") # Add your project directory in here
#path = sys.argv[1].split('/')[0] + "/" + sys.argv[1].split('/')[1] + "/" + sys.argv[1].split('/')[2]

# input data
parser = argparse.ArgumentParser(
	description = 'Simply taking a multi fasta file of contigs and output each contig into seperate fasta files',
	usage = 'Multifasta_to_Single [options] multifastafile')
parser.add_argument('multifastafile', help='A Multi fasta file')
options = parser.parse_args()

opened = False #Assume outfile is not open
with open(options.multifastafile) as data:
   
    for line in data:
        if line[0] == ">": #if line starts with ">"
            if(opened):
                outfile.close() # Will close the outfile if it'sopen (look below and follow loop)
            opened = True #Set opened to TRue to represent an opened outfile
            contig_name = line[1:].rstrip() #contig name; remove ">", extract contig string, remove any spaces or new lins following file
            print('Contig file output: ' + contig_name)
            outfile=open(str(contig_name) + ".fa", 'w')
        outfile.write(line)

outfile.close()          