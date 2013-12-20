def ManhattanTourist(n, m, down_matix, right_matrix): 
    '''
    CODE CHALLENGE: Find the length of a longest path in the Manhattan Tourist Problem.
    Input: Integers n and m, followed by an n * (m + 1) matrix down and an (n + 1) * m matrix right.
    
    The two matrices are separated by the - symbol.
    
    Output: The length of a longest path from source (0, 0) to sink (n, m) in the n * m rectangular grid whose
    edges are defined by the matrices down and right.
    
    Sample Input:
    4
    4
    1 0 2 4 3
    4 6 5 2 1
    4 4 5 2 1
    5 6 8 5 3
    -
    3 2 4 0
    3 2 4 2
    0 7 3 3
    3 3 0 2
    1 3 2 2
    
    Sample Output:
    34
    ===
    algorithm:
        MANHATTANTOURIST(n, m, down, right)
        s0, 0 <- 0
        for i <- 1 to n
            si, 0 <- si-1, 0 + downi, 0
        for j <- 1 to m
            s0, j <- s0, j-1 + right0, j
        for i <- 1 to n
            for j <- 1 to m
                si, j <- max{si - 1, j + downi, j, si, j - 1 + righti, j}
        return sn, m
    '''
    # init
    s_dic = {(0,0):0}
    
    for i in range(1,n+1):
        s_dic[(i,0)] = s_dic[(i-1,0)] + down_matix[i-1][0]
        
    for j in range(1,m+1):
        s_dic[(0,j)] = s_dic[(0,j-1)] + right_matrix[0][j-1]

    # calulation
    for i in range(1,n+1):
        for j in range(1,m+1):
            s_dic[(i,j)] = max(s_dic[(i-1,j)]+down_matix[i-1][j], s_dic[(i,j-1)] + right_matrix[i][j-1])

    #return
    return s_dic[(n,m)]
    

if __name__ == "__main__":
    # read file and get parameters
    fin = open('mt_input.txt','r')
    n = int(fin.readline().rstrip('\n') )
    m = int(fin.readline().rstrip('\n') )
    line = fin.readline().rstrip('\n')
    down_matix =[]
    while line != '-':
        down_matix.append([int(i) for i in line.split()])
        line = fin.readline().rstrip('\n') 

    right_matrix = [[int(i) for i in line.split()] for line in fin.readlines()]

    
    # run the function 
    output = ManhattanTourist(n,m,down_matix,right_matrix)
    
    # output the results
    with  open('mt_output.txt','w') as fout:
        fout.write ("%s\n" % str(output) )

    from subprocess import call
    call(["open","mt_output.txt"])        

