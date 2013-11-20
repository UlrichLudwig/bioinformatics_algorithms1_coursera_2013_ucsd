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

# timer 
import time
start_time = time.time()

# read the genome
fin = open('input.txt')
tmp_read = fin.readline().split()
genome = tmp_read[0]
kmer = int(tmp_read[1])
d = int(tmp_read[2])
fin.close()

print genome,kmer,d



# calPatternOccurance
def calMismatchNo(target,pattern):
    '''Time: kmer '''
    mis_count = 0 
    for i in range(len(target)):
        if target[i] != pattern[i]:
            mis_count += 1
    return mis_count

def calPatternOccurance(genome,pattern,d):
    '''Time: kmer * len(genome)'''
    output = []
    kmer = len(pattern)

    for i in range(len(genome)-kmer +1):
        if calMismatchNo(genome[i:i+kmer],pattern) <= d:
            output.append(i)
    return len(output)




############################################################
# extend pattern set 
############################################################
# generate length d mutation list 

def generateKmerAll(kmer):
    atcg = ['A','T','G','C']
    output = []
    while kmer>1:
        for i in generateKmerAll(kmer-1):
            for j in atcg:
                output.append(i+j)
        return output
    return atcg

mutant_list = generateKmerAll(d)

# generate pattern seed from genome (len(genome) complex)
pattern_set_seed = set([])
for i in range(len(genome)-kmer +1):
    pattern_set_seed.add(genome[i:i+kmer])

# extend the pattern set seed by using mutation list  ()  
pattern_set_extended = set([])
index_combinations = []; # 2d list (C(kmer,d),complex)

# http://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python
# using itertools
import itertools

for i,pattern in enumerate(pattern_set_seed): # (len(pattern_set_seed) complex)
    # select all d-length index combinations 
    for index in itertools.combinations(range(kmer),d): # (C(kmer,d),complex)
        for mutant in mutant_list:# (4**d complex)
            tmp = list(pattern)
            for ind,v in enumerate(index): # (d complex)
                tmp[v] = mutant[ind]
                pattern_set_extended.add("".join(tmp))

# calculate the pattern occurance dictionary 
pattern_occur_dict = {}
for ind,pattern in enumerate(pattern_set_extended): # Time: 4**kmer*kmer*len(genome)
    if ind % 5000 ==0:
        print float(ind)/len(pattern_set_extended)
    pattern_occur_dict[pattern]=calPatternOccurance(genome,pattern,d)
print len(pattern_occur_dict)

# output the patterns with max occurance 
max_value = max(pattern_occur_dict.values())
output = [pattern for pattern,occur in pattern_occur_dict.iteritems() if occur == max_value]

print output 

# output 
print (time.time() - start_time)/60.0, "mins"

with  open('output.txt','w') as fout:
    for k in output:
        fout.write ("%s " % k )

from subprocess import call
call(["open","output.txt"])        
