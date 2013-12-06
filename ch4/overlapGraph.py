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
    prefix and suffix to refer to the first k - 1 nucleotides and last k
    - 1 nucleotides of a k-mer, respectively. 

    if prefix(kmer2) = suffix(kmer1), then kmer1 -> kmer2

    node for each k-mer in Patterns and connect k-mers Pattern1 and Pattern2
    by a directed edge if the suffix of Pattern1 is equal to the prefix
    of Pattern2. The resulting graph is called the overlap graph on
    these k-mers, denoted Overlap(Patterns). 
    '''
    # duplicate kmers
    kmers_1 = kmers[:]

    output = []
    # use turple 
    for kmer in kmers:
        for kmer1 in kmers_1:
            if suffix(kmer) == prefix(kmer1):
                output.append((kmer,kmer1))

    return sorted(output)

def prefix(kmer):
    '''
    return the first k - 1 nucleotides of a k-mer, respectively.
    '''  
    return kmer[:-1]
  
def suffix(kmer):
    '''
    return the last k - 1 nucleotides of a k-mer, respectively. 
    '''  
    return kmer[1:]

if __name__ == "__main__":
    # read file and get parameters
    fin = open('og_input.txt','r')
    kmers = [line.rstrip('\n') for line in fin.readlines()]
    fin.close()

    # run the function 
    graph_tuple_list = overlapGraph(kmers)
    
    # output the results
    with  open('og_output.txt','w') as fout:
        fout.write ('\n'.join("%s -> %s" % s for s in graph_tuple_list))

    from subprocess import call
    call(["open","og_output.txt"])        
            
            
            
