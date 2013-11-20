'''
Frequent Words with Mismatches and Reverse Complements Problem: Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.
      Input: A DNA string Text as well as integers k and d.
      Output: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern)
      over all possible k-mers.

CODE CHALLENGE: Solve the Frequent Words with Mismatches and Reverse Complements Problem.

Sample Input:
     ACGTTGCATGTCGCATGATGCATGAGAGCT
     4 1

Sample Output:
     ATGT ACAT
'''
# timer 
import time
start_time = time.time()

# read the DNA_string
fin = open('input.txt')
DNA_string = fin.readline().rstrip('\n')
tmp_read = fin.readline().split()
kmer = int(tmp_read[0])
d = int(tmp_read[1])
fin.close()

print DNA_string,kmer,d
############################################################
# countPatternWithMismatch
############################################################
def countPatternWithMismatch(text,pattern,d):
    
    return no_occur 

# calPatternOccurance
def calMismatchNo(target,pattern):
    '''Time: kmer '''
    mis_count = 0 
    for i in range(len(target)):
        if target[i] != pattern[i]:
            mis_count += 1
    return mis_count

def reversePattern(pattern):
    DNA_dic = {'A':'T','G':'C','T':'A','C':'G'}
    return ''.join([DNA_dic[s] for s in pattern[::-1]])


def calPatternOccurance(DNA_string,pattern,d):
    '''Time: kmer * len(DNA_string)'''
    output = []
    kmer = len(pattern)

    for i in range(len(DNA_string)-kmer +1):
        if calMismatchNo(DNA_string[i:i+kmer],pattern) <= d:
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

# generate pattern seed from DNA_string (len(DNA_string) complex)
pattern_set_seed = set([])
for i in range(len(DNA_string)-kmer +1):
    pattern_set_seed.add(DNA_string[i:i+kmer])

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
for ind,pattern in enumerate(pattern_set_extended): # Time: 4**kmer*kmer*len(DNA_string)
    if ind % 5000 ==0:
        print float(ind)/len(pattern_set_extended)
    pattern_occur_dict[pattern] = calPatternOccurance(DNA_string,pattern,d)+calPatternOccurance(DNA_string,reversePattern(pattern),d)
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
