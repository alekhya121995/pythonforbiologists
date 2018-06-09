###############################################
# Program: splicing1.py
# Author: Alekhya Akkunuri
# Date: 10-25-2017
# Description: This program prints only the coding 
# regions of the DNA sequence, i.e., the exons
#################################################

my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"

# start of sequence to base 63,when count starts at zero
# 63 is exclusive but position is to be included in the fragment
exon1 = my_dna[0:64]
# second exon starting at position 91 
exon2 = my_dna[91: ]

# print fragment 1
print("coding region 1: " + exon1)
# print fragment 2
print("coding region 2: " + exon2)
