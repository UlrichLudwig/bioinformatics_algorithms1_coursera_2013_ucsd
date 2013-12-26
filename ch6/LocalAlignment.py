from collections import deque
import sys
sys.setrecursionlimit(10000)

def localAlign(str1, str2, score_dic, sigma): 
    '''
    CODE CHALLENGE: Solve the Local Alignment Problem.
    Input: Two protein strings written in the single-letter amino acid
    alphabet. 
    Output: The maximum score of a local alignment of the strings,
    followed by a local alignment of these 
    
    strings achieving the maximum score. Use the PAM250 scoring matrix
    and indel penalty sigma = 5. 
    
    Download PAM250 scoring matrix
    
    Sample Input:
    MEANLY
    PENALTY
    
    Sample Output:
    15
    EANL-Y
    ENALTY
    ===
    alternative description:
    Local Alignment Problem: Find the highest-scoring local alignment
    between two strings.  
    Input: Strings v and w as well as a matrix score.
    Output: Substrings of v and w whose global alignment score (as
    defined by score) is maximal among all global alignments of all
    substrings of v and w.

    Solution:
    Connecting the source (0, 0) to every other node by adding a
    zero-weight edge and connecting every node to the sink (n, m) by a
    zero-weight edge will result in a DAG perfectly suited for solving
    the Local Alignment Problem ;

    find the max score place in the map; and backwards to the source. 
    '''
    score, backtrack = getAlignmentGraph(str1,str2,score_dic,sigma) 
    #print s, backtrack
    max_score = max(max(l) for l in score)

    for i in range(len(score)):
        for j in range(len(score[0])): 
            if max_score == score[i][j]:
                max_index = [i,j]
                
    result =['','']
    
    OutputLCS(backtrack,str1,str2,max_index[0],max_index[1],result)
    return result, max_score
    
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

    elif backtrack[i-1][j-1] == 2: # down right
        OutputLCS(backtrack,v,m, i-1, j-1,result)
        result[0] += v[i-1]
        result[1] += m[j-1]
    else: # 3, back to source 
        return result 

    
    

def getAlignmentGraph(v,w,score_dic,sigma):
    '''
    add a (0,0) to every node as a predecessor:
    s_{i,j} = max(0, s_{i-1,j} + score(v_i,-); s_{i,j-1} + score(-,w_j),s_{i-1,j-1} + score(v_i,w_j) )

    backtrack_{i,j} = deletion(down,0), insertion(right,1),
    match/mismatch(downright,2), or source 3
    example:
    AlignmentGraph(TGTTA, TCGT)    
    '''    
    s = [[0] * (len(w)+1) for _ in range(len(v) + 1)]
                                
    backtrack = [[0] * len(w) for _ in range(len(v))]

    # calculate score matrix or map
    for i in range(1, len(v) +1):
        for j in range(1, len(w)+1):
            
            max_value, backtrack[i-1][j-1]  = s[i-1][j] - sigma, 0 
            if s[i][j-1] - sigma > max_value:
                max_value, backtrack[i-1][j-1]  = s[i][j-1] - sigma, 1 
            if s[i-1][j-1]+score_dic[(v[i-1],w[j-1])] > max_value:
                max_value, backtrack[i-1][j-1]  = s[i-1][j-1]+score_dic[(v[i-1],w[j-1])], 2            
            if 0 > max_value: 
                max_value, backtrack[i-1][j-1]  = 0, 3
            s[i][j] = max_value

    return s,backtrack

def calScore(output, score_dic, sigma):
    '''
    cal output alignment's score 
    '''
    score = 0 
    for i in range(len(output[0])):
        if output[0][i] == '-' or output[1][i] =='-':
            score -= sigma
        else:
            score += score_dic[(output[0][i],output[1][i])]
    return score 


if __name__ == "__main__":
    # read score file
    with open('PAM250_1.txt','r') as fin:
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
    with open('la_input.txt','r') as fin:
        s = fin.readlines()
    str1 = s[0].rstrip('\n')
    str2 = s[1].rstrip('\n')
        
    # run the function 
    output,score = localAlign(str1,str2,score_dic,sigma)

    #print output
    
    # output the results
    with  open('la_output.txt','w') as fout:
        fout.write ("%d\n" % score)
        fout.write ("%s\n" % output[0])
        fout.write ("%s\n" % output[1])        

    from subprocess import call
    call(["open","la_output.txt"])

