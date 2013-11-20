fin = open('E-coli.txt')
genome = fin.readline().rstrip('\n')

kmer = 9
L = 500
t = 3
fin.close()

# 1. Generate all Kmers: 4^k 
def generateKmerAll(kmer):
    atcg = ['A','T','G','C']
    output = []
    while kmer>1:
        for i in generateKmerAll(kmer-1):
            for j in atcg:
                output.append(i+j)
        return output
    return atcg

# 3. Counting the max occurance in the L windows in the dictionary
def countMaxOccur(index_list, kmer, L):
    '''Input: a sorted index list, L size window, kmer
    Output max occurance times for kmer in a L window'''
    occur = [0] * len(index_list)
    for i,item in enumerate(index_list):
        for item2 in index_list:
            if item2-item >=0 and item2 - item <= L - kmer:
                occur[i] += 1
    return max(occur)

# only include the kmer that appears more or equal than t
# generate initial kmer occurance index dictionary 
kmer_occurInd_dic = dict((key,[0]) for key in generateKmerAll(kmer))
# 2. Scan the genome to add occurance index lists into the dictionary
for i in range(len(genome)-kmer+1):
    kmer_occurInd_dic[genome[i:i+kmer]].append(i)

kmer_occurInd_dic = dict((k,v) for k,v in kmer_occurInd_dic.iteritems() if len(v)>=t)    
kmer_occur_dic = {}

for k,v in kmer_occurInd_dic.iteritems():
    tmp = countMaxOccur(v,kmer,L)
    if tmp>=t:
        kmer_occur_dic[k] = tmp

# 4. output the result and show it 

with  open('output.txt','w') as fout:
    for k in set(kmer_occur_dic.keys()):
        fout.write ("%s " % k )

from subprocess import call
call(["open","output.txt"])        
