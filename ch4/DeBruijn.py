#ri://stackoverflow.com/questions/9835762/find-and-list-duplicates-in-python-list
    
class DeBruijn(PathGraph):
    '''
    Input: An integer k and a string Text.
    Output: DeBruijnk(Text).
    
    Sample Input:
    4
    AAGATTCTCTAC
    
    Sample Output:
    AAG -> AGA
    AGA -> GAT
    ATT -> TTC
    CTA -> TAC
    CTC -> TCT
    GAT -> ATT
    TCT -> CTA,CTC
    TTC -> TCT

    In general, say we have a genome Text, and let PathGraphk(Text) be a
    path consisting of |Text| - k + 1 edges, where the i-th edge of this
    path is labeled by the i-th k-mer in Text and the i-th node of the
    path is labeled by the i-th (k - 1)-mer in Text. The de Bruijn graph
    DeBruijnk(Text) is formed by gluing identically labeled nodes in
    PathGraphk(Text). 
    '''
    
    #DeBruijnk_path = glue()

    def glue(self):
        '''
        Glue the same node
        '''
        self.path = [[self.node[i],self.node[i+1]] for i in range(len(self.edge))]
    
        # sort 
        self.sorted_path = sorted(self.path)

        # create the unique list 
        self.unique_node = sorted(list(set([path[0] for path in self.sorted_path])))

        # combine the duplicate 
        index_list = [0]*(self.edge_no)
        i = 0; j = 0; 
        output =[]
        tmp = []
        while i<(self.edge_no):
            if self.sorted_path[i][0] == self.unique_node[j]:
                if len(tmp) > 0:
                    tmp += [self.sorted_path[i][1]]
                else:
                    tmp += self.sorted_path[i]
                i+=1
            else:
                j+=1
                output.append(tmp)
                tmp =[]
        output.append(tmp)
        return output
    

class PathGraph:
    '''
    PathGraphk(Text) is a
    path consisting of |Text| - k + 1 edges, where the i-th edge of this
    path is labeled by the i-th k-mer in Text and the i-th node of the
    path is labeled by the i-th (k - 1)-mer in Text.
    ''' 
    def __init__(self, k, text):
        '''
        Generate the path graph 
        '''
        self.node = [text[i:i+k-1] for i in range(len(text)-k+2)]
        self.edge = [text[i:i+k] for i in range(len(text)-k+1)]
        self.node_no = len(self.node)
        self.edge_no = len(self.edge)
        
        
if __name__ == "__main__":
    #read file and get parameters
    fin = open('db_input.txt','r')
    k = int(fin.readline().rstrip('\n') )
    Dna = fin.readline().rstrip('\n')
    fin.close()

    # run the class 
    y = DeBruijn(k,Dna)
    output = y.glue()
    
    # output the results
    with  open('db_output.txt','w') as fout:
        for edge in output:
            if len(edge)>2:
                fout.write(','.join([' -> '.join(edge[:-1])] + edge[-1:]) + '\n')
            else:
                fout.write(' -> '.join(edge) + '\n')
                    
    from subprocess import call
    call(["open","db_output.txt"])        
    
