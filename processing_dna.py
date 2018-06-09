#################################################
# Program: processing_dna.py
# Author: Alekhya Akkunuri
# Date: 11-2-2017
# Description: Takes in input.txt, trims sequencing
# adapter and write the cleaned sequences to a new file
# It also prints the length of each sequence to the screen
#################################################

# open the file
my_dna_file = open("input.txt")

# open file for writing 
cleaned_sequences = open("cleaned_sequences.txt","w")

for dna in my_dna_file:
   # remove sequencing adapter
   trimmed = dna[14: ] 
   # writing cleaned sequences to output file
   cleaned_sequences.write(trimmed)
   # print length of each sequence 
   print("cleaned sequence length: " + str(len(trimmed)))
