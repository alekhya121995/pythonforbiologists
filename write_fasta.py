#################################################
# Program: write_fasta.py
# Author: Alekhya Akkunuri
# Date: 11-2-2017
# Description: The program creates a FASTA file
#################################################

# sequence headers
header1 = "ABC123"
header2 = "DEF456"
header3 = "HIJ789"

# DNA sequences
sequence1 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
sequence2 = "actgatcgacgatcgatcgatcacgact"
sequence3 = "ACTGAC-ACTGT--ACTGTA----CATGTG"

# create output file
fasta_file = open("all_sequences.fasta", "w")

# writing headers and sequences to the files
fasta_file.write(">" + header1 + "\n" + sequence1 + "\n")
# lowercase sequence2 to uppercase
fasta_file.write(">" + header2 + "\n" + sequence2.upper() + "\n")
# replace '-' with blank 
fasta_file.write(">" + header3 + "\n" + sequence3.replace("-","") + "\n")
