import os
from os import path
import sys
import argparse

#Created: 13.04.17 - Alexander Wailan

# input data
parser = argparse.ArgumentParser(
	description = 'Simply taking a multi fasta file of contigs and output each contig into seperate fasta files',
	usage = 'Multifasta_to_Single [options] multifastafile')
parser.add_argument('multifastafile', help='A Multi fasta file')
options = parser.parse_args()

opened = False #assume outfile is not open
with open(options.multifastafile) as data:
   
    for line in data:
        if line[0] == ">": #if line starts with ">"
            if(opened): #Look at the end of loop; if previous contig file is open it will be close to start a new one
                outfile.close() # Will close the outfile if it's open (look below and follow loop)
            opened = True #Set opened to true to represent an opened outfile
            contig_name = line[1:].rstrip() #contig name; remove ">", extract contig string, remove any spaces or new lins following file
            print('Contig file output: ' + contig_name)
            outfile = open(str(contig_name) + ".fa", 'w')
        outfile.write(line)

outfile.close()          