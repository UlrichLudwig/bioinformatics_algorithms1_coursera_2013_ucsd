def findEulerianCycle(adjacency_dic):
    '''
    Input: The adjacency list of an Eulerian directed graph.
    Output: An Eulerian cycle in this graph.
    
    Sample Input:
    0 -> 3
    1 -> 0
    2 -> 1,6
    3 -> 2
    4 -> 2
    5 -> 4
    6 -> 5,8
    7 -> 9
    8 -> 7
    9 -> 6
    
    Sample Output:
    6->8->7->9->6->5->4->2->1->0->3->2->6

    ------------------------------------------------------------
        EULERIANCYCLE(Graph)
        form a cycle Cycle by randomly walking in Graph (never visit an edge twice!)
        while there are unexplored edges
            select a node newStart in Cycle with still unexplored edges
            form Cycle' by traversing Cycle (starting at newStart) and randomly walking 
            Cycle <- Cycle'
        return Cycle
    '''
    start_node = adjacency_dic.keys()[0]
    cycle = findCycle(adjacency_dic,start_node)
    #print start_node,cycle
    while len(adjacency_dic) >0:
        start_node = findStart(adjacency_dic,cycle)
        cycle = combineCycle(cycle,findCycle(adjacency_dic,start_node))
        #print start_node,cycle
        #raw_input("Press Enter to continue...")
    return cycle 
        
def findStart(adjacency_dic,cycle):
    '''
    find start node from adjacency_dic based on existing cycle 
    ''' 
    for key in adjacency_dic.keys():
        if key in cycle:
            return key 
    return False 
            
    
def findCycle(adjacency_dic, start_node):
    '''
    find a cycle from a adjacency_dic with a specified start node 
    '''

    cycle = []
    cycle.append(start_node)
    
    current_vertex = adjacency_dic[start_node][0]
    adjacency_dic[start_node].remove(adjacency_dic[start_node][0])
    if len(adjacency_dic[start_node])==0:
        del adjacency_dic[start_node]
    
    cycle.append(current_vertex)
     
    while current_vertex != start_node:
        next_vertex = adjacency_dic[current_vertex][0]
        adjacency_dic[current_vertex].remove(adjacency_dic[current_vertex][0])
        if len(adjacency_dic[current_vertex])==0:
            del adjacency_dic[current_vertex]
        current_vertex = next_vertex
        cycle.append(current_vertex)
        
        #print cycle,current_vertex

    return cycle
        
def combineCycle(old_cycle,new_cycle):
    ind = old_cycle.index(new_cycle[0])
    return new_cycle + old_cycle[ind+1:]+old_cycle[1:ind+1]
    
if __name__ == "__main__":
    #read file and get parameters
    adjacency_dic = {}
    with open('fec_input.txt','r') as fin:
        for line in fin.readlines():
            line.rstrip('\n')
            tmp = line.split('->')
            adjacency_dic[int(tmp[0])] = [int(a) for a in tmp[1].split(',')] 
                                        

    # run 
    output = findEulerianCycle(adjacency_dic)


    # output the results
    with  open('fec_output.txt','w') as fout:
        fout.write('->'.join([str(a) for a in output]))
                    
    from subprocess import call
    call(["open","fec_output.txt"])        

