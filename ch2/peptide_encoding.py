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
with open("DNA_codon_table_1.txt",'r') as f:
    DNA_codon_dic = { line.split()[0]:line.split()[1] for line in f}

# read the input RNA pattern
fin = open('input.txt')
DNA_string = fin.readline().rstrip('\n')

peptides_string = fin.readline().rstrip('\n')
fin.close()


# from peptides strings to DNA strings (search target, 3mers): 
DNA_target_list=[[key for key,value in DNA_codon_dic.iteritems() if value==peptide_str] for peptide_str in peptides_string] 

# function: Combine codon_list1 and codon_list2
def combine2CondonLists(codon_list1, codon_list2):
    return [codon1+ codon2 for codon1 in codon_list1 for codon2 in codon_list2]

# Combine all possible encoding DNA target list
def combineAllCondonLists(DNA_target_list):
    tmp = combine2CondonLists(DNA_target_list[0],DNA_target_list[1])
    for i in range(2,len(DNA_target_list)):
        tmp = combine2CondonLists(tmp,DNA_target_list[i])
    return tmp
    
DNA_target_list_all = combineAllCondonLists(DNA_target_list)
                
# DNA_target_list_all = combineAllCondonLists(DNA_target_list,len(DNA_target_list)-1)
tmp_target_rev = map(reverse_complement.reverse_complement,DNA_target_list_all)
for rev in tmp_target_rev:
    DNA_target_list_all.append(rev)

# funcion: find all the DNA pattern in trans and rev string 
kmer = len(peptides_string)*3
with  open('output.txt','w') as fout:
    for i in range(len(DNA_string) - kmer+1):
        if DNA_string[i:i+kmer] in DNA_target_list_all:
            #fout.write ("%d,%s\n" % (i,DNA_string[i:i+kmer]) )
            fout.write ("%s\n" % DNA_string[i:i+kmer])

from subprocess import call
call(["open","output.txt"])        
        
