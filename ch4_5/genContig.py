import DeBruijnFromPattern as dbfp
import findEulerianPath as fep


def genContig(patterns):
    '''
    Contig Generation Problem: Generate the contigs from a collection of
    reads (with imperfect coverage). 
    
    Input: A collection of k-mers Patterns.
    Output: All contigs in DeBruijn(Patterns).
    
    CODE CHALLENGE: Solve the Contig Generation Problem.
    
    Sample Input:
    ATG
    ATG
    TGT
    TGG
    CAT
    GGA
    GAT
    AGA
    
    Sample Output:
    AGA ATG ATG CAT GAT TGGA TGT
    ------------------------------------------------------------
    DEFINITION:
    1. Contig: (long, contiguous segments of the genome) -- by  maximal
    non-branching path spell out 
    2. A path in a graph is called *non-branching* if in(v) = out(v) = 1  
    3. A maximal non-branching path is a non-branching path that cannot
    be extended into a longer non-branching path. 
    '''
    DB_graph_list = dbfp.getDeBruijnFromPatten(patterns)
    DB_graph_dic = {edge[0]:edge[1:] for edge in DB_graph_list}

    paths  =genMaxNonBranchingPath(DB_graph_dic)
    return [pathToStr(path) for path in paths]

def pathToStr(path):
    output = path[0]
    for i in range(1,len(path)):
        output += path[i][-1]
    return output 
            
    
def genMaxNonBranchingPath(DB_graph_dic):
    '''
    Return: all maxNonBranchingPath as string list 
    '''
    all_vertex = fep.getAllVertex(DB_graph_dic)
    in_degree_list = map((lambda vertex: fep.calIn(DB_graph_dic,vertex)),all_vertex)
    out_degree_list = map((lambda vertex: fep.calOut(DB_graph_dic,vertex)),all_vertex)
    degree_dic = {all_vertex[i]:[in_degree_list[i],out_degree_list[i]] for i in range(len(all_vertex))}   

    
    

    # buid one path from the start_node and delete the path from graph 
    paths =[]

    while len(DB_graph_dic)>0:
        # start from the first vertex that out_degree >0 :c
        start_node = findStart(DB_graph_dic,degree_dic)
        paths.append(genPath(DB_graph_dic,start_node,degree_dic))

    return paths 

def findStart(DB_graph_dic,degree_dic):
    for key in DB_graph_dic.keys():
        if degree_dic[key]!= [1,1]:
            return key 
        
def genPath(DB_graph_dic,start_node,degree_dic):
    path = [];

    # check 1st edge. 
    path.append(start_node) # add 1st vertex
    #print start_node,DB_graph_dic
    #raw_input('wait')
   
    while True:
        current_vertex = DB_graph_dic[start_node][0]#mv to the next vertex 
        if degree_dic[current_vertex] != [1,1] or current_vertex not in DB_graph_dic.keys(): # stop and save it but not continue
            path.append(current_vertex)
            delNode(DB_graph_dic,start_node)    
            return path
        else:            # save it & continue 
            path.append(current_vertex)
            delNode(DB_graph_dic,start_node)  # del 
            start_node = current_vertex #mv start 
        

def delNode(DB_graph_dic,vertex):
    if vertex in DB_graph_dic.keys():
        DB_graph_dic[vertex].remove(DB_graph_dic[vertex][0])
        if len(DB_graph_dic[vertex]) == 0:
            del DB_graph_dic[vertex]

    
if __name__ == "__main__":

    with open('gc_input.txt') as fin:
        patterns = [ line.rstrip('\n') for line in fin.readlines()]

    # run 
    output = genContig(patterns)


    # output the results
    with  open('gc_output.txt','w') as fout:
        for p in output:
            fout.write(p+'\n')
                    
    from subprocess import call
    call(["open","gc_output.txt"])        
    
