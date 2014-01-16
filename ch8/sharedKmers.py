def sharedKmers(str1,str2,k):
    '''
    Shared k-mers Problem: Given two strings, find all their shared k-mers.
    
    Input: An integer k and two strings.
    Output: All k-mers shared by these strings, in the form of ordered pairs (x, y).
    
    CODE CHALLENGE: Solve the Shared k-mers Problem.
    
    Sample Input:
    3
    AAACTCATC
    TTTCAAATC
    
    Sample Output:
    (0, 4)
    (0, 0)
    (4, 2)
    (6, 6)
    ----------------------------------------
    Definition:
    We say that a k-mer is shared by two genomes if either the k-mer or
    its reverse complement appears in each genome.  
    '''
    output = []

    sharedKmersBasic(str1,str2,k,output,False)
    sharedKmersBasic(str1,reverse(str2),k,output,True)

    return output 

def sharedKmersBasic(str1,str2,k,output,reverse_flag):
    '''
    Basic shared k mers finding. not including reverse complementry 
    '''
    if reverse_flag:
        all_kmers_str2 = [str2[i:i-k:-1] for i in range(k,len(str2))]
        all_kmers_str2 = str2[k::-1] + all_kmers_str2
    else:
        all_kmers_str2 = [str2[i:i+k] for i in range(len(str2)-k+1)]

    for i in range(len(str1)-k+1):
        if str1[i:i+k] in all_kmers_str2:
            all_index = all_indices(str1[i:i+k], all_kmers_str2)
            for j in all_index:
                output.append([i,j])
    return 

def all_indices(value, qlist):
    indices = []
    idx = -1
    while True:
        try:
            idx = qlist.index(value, idx+1)
            indices.append(idx)
        except ValueError:
            break
    return indices



def reverse(str):
    '''
    get the reverse complement of str
    '''
    codon_dic = {'A':'T','T':'A','C':'G','G':'C'}
    str_reverse = ''
    for s in str:
        str_reverse += codon_dic[s]
    return str_reverse 

    


if __name__ == "__main__":
    # read file and get parameters
    with open('sk_input.txt','r') as fin:
        k = int(fin.readline())
        str1 = fin.readline().rstrip('\n') 
        str2 = fin.readline().rstrip('\n') 

    output = sharedKmers(str1,str2,k)

    with open('sk_output.txt','w') as fout:
        for val in output:
            fout.write('(%s)\n' % (str(val[0])+', '+str(val[1])))

    from subprocess import call
    call(["open","sk_output.txt"])        


    
    
