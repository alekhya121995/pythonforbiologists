###################################
# Program: exon_extract.py
# Name: Alekhya Akkunuri
# Date: 11-2-2017
# Description: Use data from genomic_dna_ch4.txt
# and exons.txt to extract exon segments, concatenate
# them and write them into a new file
####################################

# open files
exon_file = open("exons.txt")
genomic_dna_file = open("genomic_dna_ch4.txt")
my_dna = genomic_dna_file.read()
# initialize string to concatenate  exons
concat = ""

# open output file
multiple_exons = open("multiple_exons.txt", "w")

for line in exon_file:
    start_end = line.split(",")
    # start position
    start = int(start_end[0])
    # stop position
    stop = int(start_end[1])
    # getting exon segment
    exon = my_dna[start:stop]
    # concatenate exon segments
    concat = concat + exon

# writing to output file
  
multiple_exons.write(concat)
multiple_exons.close()
