import findEulerianPath as fep
def pairedComposition(d, read_pairs):
    '''
    CODE CHALLENGE: Solve the String Reconstruction from Read-Pairs Problem.
    Input: An integer d followed by a collection of paired k-mers PairedReads.
    Output: A string Text with (k, d)-mer composition equal to PairedReads.
    
    Sample Input:
    2
    GAGA|TTGA
    TCGT|GATG
    CGTG|ATGT
    TGGT|TGAG
    GTGA|TGTT
    GTGG|GTGA
    TGAG|GTTG
    GGTC|GAGA
    GTCG|AGAT
    
    Sample Output:
    GTGGTCGTGAGATGTTGA    

    ------------------------------------------------------------
    Definitions:
    1. Read-pairs, which are pairs of reads separated by a fixed distance d in the genome 
    2. (k,d)-mer: Given a string Text, a (k,d)-mer is a pair of k-mers in Text separated by distance d.

    Data structure:
    read_pairs: 2d list, [[GAGA,TTGA],....]
    '''
    # 1. get DB_graph from pair_reads
    DB_graph = genDBGraph(read_pairs)
    
    # 2. cal euler path from DB_graph
    euler_path = fep.findEulerianPath(DB_graph)
    
    # 3. covert to seq from euler_path.  
    return genSeqFromKDmersPath(euler_path,d)


def genSeqFromKDmersPath(euler_path,d):
    '''
    input: tuple list as euler_path for kd-mers 
    output: sequence 
    '''
    k = len(euler_path[0][0])
    n = len(euler_path)
    seq_len = k * 2 + d + n - 1

    # 1.fill the first d gaps, get a 2*k+d length seq 
    output_seq = euler_path[0][0] 
    for i in range(d):
        output_seq += euler_path[i+1][0][-1]

    output_seq += euler_path[0][1]

    # 2. linking the remains n-1 
    for i in range(-n+1,0):
        output_seq += euler_path[i][1][-1]

    return output_seq
    
    

def prefix(read_pair):
    return [read_pair[0][:-1],read_pair[1][:-1]]

def suffix(read_pair):
    return [read_pair[0][1:],read_pair[1][1:]]

def genDBGraph(read_pairs):
    '''
    return: db graph as adjacency_dic 
    an edge is defined by: Suffix((TAA | GCC))=Prefix((AAT | CCA))=(AA | CC).
    '''
    read_pairs_dup = read_pairs[:]

    output = {} 
    for pair in read_pairs:
        for pair_dup in read_pairs_dup:
            if suffix(pair) == prefix(pair_dup):
                #print pair,pair_dup
                if pair not in output.keys():
                    output[tuple(pair)] = [tuple(pair_dup)] # cannot use list as key 
                else:
                    output[tuple(pair)].append(tuple(pair_dup))
    return output 
    

if __name__ == "__main__":

    with open('srfrp_input.txt') as fin:
        d = int(fin.readline())
        read_pairs = [ line.rstrip('\n').split('|') for line in fin.readlines()]

    # run 
    output = pairedComposition(d,read_pairs)


    # output the results
    with  open('srftp_output.txt','w') as fout:
        fout.write(output)
                    
    from subprocess import call
    call(["open","srftp_output.txt"])        
    
