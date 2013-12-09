'''
The theoretical spectrum of a cyclic peptide Peptide, denoted Cyclospectrum(Peptide), is the collection of all of the masses of its subpeptides, in addition to the mass 0 and the mass of the entire peptide. Note that the theoretical spectrum may contain duplicate elements, as is the case for NQEL (shown below), where NQ and EL have the same mass.

0	113	114	128	129	227	242	242	257	355	356	370	371	484
L	N	Q	E	LN	NQ	EL	QE	LNQ	ELN	QEL	NQE	NQEL

Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.
     Input: An amino acid string Peptide.
     Output: Cyclospectrum(Peptide).

CODE CHALLENGE: Solve the Generating Theoretical Spectrum Problem.

Sample Input:
     LEQN

Sample Output:
     0 113 114 128 129 227 242 242 257 355 356 370 371 484
'''

#  peptide_spetrum_dic is taken from the text
#import urllib
#urllib.urlretrieve ("https://beta.stepic.org/media/attachments/lessons/98/integer_mass_table.txt", "integer_mass_table.txt")
with open("integer_mass_table.txt","r") as f:
    peptide_spetrum_dic = {line.split()[0]:int(line.split()[1]) for line in f}


# read the input RNA pattern
with open('input.txt') as fin:
    peptide_str = fin.readline().rstrip('\n')

# all substrings:
# http://stackoverflow.com/questions/127704/algorithm-to-return-all-combinations-of-k-elements-from-n
# Thanks to Claudiu, recursive solution
def subStringLen(str, length):
    str+= str
    return [str[i:i+length] for i in range(len(str)/2)]

peptide_str_all=[]
for i in range(1,len(peptide_str)):
    peptide_str_all += subStringLen(peptide_str,i) 
peptide_str_all.append(peptide_str)

# str to spectrum
result =  [sum([peptide_spetrum_dic[i] for i in str]) for str in peptide_str_all]
result.sort()

# output
with  open('output.txt','w') as fout:
    fout.write("%d " % 0)
    for i in result:
        fout.write ("%d " % i)

from subprocess import call
call(["open","output.txt"])        
        
