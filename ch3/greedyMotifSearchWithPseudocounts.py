import greedyMotifSearch 
    
def greedyMotifSearch2(Dna,k,t):
    '''
    GREEDYMOTIFSEARCH implementation to incorporate pseudocounts.
    Input: Integers k and t, followed by a collection of strings Dna.

    Output: A collection of strings BestMotifs resulting from applying
    GREEDYMOTIFSEARCH(Dna,k,t). If at any step you find more than one
    Profile-most probable k-mer in a given string, use the one occurring
    first. 
    ====================
    Sample Input:
    3 5
    GGCGTTCAGGCA
    AAGAATCAGTCA
    CAAGGAGTTCGC
    CACGTCAATCAC
    CAATAATATTCG

    Sample Output:
    TTC
    ATC
    TTC
    ATC
    TTC
    ++++++++++++++++++++
    GREEDYMOTIFSEARCH2(Dna, k,t)
        form a set of k-mers BestMotifs by selecting 1st k-mers in each string from Dna
        for each k-mer Motif in the 1st string from Dna
            Motif1 <- Motif
            for i = 2 to t
                apply Laplace's rule to form Profile from motifs Motif1, ..., Motifi - 1
                Motifi <- Profile-most probable k-mer in the i-th string in Dna
            Motifs <- (Motif1, ..., Motift)
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs <- Motifs
        output BestMotifs
    '''
    # motif from previous parctice:
    import FindProfileMostProbableKmer
    
    #form a set of k-mers BestMotifs by selecting 1st k-mers in each
    #string from Dna 
    best_motifs = [Dna_fragment[:k] for Dna_fragment in Dna]
    motifs = best_motifs[:]    
    
    for motif in [Dna[0][i:i+k] for i in range(len(Dna[0])-k+1)] :
        motifs[0] = motif
        
        for i in range(1,t): #1 to t-1
            #form Profile from motifs Motif0, ..., Motifi - 1
            profile_dic = calProfile2(motifs[:i])
            motifs[i] = FindProfileMostProbableKmer.findProfileMostProbableKmer(Dna[i],k,profile_dic)

        if greedyMotifSearch.calScore(motifs) < greedyMotifSearch.calScore(best_motifs):
            best_motifs =  motifs[:]
    return best_motifs

def calProfile2(motifs):
    '''
    form Profile from motifs Motif0, ..., Motifi - 2
    Output: profile_dic
    '''
    count_list = countMotifs2(motifs)
    t = len(motifs) + 4 

    ACGT = ['A','C','G','T']
    profile_dic = {}

    for ind,row in enumerate(count_list):        
        profile_dic[ACGT[ind]] =  [item/float(t) for item in row] 
    return profile_dic

def countMotifs2(motifs):
    '''
    generate count matrix: row names follow the order A C G T 
    '''
    t = len(motifs)
    motifs_col_list = greedyMotifSearch.convertByCol(motifs)
    a = [[col.count('A')+1,col.count('C')+1,col.count('G')+1,col.count('T')+1] for col in motifs_col_list]
    return greedyMotifSearch.convertByCol(a)

if __name__ == "__main__":
    # read file and get parameters
    fin = open('gms2_input.txt','r')
    tmp = fin.readlines()
    k = int(tmp[0].split()[0])    
    t = int(tmp[0].split()[1])        
    Dna =[s.rstrip('\n') for s in tmp[1:]] 

    # run the function 
    motif = greedyMotifSearch2(Dna,k,t)
    
    # output the results
    with  open('gms2_output.txt','w') as fout:
        for s in motif:
            fout.write ("%s\n" % s )

    from subprocess import call
    call(["open","gms2_output.txt"])        
        
