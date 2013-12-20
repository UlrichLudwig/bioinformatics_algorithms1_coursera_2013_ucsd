def OutputLCSMain(s, t): 
    '''
    CODE CHALLENGE: Use OUTPUTLCS (reproduced below) to solve the Longest Common Subsequence Problem.
    
    Input: Two strings s and t.
    Output: A longest common subsequence of s and t.
    
    Note: If more than one LCS exists, you may return any one.
    
    OUTPUTLCS(backtrack, v, i, j)
        if i = 0 or j = 0
            return
        if backtracki, j = (down_arrow,0)
            OUTPUTLCS(backtrack, v, i - 1, j)
        else if backtracki, j = (right_arrow,1)
            OUTPUTLCS(backtrack, v, i, j - 1)
        else (2)
            OUTPUTLCS(backtrack, v, i - 1, j - 1)
            output vi    
            
    Sample Input:
    AACCTTGG
    ACACTGTGA
    
    Sample Output:
    AACTGG
    ------------------------------------------------------------
    defines:
    1. Define LCS_i,j as an LCS between the i-prefix of v, v1...vi, and the j-prefix of w, w1...wj.  
    2. Si,j be the length of LCS_i,j 
    3.  si, j = max{si-1, j, si,j-1, si-1, j-1 + 1 (if vi = wj)}
    '''
    s_mat,backtrack = LCS(s,t) 
    return OutputLCS(backtrack,s,len(s),len(t))
    
def OutputLCS(backtrack,v,i,j):
    if i ==0 or j ==0:
        return 
    if backtrack[i-1][j-1] == 0:
        OutputLCS(backtrack,v, i-1, j)
    elif backtrack[i-1][j-1] == 1:
        OutputLCS(backtrack,v, i, j-1)
    else: 
        OutputLCS(backtrack,v, i-1, j-1)
        print v[:i]
        return v[:i]

def LCS(v,w):
    s = [[0] * (len(w)+1)]*(len(v)+1)
    backtrack = [[0] * len(w)]*len(v)
    
    # for i in range(0,len(v)+1):
    #    s[(i,0)] = 0
    #for j in range(0,len(w)+1):
    #    s[(0,j)] = 0

    for i in range(1, len(v) +1):
        for j in range(1, len(w)+1):
            tmp = [s[i-1][j],s[i][j-1]]
            if v[:i] == w[:j]:
                tmp.append(s[i-1][j-1]+1)
            s[i][j] = max(tmp)
            backtrack[i-1][j-1] = 0 if s[i][j] == s[i-1][j] else 1 if s[i][j] == s[i][j-1] else 2
            print s[i][j],s[i-1][j],s[i][j-1],i,j
            raw_input('wait')
    return s,backtrack
    
        
    

if __name__ == "__main__":
    # read file and get parameters
    with open('olcs_input.txt','r') as fin:
        s = fin.readline().rstrip('\n') 
        t = fin.readline().rstrip('\n') 
    
    # run the function 
    output = OutputLCSMain(s,t)
    
    # output the results
    with  open('olcs_output.txt','w') as fout:
        fout.write ("%s\n" % output)

    from subprocess import call
    call(["open","olcs_output.txt"])        

