# Author: Hank Helmers -- helmershank123@gmail.com
# Date: July 7, 2024
# REU'24 Fungal Genomics & Computational Biology
# 
# Purpose: Seperate the A and B genomes for use in synteny analysis for GENESPACE & MCSCANX
#   We specifically used this for Finger Millet genes, but should be generalizable to other
#   A & B genomes if labelled as such in the .gff files.

# 1. Open input gff file & Create output files
input_lines = open("Ecoracana_560_v1.1.gene.gff3").readlines()
 
a_file = open("fingermillet_a.gene.gff3", "w")
b_file = open("fingermillet_b.gene.gff3", "w")

# 2. Copy the top three lines from input into both a_file & b_file
#       These are the .gff formating lines
for i in range(3):
    a_file.write(input_lines[i])
    b_file.write(input_lines[i])


# 3. For each remaining line, sort into A or B based on the **starting two characters**
#   This starting two characters may differ by genomes
for line in input_lines:
    # line[1] is character where the genomes are specificed
    if line[1] == 'A':
        a_file.write(line)
    if line[1] == 'B':
        b_file.write(line)

