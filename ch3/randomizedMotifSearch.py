import greedyMotifSearchWithPseudocounts as gmsp
import greedyMotifSearch as gms

def randomizedMotifSearch(Dna,k,t):
    '''
    Input: Integers k and t, followed by a collection of strings Dna.
    Output: A collection BestMotifs resulting from running RANDOMIZEDMOTIFSEARCH(Dna, k, t) 1000 times.
    Remember to use pseudocounts!

    Sample Input:
    8 5
    CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA
    GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG
    TAGTACCGAGACCGAAAGAAGTATACAGGCGT
    TAGATCAAGTTTCAGGTGCACGTCGGTGAACC
    AATCCACCAGCTCCACGTGCAATGTTGGCCTA

    Sample Output:
    TCTCGGGG
    CCAAGGTG
    TACAGGCG
    TTCAGGTG
    TCCACGTG
    '''
    
    
    #randomly select k-mers Motifs = (Motif1, ..., Motift) in each string from Dna
    motifs = randomSelect(Dna,k,t)
    best_motifs = motifs[:]
    
    while True:
        profile_dic = gmsp.calProfile2(motifs)
        motifs = generateMotifs(profile_dic, Dna, k)
        if gms.calScore(motifs) < gms.calScore(best_motifs):
            best_motifs = motifs[:]
        else:
            return best_motifs

def randomSelect(Dna,k,t):
    '''
    randomly select k-mers Motifs = (Motif1, ..., Motift) in each string from Dna
    '''
    import random
    # init the seed by time
    random.seed()
    output_kmers = []
    for i in range(t):
        ind = random.choice(range(len(Dna[0])-k+1))
        output_kmers.append(Dna[i][ind:ind+k])
    return output_kmers

def generateMotifs(profile_dic, Dna, k):
    '''
    we define Motifs(Profile,Dna) as a collection of k-mers formed by
    the Profile-most probable k-mers in each sequence from Dna. For
    example, consider the following Profile and Dna:  

                      A:  4/5  0    0  1/5               ttaccttaac
            Profile   C:   0  3/5  1/5  0          Dna   gatgtctgtc
                      G:  1/5 1/5  4/5  0                acggcgttag
                      T:   0  1/5   0  4/5               ccctaacgag
                                                         cgtcagaggt

    Taking the Profile-most probable 4-mer from each row of Dna produces
    the following 4-mers (shown in red): 

                                             ttACCTtaac
                                             gATGTctgtc
                       Motifs(Profile,Dna)   acgGCGTtag
                                             ccctaACGAg
                                             cgtcagAGGT                                                         
    '''
    import FindProfileMostProbableKmer as fpmpk
    return [fpmpk.findProfileMostProbableKmer(Dna_fragment,k,profile_dic) for Dna_fragment in Dna]



            
if __name__ == "__main__":
    # read file and get parameters
    fin = open('rms_input.txt','r')
    tmp = fin.readlines()
    k = int(tmp[0].split()[0])    
    t = int(tmp[0].split()[1])        
    Dna =[s.rstrip('\n') for s in tmp[1:]] 

    # run the function 
    best_motifs = randomizedMotifSearch(Dna,k,t)
    best_score = gms.calScore(best_motifs)
    
    for i in range(999):
        motifs = randomizedMotifSearch(Dna,k,t)
        current_score = gms.calScore(motifs)
        if current_score < best_score:
            best_motifs = motifs
            best_score = current_score 
    
    # output the results
    with  open('rms_output.txt','w') as fout:
        for s in best_motifs:
            fout.write ("%s\n" % s )

    from subprocess import call
    call(["open","rms_output.txt"])        
