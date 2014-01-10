from collections import deque
import sys, copy
sys.setrecursionlimit(10000)

def affineGapAlign(v,m,score_dic,sigma,epsilon):
    '''
    CODE CHALLENGE: Solve the Alignment with Affine Gap Penalties Problem.
    Input: Two amino acid strings v and w (each of length at most 100).
    Output: The maximum alignment score between v and w, followed by an alignment of v and w
    achieving this maximum score. Use the BLOSUM62 scoring matrix, a gap opening penalty of 11, and
    a gap extension penalty of 1.
    
    Download BLOSUM62 scoring matrix
    
    Sample Input:
    PRTEINS
    PRTWPSEIN
    
    Sample Output:
    8
    PRT---EINS
    PRTWPSEIN-    

    ====
    CONCEPTIONS:
    A gap is a contiguous sequence of spaces in a row of an alignment.
    
    Affine score for a gap of length k as:  sigma + epsilon*(k - 1), where
    sigma is the *gap opening penalty*, assessed to the first symbol in
    the gap, and epsilon is the gap extension penalty, assessed for each
    additional symbol in the gap.  

     We typically select epsilon to be smaller than sigma so that the
     affine penalty for a gap of length k is smaller than the penalty
     for k independent single-nucleotide indels (sigma * k). 

     Solution:
     Draw the alignment graph and matrix. 

     Use 3 score matrix (lower---down direction,upper --- right
     direction,middle --- down right):  

     lower and upper increase by epsilon; when jump from middle to upper
     or lower incresing sigma; 

     lower_i,j = max(lower_i-1,j - epsilon, middle_i-1,j - sigma)
     upper_i,j = max(upper_i,j-1 - epsilon, middle_i,j-1 - sigma)     
     middle_i,j = max(lower_i,j, middle_i-1,j-1 + score(v_i,w_j),
     upper_i,j

     The variable loweri,j computes the score of an optimal alignment
    between the i-prefix of v and the j-prefix of w ending with a
    deletion (i.e., a gap in w), whereas the variable upperi,j computes
    the score of an optimal alignment of these prefixes ending with an
    insertion (i.e., a gap in v), and the variable upperi,j computes the
    score for an optimal alignment ending with a match or mismatch. The
    first term in the recurrences for loweri,j and upperi,j corresponds
    to extending the gap, whereas the second term corresponds to
    initiating the gap. 
    '''

    score_upper,score_lower,score_middle,backtrack = getAlignmentGraph(str1,str2,score_dic,sigma,epsilon) 
    #print s, backtrack

    result =['','']
    OutputLCS(backtrack,str1,str2,len(str1),len(str2),result)
    return result, score_middle[-1][-1]
    
def OutputLCS(backtrack,v,m,i,j, result):

    if i ==0:
        result[0] += '-'*j
        result[1] += m[:j]
        return result
    if j ==0:
        result[0] += v[:i]
        result[1] += '-'* i 
        return result
    if backtrack[i-1][j-1] == 0: # down, lower score matrix
        OutputLCS(backtrack,v,m, i-1, j,result)
        result[0] += v[i-1]
        result[1] += '-' 
    elif backtrack[i-1][j-1] == 1: # right, upper score matrix
        OutputLCS(backtrack,v,m, i, j-1,result)
        result[0] += '-'
        result[1] += m[j-1]

    else: # middle score matrix 
        OutputLCS(backtrack,v,m, i-1, j-1,result)
        result[0] += v[i-1]
        result[1] += m[j-1]
        
def getAlignmentGraph(v,w,score_dic,sigma,epsilon):
    '''
    s_{i,j} = max(s_{i-1,j} + score(v_i,-); s_{i,j-1} + score(-,w_j),s_{i-1,j-1} + score(v_i,w_j) )

    backtrack_{i,j} = deletion(down,0), insertion(right,1), match/mismatch(downright,2,3)
    example:
    AlignmentGraph(TGTTA, TCGT)    
    '''    
    
    # initial the score matrix    
    s_up = [[0] * (len(w)+1) for _ in range(len(v) + 1)]
    s_up[0] = [-sigma*i for i in range(len(s_up[0]))]
    for i in range(len(v) + 1):
        s_up[i][0] = -sigma * i 

    s_low = copy.deepcopy(s_up)        
    s_mid = copy.deepcopy(s_up)            

    
    backtrack = [[0] * len(w) for _ in range(len(v))]

    # calculate score matrix or map
    for i in range(1, len(v) +1):
        for j in range(1, len(w)+1):
            # for the lower score matrix
            
            s_low[i][j] = max(s_low[i-1][j] - epsilon, s_mid[i-1][j] - sigma)
            
            s_up[i][j] = max(s_up[i][j-1] - epsilon, s_mid[i][j-1] - sigma)            

            # for the middle score matrix 
            max_value, backtrack[i-1][j-1]  = s_low[i][j], 0 #low
            if s_up[i][j]  > max_value:
                max_value, backtrack[i-1][j-1]  = s_up[i][j], 1 #up
            if s_mid[i-1][j-1]+score_dic[(v[i-1],w[j-1])] > max_value:
                max_value, backtrack[i-1][j-1]  = s_mid[i-1][j-1]+score_dic[(v[i-1],w[j-1])], 2            
            s_mid[i][j] = max_value

    return s_up,s_low,s_mid,backtrack


    
    
if __name__ == "__main__":
    # read score file
    with open('BLOSUM62.txt','r') as fin:
        s = fin.readlines()
    score_matrix = [line.split()[1:] for line in s[1:]]
    strs = s[0].split()

    # get the score dictionsary 
    score_dic = {}
    for ind_i,i in enumerate(strs):
        for ind_j,j in enumerate(strs):
            score_dic[(i,j)] = int(score_matrix[ind_i][ind_j])

    sigma, epsilon = 11, 1 
    
    # get the input arguments. 
    with open('aga_input.txt','r') as fin:
        s = fin.readlines()
    str1 = s[0].rstrip('\n')
    str2 = s[1].rstrip('\n')
        
    # run the function 
    output,score = affineGapAlign(str1,str2,score_dic,sigma,epsilon)

    #print output
    
    # output the results
    with  open('aga_output.txt','w') as fout:
        fout.write ("%d\n" % score)
        fout.write ("%s\n" % output[0])
        fout.write ("%s\n" % output[1])        

    from subprocess import call
    call(["open","aga_output.txt"])

