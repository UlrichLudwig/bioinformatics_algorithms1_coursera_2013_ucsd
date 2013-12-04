
'''
CODE CHALLENGE: Implement MOTIFENUMERATION (reproduced below).
     Input: Integers k and d, followed by a collection of strings Dna.
     Output: All (k, d)-motifs in Dna.

    MOTIFENUMERATION(Dna, k, d)
        for each k-mer a in Dna
            for each k-mer a' differing from a by at most d mutations
                if a' appears in each string from Dna with at most d mutations
                    output a'

Sample Input:
     3 1
     ATTTGGC
     TGCCTTA
     CGGTATC
     GAAAATT

Sample Output:
     ATA ATT GTT TTT
'''
def getKmersFromDna(Dna,k):
    '''
    Input: integers k, a list of strings Dna, same length.
    Output: all k mers as a list in the Dna collection
    '''
    kmer_list = set([]) # to avoid reduncency
    for Dna_frag in Dna:
        for i in range(len(Dna_frag)-k+1):
            kmer_list.add(Dna_frag[i:i+k])
    return list(kmer_list)

def comb(m, s):
    '''
    output: m number combination from list s, a 2d list
    ref:http://rosettacode.org/wiki/Combinations#Python
    '''
    if m == 0: return [[]]
    if s == []: return []
    return [s[:1] + a for a in comb(m-1, s[1:])] + comb(m, s[1:])

def generateAllIndex(kmer_length,mutation_no):
    '''
    Input: kmer length and mutation number
    Output: all index combinations where mutation happpens
    '''
    return comb(mutation_no,range(kmer_length))

def generateKmerAll(k):
    atcg = ['A','T','G','C']
    output = []
    while k>1:
        for i in generateKmerAll(k-1):
            for j in atcg:
                output.append(i+j)
        return output
    return atcg

def mutateByIndex(kmer,index):
    '''
    Input: kmer and 1 index 
    Output: All possible mutated kmer, happened in the index
    '''
    mutated_kmer = set([])
    all_possible_value = generateKmerAll(len(index))
    for val in all_possible_value:
        kmer_as_list = list(kmer)
        for i,ind in enumerate(index):
            kmer_as_list[ind] = val[i]
        mutated_kmer.add(''.join(kmer_as_list))

    return mutated_kmer
    
    
def mutateByIndexList(kmer,index_list):
    '''
    Input: a kmer, and the index list (2d list) for which place to be mutate
    Output: all the mutations which happens at the specified index.
    '''
    mutated_kmer = set([])
    for index in index_list:
        mutated_kmer= set(list(mutated_kmer) + list(mutateByIndex(kmer,index)))
    return mutated_kmer
    
def generateAllMutation(kmer,d):
    '''
    Input: a kmer
    Output: all the kmer differing from the input kmer by at most d mutations
    '''
    kmer_list = set([kmer])
    for i in range(1,d+1):
        index_list = generateAllIndex(len(kmer),i) #2d
        kmer_list=set(list(kmer_list)+list(mutateByIndexList(kmer,index_list)))
    return list(kmer_list)

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
    k = len(pattern)
    for i in range(len(genome)-k +1):
        if calMismatchNo(genome[i:i+k],pattern) <= d:
            output.append(i)
    return len(output)


def isKmerInAllDnaByDmutation(Dna,kmer,d):
    '''
    input: a list of DNA (Dna), a kmer, max mismatch d 
    output: whether this kmer is in all the Dna list with max d mismatch
    '''
    flag = 1
    for Dna_frag in Dna:
        flag *= calPatternOccurance(Dna_frag,kmer,d)
    if flag >0:
        return True
    else:
        return False
        
    

def motifEnumeration(Dna, k, d):
    '''
    Input: Integers k and d, followed by a collection of strings Dna.
    Output: All (k, d)-motifs in Dna.
    '''
    all_kmers = getKmersFromDna(Dna,k)
    
    motif = set([])
    for kmer in all_kmers:
        #        print 'kmer is:' 
        #print kmer
        kmer_mutation_list = generateAllMutation(kmer,d)
        #print 'kmer\'s mutation'
        #print kmer_mutation_list
        for kmer1 in kmer_mutation_list:
            if isKmerInAllDnaByDmutation(Dna,kmer1,d):

                motif.add(kmer1)
    return list(motif)
        

if __name__ == "__main__":
    # read file and get parameters
    fin = open('me_input.txt','r')
    tmp = fin.readlines()
    k = int(tmp[0].split()[0])
    d = int(tmp[0].split()[1])
    Dna =[t.rstrip('\n') for t in tmp[1:]]
    fin.close()

    # run the function 
    motif = motifEnumeration(Dna,k,d)
    
    # output the results
    with  open('me_output.txt','w') as fout:
        for i in motif:
            fout.write ("%s " % i )

    from subprocess import call
    call(["open","output.txt"])        
        
