'''
We say that a DNA string Pattern encodes an amino acid string Peptide if the RNA string transcribed from either Pattern or its reverse complement Pattern translates into Peptide.

Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.
     Input: A DNA string Text and an amino acid string Peptide.
     Output: All substrings of Text encoding Peptide (if any such substrings exist).

CODE CHALLENGE: Solve the Peptide Encoding Problem.

Sample Input:
     ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
     MA

Sample Output:
     ATGGCC
     GGCCAT
     ATGGCC

Note: The solution may contain repeated strings if the same string occurs more than once as a substring of Text and encodes Peptide.
'''

# read the RNA codon and store it in a dictionrary 
# Added STOP sign into the table txt file. 
with open("../1.Protein_translation_problem/RNA_codon_table_1.txt",'r') as f:
    RNA_codon_dic = { line.split()[0]:line.split()[1] for line in f}

# read the input RNA pattern
fin = open('input.txt')
DNA_string = fin.readline().rstrip('\n')
peptide_string = fin.readline().rstrip('\n')
fin.close()

# translate by using the dic
RNA_length = len(RNA_pattern)


protein_seq = [RNA_codon_dic[RNA_pattern[i:i+3]] for i in range(0,len(RNA_pattern),3) if RNA_codon_dic[RNA_pattern[i:i+3]] != 'STOP']
protein_seq = ''.join(protein_seq)
print protein_seq

with  open('output.txt','w') as fout:
    for i in protein_seq:
        fout.write ("%s" % i )

from subprocess import call
call(["open","output.txt"])        
        
