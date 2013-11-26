'''
The following problem asks you to find the translation of an RNA string into an amino acid string.

Protein Translation Problem: Translate an RNA string into an amino acid string.
     Input: An RNA string Pattern.
     Output: The translation of Pattern into an amino acid string Peptide.

CODE CHALLENGE: Solve the Protein Translation Problem.

Notes:

The “Stop” codon should not be translated, as shown in the sample below.
For your convenience, we provide a downloadable RNA codon table indicating which codons encode which amino acids.
Download RNA Codon Table

Sample Input:
AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output:
MAMAPRTEINSTRING
'''

# read the RNA codon and store it in a dictionrary 
# Added STOP sign into the table txt file. 
with open("RNA_codon_table_1.txt",'r') as f:
    RNA_codon_dic = { line.split()[0]:line.split()[1] for line in f}

# read the input RNA pattern
fin = open('sample_input.txt')
RNA_pattern = fin.readline().rstrip('\n')
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
        
