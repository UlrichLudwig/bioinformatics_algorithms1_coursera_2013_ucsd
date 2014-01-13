def calTwoBreakDistance(P, Q):
    '''
    CODE CHALLENGE: Solve the 2-Break Distance Problem.
    Input: Genomes P and Q.
    Output: The 2-break distance d(P, Q).
    
    Sample Input:
    (+1 +2 +3 +4 +5 +6)
    (+1 -3 -6 -5)(+2 -4)
    
    Sample Output:
    3    
    ----------
    Definations:
    1. 2-break distane: minimal number of 2-breaks transforming genome
    P into genome Q 
    2. 2-break distance = blocks(P,Q) - cycle(P,Q)

    '''
    # initial the graph dic, get the key 
    graph_PQ_dic = initBPGraph(P)
    constructBPGraph(P,Q,graph_PQ_dic) # adjancy graph

    return calBlocks(P) - calCycle(graph_PQ_dic)

def calBlocks(P):
    '''
    Calculate number of blocks in P
    input P is given as 2d list 
    '''
    no_blocks = 0
    for p_row in P:
        no_blocks += len(p_row)
    return no_blocks

def calCycle(graph_PQ_dic):
    '''
    Calculate the number of cycles in P & Q breakpoint graph;
    Algorithm: BFS from Algorithm 1 (stanfrod) 2013 coursera week 4. 

    -- init all nodes are unexplored 
    -- for i = 1 to n
       -- if i not yet explored
        -- BFS(G,i)

    BFS(G, start vertex s):
    -- mark s as explored
    -- let Q = queue (FIFO), init with s
    -- while Q != empty:
       -- remove the first node of Q, call it v
       -- for each edge(v,w):
          -- if w unxplored:
             -- mark w as explored
             -- add w to Q (at the end) 
    
    '''
    explored = []
    count = 0
    for i in graph_PQ_dic.keys():
        if i not in explored:
            #            print i 
            BFS(graph_PQ_dic, i,explored)
            count+=1 
    return count

def BFS(graph_dic, s,explored):
    '''
    BFS(G, start vertex s):
    -- mark s as explored
    -- let Q = queue (FIFO), init with s
    -- while Q != empty:
       -- remove the first node of Q, call it v
       -- for each edge(v,w):
          -- if w unxplored:
             -- mark w as explored
             -- add w to Q (at the end) 
    '''
    
    from  collections import deque
    Q = deque([])
    
    explored.append(s)
    Q.append(s)

    while len(Q) != 0:
        v = Q.popleft()
        for w in graph_dic[v]:
            if w not in explored:
                explored.append(w)
                Q.append(w)
    return explored
        
    
    
    
def initBPGraph(P):
    '''
    init the graph_dic 
    '''
    graph_dic ={}
    # get the number of genes 
    no_genes = max(map(lambda i: abs(max(P[i],key=abs)),range(len(P))))
    for i in range(1,no_genes+1):
        graph_dic[str(i)+'-'] = [] # breakpoint start
        graph_dic[str(i)+'+'] = [] # breakpoint end 
    return graph_dic
    
def constructBPGraph(P,Q,graph_PQ_dic):
    '''
    Construct the P_Q breakpoint graph 
    Output in an adjancy dic 
    '''
    constructGraph(P,graph_PQ_dic)
    constructGraph(Q,graph_PQ_dic)

    # make the edges complete because of undirected
    for key,value in graph_PQ_dic.iteritems():
        for val in value:
            if key not in graph_PQ_dic[val]:
                graph_PQ_dic[val].append(key)
    return 
    
def constructGraph(P,graph_dic):
    '''
    Construct the adjancy graph
    '''
    for p_row in P:
        constructGraphFromRow(p_row,graph_dic)
    return 

def constructGraphFromRow(p_row,graph_dic):
    for i in range(len(p_row)-1):
        graph_dic[str(abs(p_row[i]))+('+' if p_row[i]>0 else '-') ].append(str(abs(p_row[i+1])) + ('+' if p_row[i+1]<0 else '-'))
        
    # the last link 
    graph_dic[str(abs(p_row[-1]))+('+' if p_row[-1]>0 else '-') ].append(str(abs(p_row[0])) + ('+' if p_row[0]<0 else '-'))
    return 
        
def getVal(s):
    s= s.split(')')[:-1]
    s= [s2.strip('(') for s2 in s]
    return [[int(i) for i in s2.split(' ')] for s2 in s]


if __name__ == "__main__":
    # read file and get parameters
    with open('ctbd_input.txt','r') as fin:
        s1 = fin.readline().rstrip('\n') 
        s2 = fin.readline().rstrip('\n') 
    P = getVal(s1)
    Q = getVal(s2)

    
    # run the function 

    d = calTwoBreakDistance(P, Q)
    
    # output the results
    print d


    
