###############################################
# Program: splicing3.py
# Author: Alekhya Akkunuri
# Date: 10-26-2017
# Description: This program prints coding regions
# in uppercase and non-coding refions in lowecase
#################################################

my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

# first exon from position 0 to 63
exon1 = my_dna[0:64]
# second exon starting at position 91 
exon2 = my_dna[91: ]

# intron
intron_region = my_dna[64:91]
# setting intron region to lowercase
intron = intron_region.lower() 

print(exon1 + intron + exon2)                                
