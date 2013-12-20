from collections import deque
import sys
sys.setrecursionlimit(10000)

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
    result = deque([])
    OutputLCS(backtrack,s,len(s),len(t),result)
    return ''.join(list(result))
    
def OutputLCS(backtrack,v,i,j, result):
    # print i,j
    if i ==0  or j ==0:
        return result
    if backtrack[i-1][j-1] == 0:
        OutputLCS(backtrack,v, i-1, j,result)
    elif backtrack[i-1][j-1] == 1:
        OutputLCS(backtrack,v, i, j-1,result)
    else: 
        OutputLCS(backtrack,v, i-1, j-1,result)
        result.append(v[i-1])



def LCS(v,w):
    '''
    LCS(v, w)
        for i <- 0 to |v|
            si, 0 <- 0
        for j <- 0 to |w| 
            s0, j <- 0
        for i <- 1 to |v|
            for j <- 1 to |w|
                si, j = max{si-1, j, si,j-1, si-1, j-1 + 1 (if vi = wj)}
                backtracki, j = (down,0) if si, j = si-1, j ; (right,1) if si, j = si, j-1 ; (downright,2) if si, j = si-1, j-1 + 1
        return s|v|, |w| , backtrack    
    '''
    # s = [[0] * (len(w)+1)]*(len(v)+1) a bug in the 2d list 
    # see: http://stackoverflow.com/questions/2739552/python-2d-list-has-weird-behavor-when-trying-to-modify-a-single-value
    s = [[0] * (len(w)+1) for _ in range(len(v) + 1)]
    backtrack = [[0] * len(w) for _ in range(len(v))]
    
    # for i in range(0,len(v)+1):
    #    s[(i,0)] = 0
    #for j in range(0,len(w)+1):
    #    s[(0,j)] = 0

    for i in range(1, len(v) +1):
        for j in range(1, len(w)+1):
            tmp = [s[i-1][j],s[i][j-1]]
            if v[i-1] == w[j-1]:
                tmp.append(s[i-1][j-1]+1)
            s[i][j] = max(tmp)
            backtrack[i-1][j-1] = 0 if s[i][j] == s[i-1][j] else 1 if s[i][j] == s[i][j-1] else 2
            #print s[i][j],i,j
            #    raw_input('wait')
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

