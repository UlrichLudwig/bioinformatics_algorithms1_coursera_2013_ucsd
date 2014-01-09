def overlapAlign(str1, str2, sigma): 
    '''
    CODE CHALLENGE: Solve the Overlap Alignment Problem.
    Input: Two strings v and w, each of length at most 1000.
    Output: The score of an optimal overlap alignment of v and w, followed by an alignment of a suffix v' of
    v and a prefix w' of w achieving this maximum score. Use an alignment score in which matches count
    +1 and both the mismatch and indel penalties are 2.
    
    Sample Input:
    PAWHEAE
    HEAGAWGHEE
    
    Sample Output:
    1
    HEAE
    HEAG
    ===
    Solution:

    Similar to fitting alignment. 

    In this case, you need find the max score in the last row (not col
    as fitting alignment. And back tracking from that position to reach
    the first string of str2 and then stop)
    '''
    score, backtrack = getAlignmentGraph(str1,str2,sigma) 
    #print s, backtrack

    # find max in the last row
    score_lastrow = score[-1]

    max_score =  max(score_lastrow)
    max_index = score_lastrow.index(max_score)
                
    result =['','']
    
    OutputLCS(backtrack,str1,str2,len(str1),max_index,result)
    return result, max_score
    
def OutputLCS(backtrack,v,m,i,j, result):

    if i ==0: # reach the end of v
        result[0] += '-'*j
        result[1] += m[:j]
        return result
    if j ==0: # reach the end of w
        #        result[0] += v[:i]
        #result[1] += '-'* i 
        return result
    if backtrack[i-1][j-1] == 0: # down
        OutputLCS(backtrack,v,m, i-1, j,result)
        result[0] += v[i-1]
        result[1] += '-' 
    elif backtrack[i-1][j-1] == 1: # right
        OutputLCS(backtrack,v,m, i, j-1,result)
        result[0] += '-'
        result[1] += m[j-1]
    else:
        #elif backtrack[i-1][j-1] == 2: #down right 
        OutputLCS(backtrack,v,m, i-1, j-1,result)
        result[0] += v[i-1]
        result[1] += m[j-1]
        
        

    
def getAlignmentGraph(v,w,sigma):
    '''
    s_{i,j} = max(s_{i-1,j} + score(v_i,-); s_{i,j-1} + score(-,w_j),s_{i-1,j-1} + score(v_i,w_j) )

    backtrack_{i,j} = deletion(down,0), insertion(right,1), match/mismatch(downright,2,3)
    example:
    AlignmentGraph(TGTTA, TCGT)    
    '''    
    s = [[0] * (len(w)+1) for _ in range(len(v) + 1)]

    # initial the score matrix for w; v starts 0 (col 1) 
    s[0] = [-sigma * i for i in range(len(s[0]))]
    
    #for i in range(len(v) + 1):
    #    s[i][0] = -sigma * i 
                                
    backtrack = [[0] * len(w) for _ in range(len(v))]

    # calculate score matrix or map
    for i in range(1, len(v) +1):
        for j in range(1, len(w)+1):
            max_value, backtrack[i-1][j-1]  = s[i-1][j] - sigma, 0 # 
            if s[i][j-1] - sigma > max_value:
                max_value, backtrack[i-1][j-1]  = s[i][j-1] - sigma, 1 
            if s[i-1][j-1] + scoreCmp(v[i-1],w[j-1],sigma) > max_value:
                max_value, backtrack[i-1][j-1]  = s[i-1][j-1] + scoreCmp(v[i-1],w[j-1],sigma), 2  
            s[i][j] = max_value

    return s,backtrack

def scoreCmp(str1,str2,sigma):
    return 1 if str1==str2 else -sigma

def calScore(output, sigma):
    '''
    cal output alignment's score 
    '''
    score = 0 
    for i in range(len(output[0])):
        if output[0][i] == '-' or output[1][i] =='-':
            score -= sigma
        else:
            score += scoreCmp(output[0][i],output[1][i],sigma)
    return score 

                
if __name__ == "__main__":
    # read file and get parameters
    with open('oa_input.txt','r') as fin:
        v = fin.readline().rstrip('\n') 
        w = fin.readline().rstrip('\n') 
                        
    # run the function 
    align, score = overlapAlign(v,w,2)
                        
    # output the results
    with  open('oa_output.txt','w') as fout:
        fout.write("%d\n" % score)
        fout.write ("%s\n" % align[0])
        fout.write ("%s\n" % align[1])
        
    from subprocess import call
    call(["open","oa_output.txt"])        
                            
