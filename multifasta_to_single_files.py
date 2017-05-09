import os
from os import path
import sys
import argparse

#Created: 13.04.17 - Alexander Wailan

# input data
parser = argparse.ArgumentParser(
	description = 'Simply taking a multi fasta file of contigs and output each contig into seperate fasta files',
	usage = 'Multifasta_to_Single [options] multifastafile unique_integer')
parser.add_argument('multifastafile', help = 'A Multi fasta file as input')
parser.add_argument('unique_integer', help = 'If you want a unique number per file out: input Yes or No ')
options = parser.parse_args()
output_integer = 0 #Counts the output; adds an incremental number to the file name

opened = False #assume outfile is not open
with open(options.multifastafile) as data:
    
    for line in data:
        if line[0] == ">": #if line starts with ">"
            if(opened): #Look at the end of loop; if previous contig file is open it will be close to start a new one
                outfile.close() # Will close the outfile if it's open (look below and follow loop)
            opened = True #Set opened to true to represent an opened outfile
            if options.unique_integer == "Yes":
                output_integer = output_integer + 1
                contig_name = line[1:].rstrip() #contig name; remove ">", extract contig string, remove any spaces or new lins following file
                outfile = open(str(contig_name) + "_" + str(output_integer) + ".fa", 'w') #output with a numberical integar for dataset
            if options.unique_integer == "No":
                contig_name = line[1:].rstrip() #contig name; remove ">", extract contig string, remove any spaces or new lins following file
                outfile = open(str(contig_name) + ".fa", 'w')
            print('Contig file output: ' + contig_name + ".fa")
            
        outfile.write(line)

outfile.close()          