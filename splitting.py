#################################################
# Program: splitting.py
# Author: Alekhya Akkunuri
# Date: 11-2-2017
# Description: The program reads in genomic_dna.txt
# and splits it into coding and non-coding parts
#################################################

# opening the file
my_dna_file = open("genomic_dna.txt")
my_dna = my_dna_file.read()

# splitting into introns and exons
# first exon from position 0 to 63
exon1 = my_dna[0:64]
# second exon starting at position 91 
exon2 = my_dna[91: ]
# intron
intron_region = my_dna[64:91]

# creating the two output files

exon_file = open("exon_c3.txt", "w")
intron_file = open("intron_ch3.txt", "w")

# writing the exons and intron to their respective files

exon_file.write(exon1 + exon2)
intron_file.write(intron_region)



