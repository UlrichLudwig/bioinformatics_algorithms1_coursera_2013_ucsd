import findEulerianCycle as fec
def findEulerianPath(adjacency_dic):
    '''
    input: adjacency_list 
    output: the eulerian path as a list 
    Sample Input:
     0 -> 2
     1 -> 3
     2 -> 1
     3 -> 0,4
     6 -> 3,7
     7 -> 8
     8 -> 9
     9 -> 6
     
     Sample Output:
     6->7->8->9->6->3->0->2->1->3->4

     in sample: 
     odd_in_vertex = 6 (in_degree(6) = 1 < out_degree(6) = 2 ) 
     odd_out_vertex = 4 (in_degree(4) =1 > out_degree(4) = 0)
     add a edge: 4 -> 6 
     eulerian cycle is 3->4->6->7->8->9->6->3->0->2->1->3
     
    '''
    # 1. find odd vertex odd_in_vertex and odd_out_vertex 
    all_vertex = getAllVertex(adjacency_dic)

    for vertex in all_vertex:
        in_degree = calIn(adjacency_dic,vertex)
        out_degree = calOut(adjacency_dic,vertex)
        if in_degree > out_degree:
            odd_out_vertex = vertex
        elif in_degree < out_degree:
            odd_in_vertex = vertex

    # 2. add a edge odd_in_vertex -> odd_out_vertex into adjacency_list
    added_edge = [odd_out_vertex,odd_in_vertex]
    if odd_out_vertex in adjacency_dic.keys():
        adjacency_dic[odd_out_vertex].append(odd_in_vertex)
    else:
        adjacency_dic[odd_out_vertex]=[odd_in_vertex]
        
    # 3. find Eulerian cycle from new adjacency_list
    eulerian_cycle = fec.findEulerianCycle(adjacency_dic)
    
    # 4. getEulerianPathFromCycle. 
    eulerian_path = getEulerianPathFromCycle(eulerian_cycle,added_edge)

    return eulerian_path


def getAllVertex(adjacency_dic):
    key_list = adjacency_dic.keys()
    
    value_list = []
    for val in adjacency_dic.values():
        value_list += val

    return list(set(key_list + value_list))

def calIn(adjacency_dic,vertex):
    count = 0 
    for val in adjacency_dic.values():
        count += val.count(vertex)
    return count 

def calOut(adjacency_dic,vertex):
    if vertex in adjacency_dic.keys():
        return len(adjacency_dic[vertex])
    else:
        return 0

def getEulerianPathFromCycle(eulerian_cycle,added_edge):
    for ind,vertex in enumerate(eulerian_cycle):
        if vertex == added_edge[0] and eulerian_cycle[ind+1] ==added_edge[1]:
            break
    return eulerian_cycle[ind+1:] + eulerian_cycle[1:ind+1]
        
    

if __name__ == "__main__":
    #read file and get parameters
    adjacency_dic = {}
    with open('fep_input.txt','r') as fin:
        for line in fin.readlines():
            line.rstrip('\n')
            tmp = line.split('->')
            adjacency_dic[int(tmp[0])] = [int(a) for a in tmp[1].split(',')]
                                        

    # run 
    output = findEulerianPath(adjacency_dic)


    # output the results
    with  open('fep_output.txt','w') as fout:
        fout.write('->'.join([str(a) for a in output]))
                    
    from subprocess import call
    call(["open","fep_output.txt"])        
