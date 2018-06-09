#################################################
# Program: write_fasta.py
# Author: Alekhya Akkunuri
# Date: 11-2-2017
# Description: The program creates a FASTA file
# for each sequence
#################################################

# sequence headers
header1 = "ABC123"
header2 = "DEF456"
header3 = "HIJ789"

# DNA sequences
sequence1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
sequence2 = "actgatcgacgatcgatcgatcacgact"
sequence3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

# create output files
fasta_file1 = open("sequence1.fasta", "w")
fasta_file2 = open("sequence2.fasta", "w")
fasta_file3 = open("sequence3.fasta", "w")

# writing headers and sequences to the files
fasta_file1.write(">" + header1 + "\n" + sequence1 + "\n")
# lowercase sequence2 to uppercase
fasta_file2.write(">" + header2 + "\n" + sequence2.upper() + "\n")
# replace '-' with blank 
fasta_file3.write(">" + header3 + "\n" + sequence3.replace("-","") + "\n")
