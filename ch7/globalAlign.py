from collections import deque
import sys
sys.setrecursionlimit(10000)

def globalAlign(str1, str2, sigma): 
    '''
    update: 01/02/14 
    1. Changed to simple scoring method: matches count +1 and both the
       mismatch and indel penalties are 1. 

    
    ODE CHALLENGE: Solve the Global Alignment Problem.
    Input: Two protein strings written in the single-letter amino acid alphabet.
    
    Output: The maximum alignment score of these strings followed by an alignment achieving this
    maximum score. Use the BLOSUM62 scoring matrix and indel penalty sigma = 5.

    
    
    Download BLOSUM62 scoring matrix
    
    Sample Input:
    PLEASANTLY
    MEANLY
    
    Sample Output:
    8
    PLEASANTLY
    -MEA--N-LY    
    ======
    General definitions:
    1. score = no. matches - mu *  mismatches - sigma *  indels
    '''
    score, backtrack = getAlignmentGraph(str1,str2,sigma) 
    #print s, backtrack

    result =['','']
    OutputLCS(backtrack,str1,str2,len(str1),len(str2),result)
    return result, score[-1][-1]
    
def OutputLCS(backtrack,v,m,i,j, result):

    if i ==0:
        result[0] += '-'*j
        result[1] += m[:j]
        return result
    if j ==0:
        result[0] += v[:i]
        result[1] += '-'* i 
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

    # initial the score matrix
    s[0] = [-sigma * i for i in range(len(s[0]))]
    
    for i in range(len(v) + 1):
        s[i][0] = -sigma * i 
                                
    backtrack = [[0] * len(w) for _ in range(len(v))]

    # calculate score matrix or map
    for i in range(1, len(v) +1):
        for j in range(1, len(w)+1):
            max_value, backtrack[i-1][j-1]  = s[i-1][j] - sigma, 0 
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
    # read score file
    with open('BLOSUM62.txt','r') as fin:
        s = fin.readlines()
    score_matrix = [line.split()[1:] for line in s[1:]]
    strs = s[0].split()
    sigma = 5

    # get the score dictionsary 
    score_dic = {}
    for ind_i,i in enumerate(strs):
        for ind_j,j in enumerate(strs):
            score_dic[(i,j)] = int(score_matrix[ind_i][ind_j])

    '''for i in strs:
        score_dic[(i)] = sigma'''
        
    # get the input arguments. 
    with open('ga_input.txt','r') as fin:
        s = fin.readlines()
    str1 = s[0].rstrip('\n')
    str2 = s[1].rstrip('\n')
        
    # run the function 
    output,score = globalAlign(str1,str2,score_dic,sigma)

    #print output
    
    # output the results
    with  open('ga_output.txt','w') as fout:
        fout.write ("%d\n" % score)
        fout.write ("%s\n" % output[0])
        fout.write ("%s\n" % output[1])        

    from subprocess import call
    call(["open","ga_output.txt"])

