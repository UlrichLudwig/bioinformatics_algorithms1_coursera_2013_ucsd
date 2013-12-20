def LongestPathInDAG(source, sink, DAG,result):
    '''
    S_a = max_{all predecessors b of node a}(S_b + weight of edge from b to a)
    '''
    pre_list = getPredecessors(a,DAG) 


    for b in pre_list:
        result += LongestPathInDAG(source,b,DAG) + getWeight(b,a,DAG)
        return max(result)
    
def getPredecessors(a,DAG):
    return [DAG[i][0] for i in range(len(DAG)) if DAG[i][1] ==a]

def getWeight(b,a,DAG):
    for i in range(len(DAG)):
        if DAG[i][:2] == [b,a]:
            return DAG[i][2]
    
    
def customRead(str):
    tmp = str.split('->')
    return [int(tmp[0])] + [int(i) for i in tmp[1].split(':')]
    
if __name__ == "__main__":
    # read file and get parameters
    with open('lpid_input.txt','r') as fin:
        source = int(fin.readline().rstrip('\n') )
        sink = int(fin.readline().rstrip('\n') )
        tmp = [line.rstrip('\n') for line in fin.readlines()]
        DAG = map(customRead,tmp)

    
    # run the function 
    result = []
    LongestPathInDAG(source,sink,DAG,result)
    
    # output the results
    with  open('lpid_output.txt','w') as fout:
        fout.write ("%d\n" % output)

    from subprocess import call
    call(["open","lpid_output.txt"])        
