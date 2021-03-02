# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:51:24 2020

@author: oscar
"""


    
# function to read in fastaq file and put each read pair into a list, effectivly creating a
# 3D array in the following format:  [ [[1/1],[1/2]], [[2/1],[2/2]] ect........]
def read_in_file(file):
    
    with open(str(file)) as open_file:
        readlines = [line.strip() for line in open_file.readlines()]
        
    single_reads = [readlines[i:i+4] for i in range(0, len(readlines), 4)]
    paired_reads = [single_reads[i:i+2] for i in range(0, len(single_reads), 2)]
    
    return paired_reads




# function to calculate mean q score when given a sequence identifier line 
def calc_Q(identifier):
    count = 0
    number_of_chrs = len(identifier)
    identity = repr(identifier)[1:-1] # use repr to account for \ symbols in the identifier
    
    for ch in identity:
        val = ord(ch)-64
        count += val
        
    mean = count/number_of_chrs # calculate avergae of all q values
    return mean




# main function that is called with file name to run program
def main(file):
    
    reads = read_in_file(file) # calling read_in_file function
    
    above_30 = [] # initiate lists for results
    below_30 = []
    
    for read in reads:
        forward = calc_Q(read[0][3]) #assign avergae q value for forward and reverse reads to variables 
        reverse = calc_Q(read[1][3])
        if forward < 30 or reverse < 30:
            below_30.append(read)
        else:
            above_30.append(read)
            

# Now have above_30 and below_30 lists in the form [ [[1/1],[1/2]], [[2/1],[2/2]] ect........]
# Write these lists to seperate files:
    with open("above30.fastq", "w") as out_file:
        for pair in above_30:
            for seq_read in pair:
                for string in seq_read:
                    out_file.write(string)
                    out_file.write('\n')
                
    with open("below30.fastq", "w") as out_file:
        for pair in below_30:
            for seq_read in pair:
                for string in seq_read:
                    out_file.write(string)
                    out_file.write('\n')
                    
                    
                    
# call main function to get output files             
main("seq_sample.fastq")

