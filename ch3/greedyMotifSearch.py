def greedyMotifSearch(Dna,k,t):
    '''
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
    CAG
    CAG
    CAA
    CAA
    CAA        
    ++++++++++++++++++++
    GREEDYMOTIFSEARCH(Dna, k,t)
        form a set of k-mers BestMotifs by selecting 1st k-mers in each string from Dna
        for each k-mer Motif in the 1st string from Dna
            Motif1 <- Motif
            for i = 2 to t
                form Profile from motifs Motif1, ..., Motifi - 1
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
            profile_dic = calProfile(motifs[:i])
            motifs[i] = FindProfileMostProbableKmer.findProfileMostProbableKmer(Dna[i],k,profile_dic)

        if calScore(motifs) < calScore(best_motifs):
            best_motifs =  motifs[:]

    return best_motifs

def convertByCol(twoD_list):
    '''
    similar as transpose 
    ref: http://stackoverflow.com/questions/6473679/python-list-of-lists-transpose-without-zipm-thing
    '''
    return map(list,zip(*twoD_list))



def countMotifs(motifs):
    '''
    generate count matrix: row names follow the order A C G T 
    '''
    t = len(motifs)
    motifs_col_list = convertByCol(motifs)
    a = [[col.count('A'),col.count('C'),col.count('G'),col.count('T')] for col in motifs_col_list]
    return convertByCol(a)

def calScore(motifs):
    '''
    To define scoring, consider t DNA sequences, each of length n, and
    select a k-mer from each sequence to form a collection Motifs, which
    we represent as a t * k motif matrix. 
    
    Using the motif matrix, we can construct the 4 * k count matrix
    Count(Motifs) counting the number of occurrences of each nucleotide
    in each column of the motif matrix; the (i, j)-th element of
    Count(Motifs) stores the number of times that nucleotide i appears
    in column j of Motifs. We will further divide all of the elements in
    the count matrix by t, the number of rows in Motifs. This results in
    a profile matrix P = Profile(Motifs) for which Pi,j is the frequency
    of the i-th nucleotide in the j-th column of the motif matrix. Note
    that the elements of any column of the profile matrix sum to 1. The
    figure below shows the motif, count, and profile matrices for the
    NF-kB binding sites; note that positions 3 and 4 are the most
    conserved (nucleotide G is completely conserved in these positions),
    whereas position 11 is the least conserved.   

    Motifs
    T   C   G   G   G   G   g   T   T   T   t   t           
    c   C   G   G   t   G   A   c   T   T   a   C
    a   C   G   G   G   G   A   T   T   T   t   C
    T   t   G   G   G   G   A   c   T   T   t   t
    a   a   G   G   G   G   A   c   T   T   C   C
    T   t   G   G   G   G   A   c   T   T   C   C
    T   C   G   G   G   G   A   T   T   c   a   t
    T   C   G   G   G   G   A   T   T   c   C   t
    T   a   G   G   G   G   A   a   c   T   a   C
    T   C   G   G   G   t   A   T   a   a   C   C

    Score
    3 + 4 + 0 + 0 + 1 + 1 + 1 + 5 + 2 + 3 + 6 + 4 = 30     

    Count
    A:   2   2   0   0   0   0   9   1   1   1   3   0          
    C:   1   6   0   0   0   0   0   4   1   2   4   6  
    G:   0   0  10  10   9   9   1   0   0   0   0   0  
    T:   7   2   0   0   1   1   0   5   8   7   3   4  

    Profile
    A:  .2  .2   0   0   0   0  .9  .1  .1  .1  .3   0            
    C:  .1  .6   0   0   0   0   0  .4  .1  .2  .4  .6  
    G:   0   0   1   1  .9  .9  .1   0   0   0   0   0  
    T:  .7  .2   0   0  .1  .1   0  .5  .8  .7  .3  .4  

    Consensus
    T   C   G   G   G   G   A   T   T   T   C   C     
    '''
    count_list = countMotifs(motifs)
    count_col_list = convertByCol(count_list)
    
    t = len(motifs)
    score = sum([t-max(count) for count in count_col_list])
    return score



def calProfile(motifs):
    '''
    form Profile from motifs Motif0, ..., Motifi - 2
    Output: profile_dic
    '''
    count_list = countMotifs(motifs)
    t = len(motifs)

    ACGT = ['A','C','G','T']
    profile_dic = {}

    for ind,row in enumerate(count_list):        
        profile_dic[ACGT[ind]] =  [item/float(t) for item in row] 
    return profile_dic

if __name__ == "__main__":
    # read file and get parameters
    fin = open('gms_input.txt','r')
    tmp = fin.readlines()
    k = int(tmp[0].split()[0])    
    t = int(tmp[0].split()[1])        
    Dna =[s.rstrip('\n') for s in tmp[1:]] 

    # run the function 
    motif = greedyMotifSearch(Dna,k,t)
    
    # output the results
    with  open('gms_output.txt','w') as fout:
        for s in motif:
            fout.write ("%s \n" % s )

    from subprocess import call
    call(["open","gms_output.txt"])        
        
