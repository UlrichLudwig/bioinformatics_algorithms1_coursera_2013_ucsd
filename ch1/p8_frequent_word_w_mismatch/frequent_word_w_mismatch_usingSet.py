'''
Frequent Words with Mismatches Problem: Find the most frequent k-mers with mismatches in a string.
     Input: A string Text as well as integers k and d. (You may assume k ≤ 12 and d ≤ 3.)
     Output: All most frequent k-mers with up to d mismatches in Text.

CODE CHALLENGE: Solve the Frequent Words with Mismatches Problem.
Sample Input:
     ACGTTGCATGTCGCATGATGCATGAGAGCT 4 1
Sample Output:
     GATG ATGC ATGT
'''
def calMismatchNo(target,pattern):
    mis_count = 0 
    for i in range(len(target)):
        if target[i] != pattern[i]:
            mis_count += 1
    return mis_count

# read the genome
fin = open('input.txt')
tmp_read = fin.readline().split()
genome = tmp_read[0]
kmer = int(tmp_read[1])
d = int(tmp_read[2])
fin.close()

print genome,kmer,d

# generate pattern set 
pattern_set = set([])
for i in range(len(genome)-kmer +1):
    pattern_set.add(genome[i:i+kmer])
#print pattern_set


# calPatternOccurance
def calMismatchNo(target,pattern):
    mis_count = 0 
    for i in range(len(target)):
        if target[i] != pattern[i]:
            mis_count += 1
    return mis_count

def calPatternOccurance(genome,pattern):
    output = []
    kmer = len(pattern)
    for i in range(len(genome)-kmer +1):
        if calMismatchNo(genome[i:i+kmer],pattern) <= d:
            output.append(i)
    return len(output)

# generate pattern_occur_dict
pattern_occur_dict = dict((pattern,calPatternOccurance(genome,pattern))
                          for pattern in pattern_set)

# output the patterns with max occurance 
max_value = max(pattern_occur_dict.values())
output = [pattern for pattern,occur in pattern_occur_dict.iteritems() if occur == max_value]
print output 

# output 
with  open('output.txt','w') as fout:
    for k in output:
        fout.write ("%s " % k )

from subprocess import call
call(["open","output.txt"])        
