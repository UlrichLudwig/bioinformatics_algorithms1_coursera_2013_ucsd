import overlapGraph

# http://stackoverflow.com/questions/9835762/find-and-list-duplicates-in-python-list
    
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
    self.path = [[self.node[i],self.node[i+1]] for i in range(len(self.edge)-1)]

    def glue(self):
        '''
        Glue the same edge
        '''
        # sort 
        self.path_sorted = sorted(self.path)

        # create the unique list 
        self.unique_node = list(set([path[0] for path in self.path_sorted]))

        # combine the duplicate 
        tmp_path = self.path_sorted[:]

        #
        self.output = []

        for i in range(len(self.path_sorted)-1):
            for j in range(i+1,len(self.path_sorted)):
                if self.path_sorted[i][0] == self.path_sorted[j]

    def isOverlapPath(self,path1,path2):
        if path1[0] = path2[0]:
            return [path1[0],path1[1],path2[1]]
        else:
            return 
    
        
                       
        
        
    

class PathGraph
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
        
        
        

        
    
