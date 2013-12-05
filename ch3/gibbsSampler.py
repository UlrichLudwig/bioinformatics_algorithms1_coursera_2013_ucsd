import greedyMotifSearch as gms
def gibbsSampler(Dna,k,t,N):
    '''
    Input: Integers k, t, and N, followed by a collection of strings Dna.
    Output: The strings BestMotifs resulting from running GIBBSSAMPLER(Dna, k, t, N) with
    20 random starts. Remember to use pseudocounts!

    Sample Input:
    8 5 100
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
    ====================
    NOTE:
    Note: As with RANDOMIZEDMOTIFSEARCH, there is a very small chance
    that your algorithm may be implemented correctly but not return the
    correct answer. We suggest running your algorithm on another dataset
    if you do not get the correct answer the first time.     

    Algorithm:
    GIBBSSAMPLER(Dna, k, t, N)
        randomly select k-mers Motifs = (Motif1, ..., Motift) in each string from Dna
        BestMotifs <- Motifs
        for i from 1 to N
            i <- Random(t)
            construct profile matrix Profile from all strings in Motifs except for Motifi
            Motifi <- Profile-randomly generated k-mer in the i-th sequence
            if Score(Motifs) < Score(BestMotifs)
                BestMotifs <- Motifs
        output BestMotifs

        We have previously defined the notion of a Profile-most probable
        k-mer in a string. We now define a Profile-randomly generated
        k-mer in a string Text. For each k-mer Pattern in Text, compute
        Pr(Pattern | Profile), resulting in n = |Text| - k + 1
        probabilities (p1,..., pn). These probabilities do not
        necessarily sum to 1, but we can still form a random number
        generator based on them. GIBBSSAMPLER uses this random number
        generator to randomly select a Profile-randomly generated k-mer
        at each step. If the die rolls the number i, we define the
        Profile-randomly generated k-mer as the i-th k-mer in Text.
        While the pseudocode below repeats this procedure a fixed number
        of times (N), in practice GIBBSSAMPLER depends on various
        stopping rules that are beyond the scope of this chapter         
        '''

    import randomizedMotifSearch as rms
    import greedyMotifSearchWithPseudocounts as gmsp

    import random
    
    #randomly select k-mers Motifs = (Motif1, ..., Motift) in each string from Dna
    motifs = rms.randomSelect(Dna,k,t)
    #BestMotifs <- Motifs
    best_motifs = motifs[:]

    for i in range(N):
        i = random.choice(range(t))
        # construct profile matrix Profile from all strings in Motifs except for Motifi
        profile_dic = gmsp.calProfile2([motif for ind,motif in enumerate(motifs) if ind != i])
        
        #Motifi <- Profile-randomly generated k-mer in the i-th sequence
        motifs[i] = profileRandomlyGenerateKmer(Dna[i],k,profile_dic)
        
        if gms.calScore(motifs) < gms.calScore(best_motifs):
            best_motifs = motifs[:]
    return best_motifs

def profileRandomlyGenerateKmer(text,k,profile_dic):
    '''
    We now define a Profile-randomly generated
    k-mer in a string Text. For each k-mer Pattern in Text, compute
    Pr(Pattern | Profile), resulting in n = |Text| - k + 1
    probabilities (p1,..., pn). These probabilities do not
    necessarily sum to 1, but we can still form a random number
    generator based on them.If the die rolls the number i, we define the
    Profile-randomly generated k-mer as the i-th k-mer in Text.

    input: string text, length k, profile dic
    output: motif, randomly selected by the random generator 
    '''
    import FindProfileMostProbableKmer as fpmpk

    n = len(text) - k +1
    all_kmers =  [text[i:i+k] for i in range(n)]
    pr = [fpmpk.calProbKmer(kmer,profile_dic) for kmer in all_kmers]
    ind = weightedRandomSelect(pr,n)

    return all_kmers[ind]

def weightedRandomSelect(pr,n):
    '''
    input: Weighted probabilities, n number of probabilities 
    output: a random selected index in range(n) based on corresponding probability
    '''

    import random 
    random.seed()

    a = random.random() * sum(pr)
    sum_pr = 0
    for i in range(n-1):
        if a>=sum_pr and a<sum_pr+pr[i]:
            return i
        sum_pr +=pr[i]
    return n-1

if __name__ == "__main__":
    # read file and get parameters
    fin = open('gs_input.txt','r')
    tmp = fin.readlines()
    k = int(tmp[0].split()[0])    
    t = int(tmp[0].split()[1])        
    N = int(tmp[0].split()[2])        
    Dna =[s.rstrip('\n') for s in tmp[1:]] 

    # run the function 
    best_motifs = gibbsSampler(Dna,k,t,N)
    best_score = gms.calScore(best_motifs)
    
    for i in range(200):
        print i
        motifs = gibbsSampler(Dna,k,t,N)
        current_score = gms.calScore(motifs)
        if current_score < best_score:
            best_motifs = motifs
            best_score = current_score 

    
    # output the results
    with  open('gs_output.txt','w') as fout:
        for s in best_motifs:
            fout.write ("%s\n" % s )

    from subprocess import call
    call(["open","gs_output.txt"])        


    
    
    
