###################################
# Program: calculateATcontent.py
# Author: Alekhya Akkunuri
# Date: 10-25-2017
# Description: This program calculates the AT content of 
# the DNA string and prints it out. The value we get is 
# the proportion of bases that are either A or T
###################################


# DNA string stored in variable
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"

# Getting the number of A's and T's
a_count_dna = my_dna.count('A')
t_count_dna = my_dna.count('T')

# Calculate AT content
AT_content = (a_count_dna + t_count_dna) / len(my_dna)

# print calculated AT content
print("The calculated AT content is: " + str(AT_content))
