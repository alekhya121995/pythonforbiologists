###################################################
# Program: parse_blast.py
# Author: Alekhya Akkunuri
# Date: 11-2-2017
# Description: Read in the blast file and grab transcript id,
# isoform, swissprot Id and identity. Write them to a file
#####################################################

# open the blast file
blast_file = open("/scratch/RNASeq/blastp.outfmt6")
# read the blast file line by line such that each line is its own element
blast_contents = blast_file.readlines()
# open the output file
blast_output = open("parsed_blast.txt", "w")
# write the 4 column names to the output file
blast_output.write("TranscriptId" + "\t" + "isoform" + "\t" + "Swissprot Id"
                        + "\t" + "identity" + "\n")
# go through each line in the blast file 
for line in blast_contents:
    # split at tabs
    line_split = line.split("\t")
    # store each required element into a variable
    transcriptId_isoform = line_split[0]
    swissprotId = line_split[1]
    identity = line_split[2]
    # split the variables further
    subsplit1 = transcriptId_isoform.split("|")
    subsplit2 = swissprotId.split("|")
    # write to file and separate each column with a tab
    blast_output.write(subsplit1[0] + "\t" + subsplit1[1] + "\t" + subsplit2[3] 
 			+ "\t" + identity + "\n")

# close the file
blast_output.close()
