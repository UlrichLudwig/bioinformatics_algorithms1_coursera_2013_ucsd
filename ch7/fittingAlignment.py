def fittingAlign(str1, str2, sigma): 
    '''
    Fitting Alignment Problem: Construct a highest-scoring fitting
    alignment between two strings. 
    
    Input: Two nucleotide striwngs v and w, where v has length at most
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
    
    "Fitting" w to v requires finding a substring v' of v that
    maximizes an alignment score the global alignment score between v'
    and w among all substrings of v. For example, the best global,
    local, and fitting alignments of v = GTAGGCTTAAGGTTA and w = TAGATA
    are shown below (with mismatch and indel penalties equal to 1). 
    
    Note that the optimal local alignment is not a valid fitting
    alignment. On the other hand, the score of the optimal global
    alignment (-3) is smaller than that of the best fitting alignment
    (+2). 
    ===
    update 1/06/14
    Not doing the sily way to calculate global alignment between all
    substring of v and w. 

    Now consider the free Taxi from end of w to end of v. Hint from the
    local alignment algorithm, where two free taxis are needed to drive
    to the begin of local fit and exit from the end of local fitting. 
    '''
    

    '''
    update: 01/02/14 
    1. Changed to simple scoring method: matches count +1 and both the
       mismatch and indel penalties are 1. 

    
    ODE CHALLENGE: Solve the Global Alignment Problem.
    Input: Two protein strings written in the single-letter amino acid alphabet.
    
    Output: The maximum alignment score of these strings followed by an alignment achieving this
    maximum score. Use the BLOSUM62 scoring matrix and indel penalty sigma = 5.
    '''
    score, backtrack = getAlignmentGraph(str1,str2,sigma) 
    #print s, backtrack

    # find max in the last col
    score_lastcol = [l[-1] for l in score]

    max_score =  max(score_lastcol)
    max_index = score_lastcol.index(max_score)
                
    result =['','']
    
    OutputLCS(backtrack,str1,str2,max_index,len(str2),result)
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
    with open('fa_input.txt','r') as fin:
        v = fin.readline().rstrip('\n') 
        w = fin.readline().rstrip('\n') 
                        
    # run the function 
    align, score = fittingAlign(v,w,1)
                        
    # output the results
    with  open('fa_output.txt','w') as fout:
        fout.write("%d\n" % score)
        fout.write ("%s\n" % align[0])
        fout.write ("%s\n" % align[1])
        
    from subprocess import call
    call(["open","fa_output.txt"])        
                            
