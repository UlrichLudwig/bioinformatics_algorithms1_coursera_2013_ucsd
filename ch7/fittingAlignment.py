def fittingAlignment():
    '''
    Fitting Alignment Problem: Construct a highest-scoring fitting
    alignment between two strings. 
    
    Input: Two nucleotide strings v and w, where v has length at most
    1000 and w has length at most 100. 
    
    Output: A highest-scoring fitting alignment between v and w. Use the
    simple scoring method in which matches count +1 and both the
    mismatch and indel penalties are 1. 


    Sample Input:
    GTAGGCTTAAGGTTA
    TAGATA
    
    Sample Output:
    2
    TAGGCTTA
    TAGA--TA

    ¡°Fitting¡± w to v requires finding a substring v¡ä of v that
    maximizes an alignment score the global alignment score between v¡ä
    and w among all substrings of v. For example, the best global,
    local, and fitting alignments of v = GTAGGCTTAAGGTTA and w = TAGATA
    are shown below (with mismatch and indel penalties equal to 1). 

    Note that the optimal local alignment is not a valid fitting
    alignment. On the other hand, the score of the optimal global
    alignment (-3) is smaller than that of the best fitting alignment
    (+2). 
    
    '''
if __name__ == "__main__":
    # read file and get parameters
    with open('fa_input.txt','r') as fin:
        s = fin.readline().rstrip('\n') 
        t = fin.readline().rstrip('\n') 
    
    # run the function 
    distance = fittingAlignment(s,t)
    
    # output the results
    with  open('fa_output.txt','w') as fout:
        fout.write ("%d\n" % distance)

    from subprocess import call
    call(["open","fa_output.txt"])        

