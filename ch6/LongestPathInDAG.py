def LongestPathInDAG(source, sink, DAG, seq):
    '''
    S_a = max_{all predecessors b of node a}(S_b + weight of edge from b to a)

    Sample Input:
     0
     4
     0->1:7
     0->2:4
     2->3:2
     1->4:1
     3->4:3

     s(0) = 0
     s(1) = 7
     s(2) = 4
     s(3) = s(2) + 2
     s(4) = max(s(3) + 3, s(1) + 1) 

     Sample Output:
     9
     0->2->3->4
     '''
    result = []
    if source == sink:
        return 0

    pre_list = getPredecessors(sink,DAG) 
    if len(pre_list) ==0:
        return -999999

    for b in pre_list:
        #        print b
        #raw_input('wait')
        c = LongestPathInDAG(source,b,DAG,seq)
        d = getWeight(b,sink,DAG)
        #seq[b] = c
        
        result += [c + d]
        #        print c,d,sink,result
        
    seq[sink] =pre_list[max(enumerate(result),key=lambda x: x[1])[0]]
    return max(result)
    
def getPredecessors(a,DAG):
    return [DAG[i][0] for i in range(len(DAG)) if DAG[i][1] ==a]

def getWeight(b,a,DAG):
    '''
    weight for edge from b->a
    '''
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
    seq = {}
    output = LongestPathInDAG(source,sink,DAG,seq)
    result =[]

    tmp =sink
    while tmp != source:
        result.append(tmp)
        tmp = seq[tmp]
        
    result.append(source)
    result = '->'.join([str(i) for i in result[-1::-1] ])
    #print result

    
    # output the results
    with  open('lpid_output.txt','w') as fout:
        fout.write('%d\n'% output)
        fout.write ( result)

    from subprocess import call
    call(["open","lpid_output.txt"])        
