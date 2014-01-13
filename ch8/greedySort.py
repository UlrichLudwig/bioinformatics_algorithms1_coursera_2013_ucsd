def greedySort(p, fout):
    '''

    Input: A permutation P.
    Output: The sequence of permutations corresponding to applying
    GREEDYSORTING to P, ending with the identity permutation.   
    
    Sample Input:
    (-3 +4 +1 +5 -2)
    
    Sample Output:
    (-1 -4 +3 +5 -2)
    (+1 -4 +3 +5 -2)
    (+1 +2 -5 -3 +4)
    (+1 +2 +3 +5 +4)
    (+1 +2 +3 -4 -5)
    (+1 +2 +3 +4 -5)
    (+1 +2 +3 +4 +5)        

    ------------------------------------------------------------    
    Algorithm:
    
    GREEDYSORTING(P)
        approxReversalDistance <- 0
        for k = 1 to |P|
            if element k is not sorted
                apply the k-sorting reversal to P
                approxReversalDistance <- approxReversalDistance + 1
            if k-th element of P is -k
                apply the reversal flipping the k-th element of P
                approxReversalDistance <- approxReversalDistance + 1
        return approxReversalDistance    
    '''
    approxReversalDistance = 0

    for k in range(1,len(p)+1):
        if p[k-1] != k: # not sorted 
            p = sortReversal(p,k) 
            approxReversalDistance += 1
            fout.write('%s\n' % formatPrint(p))
        if p[k-1] == -k:
            reversalFlip(p,k)
            approxReversalDistance += 1
            fout.write('%s\n' % formatPrint(p))
    return approxReversalDistance

def sortReversal(p,k):
    # find the index of k or -k: index_k
    try: 
        index_k = p.index(k)
    except ValueError:
        index_k = p.index(-k)
        
    # reversal k to index_k
    return p[:k-1] + [-p[i] for i in range(index_k,k-2,-1)] + p[index_k+1:]

def reversalFlip(p,k):
    p[k-1] = k    
    return 

def formatPrint(p):
    str_output = '('
    for val in p[:-1]:
        str_output += (str(val) if val<0 else '+' + str(val))
        str_output += ' '
    str_output += (str(p[-1]) if p[-1]<0 else '+' + str(p[-1]))
    str_output += ')'
    return str_output
        

if __name__ == "__main__":
    # read file and get parameters
    with open('gs_input.txt','r') as fin:
        s = fin.readline().rstrip('\n') 
    s = s.strip('(')
    s = s.strip(')')
    s = s.split(' ' )

    p = [ int(i) for i in s]
    
    # run the function 
    fout= open('gs_output.txt','w')     
    distance = greedySort(p,fout)
    fout.close()
    # output the results
    print distance

    from subprocess import call
    call(["open","gs_output.txt"])        

    
