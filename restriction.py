##################################
# Program: restriction.py
# Author: Alekhya Akkunuri
# Date: 10-25-2017
# Description: This program calculates the
# size of the 2 fragments split when
# the sequence is digested with EcoRI
###################################

# Store DNA string in variable
my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
# Find recongntion site and get position of where to cut (after G)
cut_length = my_dna.find('GAATTC')+1

# Get length of both fragments
fragment1 = my_dna[:cut_length]
fragment2 = my_dna[cut_length:]

# Print the lengths of both fragments
print("Length of fragment 1 is: " + str(len(fragment1)))
print("Length of fragment 2 is: " + str(len(fragment2)))



