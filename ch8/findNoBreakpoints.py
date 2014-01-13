def findNoBreakpoints(p):
    '''
    Number of Breakpoints Problem: Find the number of breakpoints in a
    permutation. 
    
    Input: A permutation P.
    Output: The number of breakpoints in P.
    
    CODE CHALLENGE: Solve the Number of Breakpoints Problem.
    
    Sample Input:
    (+3 +4 +5 -12 -8 -7 -6 +1 +2 +10 +9 -11 +13 +14)
    
    Sample Output:
    8

    ----------
    Solution:

    no_breakpoints = len(p) + 1 - no_adjacencies.
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
    with open('fnbp_input.txt','r') as fin:
        s = fin.readline().rstrip('\n') 
    s = s.strip('(')
    s = s.strip(')')
    s = s.split(' ' )

    p = [ int(i) for i in s]
    
    # run the function 

    no_breakpoints = findNoBreakpoints(p)
    
    # output the results
    print no_breakpoints


    
