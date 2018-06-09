###################################
# Program: compliment.py
# Author: Alekhya Akkunuri
# Date: 10-25-2017
# Description: This program prints the complement
# of the DNA sequence
###################################

# Store DNA string in variable
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
compl_table = my_dna.maketrans('ATGC', 'TACG')
complement = my_dna.translate(compl_table)
print(complement)
