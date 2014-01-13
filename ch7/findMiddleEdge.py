def findMiddleEdge():
    '''
    CODE CHALLENGE: Solve the Middle Edge in Linear Space Problem (for
    protein strings). Use the BLOSUM62 scoring matrix and a linear indel
    penalty equal to 5. 
    
    Input: Two amino acid strings.
    Output: A middle edge in the alignment graph in the form "(i, j)
    (k, l)", where (i, j) connects to (k, l).  
    
    To compute scores, use the BLOSUM62 scoring matrix and a (linear)
    indel penalty equal to 5. 
    
    Sample Input:
    PLEASANTLY
    MEASNLY
    
    Sample Output:
    (4, 3) (5, 4)
    '''


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

    
