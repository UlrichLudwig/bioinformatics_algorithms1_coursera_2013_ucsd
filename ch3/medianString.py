'''
We now give the pseudocode for a brute force solution to the Median String Problem.

    MEDIANSTRING(Dna, k)
        BestPattern <- AAA...AA
        for each k-mer Pattern from AAA...AA to TTT...TT
            if d(Pattern, Dna) < d(BestPattern, Dna)
                 BestPattern <- Pattern
        output BestPattern

'''

def calMismatchNo(target,pattern):
    '''or Hamming Distance between same length fragment '''
    mis_count = 0 
    for i in range(len(target)):
        if target[i] != pattern[i]:
            mis_count += 1
    return mis_count

def calMinimalHammingDistance(pattern,Dna_fragment):
    '''
    The minimum Hamming distance between Pattern and any k-mer in Dna_fragment. 
    e.g.:
    calMinimalHammingDistance(GATTCTCA, GCAAAGAcgCTcACCAA) = 3
    '''    
    return min([calMismatchNo(Dna_fragment[i:i+len(pattern)],pattern) for i in range(len(Dna_fragment)-len(pattern)+1)])
    
    
def d(pattern,Dna):
    '''
    Input: kmer pattern, and Dna list
    Output: the sum of distances between Pattern and all strings in Dna.

    Example (ignore the lower case):
    d(AAA, Dna) = 1 + 1 + 2 + 0 + 1 = 5:
    ttaccttAAc  1
    gAtAtctgtc  1
    Acggcgttcg  2
    ccctAAAgag  0
    cgtcAgAggt  1

    '''
    sum_of_distance = 0 
    for Dna_fragment in Dna:
        sum_of_distance += calMinimalHammingDistance(pattern,Dna_fragment)
    return sum_of_distance

def generateKmerAll(k):
    atcg = ['A','T','G','C']
    output = []
    while k>1:
        for i in generateKmerAll(k-1):
            for j in atcg:
                output.append(i+j)
        return output
    return atcg
       
    
def mediumString(Dna,k):
    '''
    Input: An integer k, followed by a collection of strings Dna.
    Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all k-mers Pattern. (Return any one if there are multiple medium strings.)

    Sample Input:
    3
    AAATTGACGCAT
    GACGACCACGTT
    CGTCAGCGCCTG
    GCTGAGCACCGG
    AGTACGGGACAG
    
    Sample Output:
    GAC
    
    '''

    best_pattern = 'A'*k

    pattern_list = generateKmerAll(k)

    for kmer_pattern in pattern_list:
        if d(kmer_pattern,Dna) < d(best_pattern,Dna):
            best_pattern = kmer_pattern
    return best_pattern

    
if __name__ == "__main__":
    # read file and get parameters
    fin = open('ms_input.txt','r')
    tmp = fin.readlines()
    k = int(tmp[0].split()[0])
    Dna =[t.rstrip('\n') for t in tmp[1:]]
    fin.close()

    # run the function 
    motif = mediumString(Dna,k)
    
    # output the results
    with  open('ms_output.txt','w') as fout:
        fout.write ("%s" % motif )

    from subprocess import call
    call(["open","output.txt"])        
        
