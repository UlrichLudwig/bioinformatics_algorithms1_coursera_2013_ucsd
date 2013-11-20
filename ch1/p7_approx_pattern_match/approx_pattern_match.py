'''
Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.
     Input: Two strings Pattern and Text along with an integer d.
     Output: All positions where Pattern appears in Text with at most d mismatches.

CODE CHALLENGE: Solve the Approximate Pattern Matching Problem

Sample Input:
     ATTCTGGA
     CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT
     3

Sample Output:
     6 7 26 27
'''
def calMismatchNo(target,pattern):
    mis_count = 0 
    for i in range(len(target)):
        if target[i] != pattern[i]:
            mis_count += 1
    return mis_count

# read the genome
fin = open('input_real.txt')
pattern = fin.readline().rstrip('\n')
genome = fin.readline().rstrip('\n')
d = int(fin.readline().rstrip('\n'))

fin.close()
output = []
kmer = len(pattern)
for i in range(len(genome)-kmer +1):
    if calMismatchNo(genome[i:i+kmer],pattern) <= d:
        output.append(i)
#print output

with  open('output.txt','w') as fout:
    for k in output:
        fout.write ("%d " % k )

from subprocess import call
call(["open","output.txt"])        


    




