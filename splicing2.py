###############################################
# Program: splicing2.py
# Author: Alekhya Akkunuri
# Date: 10-26-2017
# Description: This program caluclates the percentage
# of DNA that is coding
#################################################

# Store DNA string ain variable
my_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
# get length of DNA
length_dna = len(my_dna) 

# exon 1
exon1 = my_dna[0:64]
# get length of exon 1
length_exon1 = len(exon1)

# exon 2
exon2 = my_dna[91: ]
# get length of exon 2
length_exon2 = len(exon2)

# caluclate the percentage of coding regions in the DNA
percent_coding = ((length_exon1 + length_exon2) / length_dna) *100

print("Percentage of coding regions in sequence: " + str(percent_coding)) 
