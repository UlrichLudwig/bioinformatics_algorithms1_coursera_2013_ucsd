def calTwoBreakDistance(p):
    '''
    CODE CHALLENGE: Solve the 2-Break Distance Problem.
    Input: Genomes P and Q.
    Output: The 2-break distance d(P, Q).
    
    Sample Input:
    (+1 +2 +3 +4 +5 +6)
    (+1 -3 -6 -5)(+2 -4)
    
    Sample Output:
    3    
    ----------
    Definations:
    1. 2-break distance: minimal number of 2-breaks transforming genome
    P into genome Q 

    
    '''
    no_adjacencies = 0 

    for i in range(len(p)-1):
        if p[i+1] - p[i] == 1:
            no_adjacencies +=1
    if  p[-1] == len(p):
        no_adjacencies +=1 # handle the end 
    if p[0] == 1:
        no_adjacencies +=1 # handle the start. 
    
    return len(p)+1- no_adjacencies
    
    

if __name__ == "__main__":
    # read file and get parameters
    with open('ctbd_input.txt','r') as fin:
        s1 = fin.readline().rstrip('\n') 
        s2 = fin.readline().rstrip('\n') 
    s1 = s1.strip('(')
    s1 = s1.strip(')')
    s1 = s1.split(' ' )

    p = [ int(i) for i in s1]
    
    # run the function 

    no_breakpoints = findNoBreakpoints(p)
    
    # output the results
    print no_breakpoints


    
