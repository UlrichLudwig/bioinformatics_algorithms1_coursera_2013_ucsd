
import overlapGraph as og


def getDeBruijnFromPatten(pattern):
    '''
     Input: A collection of k-mers Patterns.
     Output: The adjacency list of the de Bruijn graph DeBruijn(Patterns).
    '''

    all_paths = [[og.prefix(kmer),og.suffix(kmer)] for kmer in pattern]
    return glue(all_paths)     


    
def glue(paths):
    '''
    Glue the same node
    '''
    
    # sort 
    sorted_paths = sorted(paths)
    edge_no = len(paths)
    
    # create the unique list 
    unique_node = sorted(list(set([path[0] for path in sorted_paths])))
    
    # combine the duplicate 
    index_list = [0]*(edge_no)
    i = 0; j = 0; 
    output =[]
    tmp = []
    while i<(edge_no):
        if sorted_paths[i][0] == unique_node[j]:
            if len(tmp) > 0:
                tmp += [sorted_paths[i][1]]
            else:
                tmp += sorted_paths[i]
            i+=1
        else:
            j+=1
            output.append(tmp)
            tmp =[]
    output.append(tmp)
    return output 
        
if __name__ == "__main__":
    #read file and get parameters
    with open('dbfp_input.txt','r') as fin:
        pattern = [line.rstrip('\n') for line in fin.readlines()]

    # run the class 
    output = getDeBruijnFromPatten(pattern)
    
    # output the results
    with  open('dbfp_output.txt','w') as fout:
        for edge in output:
            if len(edge)>2:
                fout.write(','.join([' -> '.join(edge[:-1])] + edge[-1:]) + '\n')
            else:
                fout.write(' -> '.join(edge) + '\n')
                    
    from subprocess import call
    call(["open","dbfp_output.txt"])        
    
