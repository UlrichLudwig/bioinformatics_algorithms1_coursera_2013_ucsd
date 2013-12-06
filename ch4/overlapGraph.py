def overlapGraph(kmers):
    '''
    Input: A collection Patterns of k-mers.
    Output: The overlap graph Overlap(Patterns), in the form of an adjacency list.
    
    Sample Input:
    ATGCG
    GCATG
    CATGC
    AGGCA
    GGCAT
    
    Sample Output:
    AGGCA -> GGCAT
    CATGC -> ATGCG
    GCATG -> CATGC
    GGCAT -> GCATG

    ----------
    Definition: 
    prefix and suffix to refer to the first k − 1 nucleotides and last k
    − 1 nucleotides of a k-mer, respectively. 

    if prefix(kmer2) = suffix(kmer1), then kmer1 -> kmer2

        
    node for each k-mer in Patterns and connect k-mers Pattern1 and Pattern2
    by a directed edge if the suffix of Pattern1 is equal to the prefix
    of Pattern2. The resulting graph is called the overlap graph on
    these k-mers, denoted Overlap(Patterns). 
    '''
        
    return kmers

def prefix(kmer):
    '''
    prefix and suffix to refer to the first k − 1 nucleotides and last k
    − 1 nucleotides of a k-mer, respectively. 
    '''  
    return kmer[:-1]
  
def prefix(kmer):
    '''
    prefix and suffix to refer to the first k − 1 nucleotides and last k
    − 1 nucleotides of a k-mer, respectively. 
    '''  
    return kmer[1:]

if __name__ == "__main__":
    # read file and get parameters
    fin = open('c_input.txt','r')
    k = int(fin.readline().rstrip('\n') )
    Dna = fin.readline().rstrip('\n')
    fin.close()
    # run the function 
    kmers = composition(k,Dna)
    
    # output the results
    with  open('c_output.txt','w') as fout:
        for s in kmers:
            fout.write ("%s\n" % s )
            
            from subprocess import call
            call(["open","c_output.txt"])        
            
            
            
