# sort-FASTQ-file-by-Q-score
Sort illumina paired-end reads in fatsq format by their average Q-score.

Reads .fastq file and filters out any read pairs where at least one of the sequences has an average Q score below 30.
Produces 2 output files. The first contains the sequences where both reads have an average score above and including 30 and the second those sequences that have at least 1 read with an average score below 30.

The output files have the following names:
above30.fastq
below30.fastq

Make sure fastq input file is in the same directory as this script. 
