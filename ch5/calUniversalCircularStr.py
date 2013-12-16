import findEulerianPath as fep

def calUniversalCircularStr(k):
    '''
    CODE CHALLENGE: Solve the k-Universal Circular String Problem.
    Input: An integer k.
    Output: A k-universal circular string.
    
    Sample Input:
    4
    
    Sample Output:
    0000110010111101
    '''
    output_list = fep.findEulerianPath(adjacency_dic)
    output_str = output_list[0][:-1]
    k = len(output_list[0])
    for kmer in output_list:
        output_str +=kmer[-1]
    return output_str

if __name__ == "__main__":
    #read file and get parameters
    adjacency_dic = {}
    with open('feps_input.txt','r') as fin:
        for line in fin.readlines():
            line = line.rstrip('\n')
            tmp = line.split(' -> ')
            adjacency_dic[tmp[0]] = [a for a in tmp[1].split(',')]
                                        

    # run 
    output = findEulerianPathString(adjacency_dic)


    # output the results
    with  open('feps_output.txt','w') as fout:
        fout.write(output)
                    
    from subprocess import call
    call(["open","feps_output.txt"])        


     
