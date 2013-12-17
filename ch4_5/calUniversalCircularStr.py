import DeBruijnFromPattern as dbfp
import findEulerianCycle as fec

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

    kmers_all = getAllKmers(k)
    #print kmers_all
    
    kmers_graph_dic = genKmerGraph(kmers_all)
    #print kmers_graph_dic
    
    k_circle = fec.findEulerianCycle(kmers_graph_dic)
    #print k_circle
    k_str = DBcycleToStr(k_circle)

    return k_str

def getAllKmers(k):
    if k==1:
        return['0','1']
    else:
        tmp = getAllKmers(k-1)
        return [s+'0' for s in tmp] + [s +'1' for s in tmp]


def genKmerGraph(kmers):
    db_grpah_list = dbfp.getDeBruijnFromPatten(kmers)    
    return {edge[0]:edge[1:] for edge in db_grpah_list}

    
def DBcycleToStr(circle):
    DB_edges = DBcycleToEdge(circle)
    #print DB_edges
    return DBedgeToStr(DB_edges)

def DBcycleToEdge(circle):
    return [circle[i] + circle[i+1][-1] for i in range(len(circle)-2)] + [circle[-2][-1]+circle[-1]]

def DBedgeToStr(DB_edges):
    output = DB_edges[0][-1]
    for edge in DB_edges[1:]:
        output += edge[-1]
    return output

if __name__ == "__main__":
    #read file and get parameters
    with open('cucs_input.txt','r') as fin:
        k = int(fin.readline())
                                        
    # run 
    output = calUniversalCircularStr(k)


    # output the results
    with  open('cucs_output.txt','w') as fout:
        fout.write(output)
                    
    from subprocess import call
    call(["open","cucs_output.txt"])        


     
