def composition(k, text):
    '''
    Given a string Text, its k-mer composition Compositionk(Text) is the
    collection of all k-mer substrings of Text (including repeated
    k-mers) in lexicographic order. For example, 

    Composition3(TATGGGGTGC) = ATG, GGG, GGG, GGT, GTG, TAT, TGC, TGG
    
    Solve the String Composition Proble
    Input: An integer k and a string Text.
    Output: Compositionk(Text), where the k-mers are written in
    lexicographic order. 
    
    Sample Input:
    5
    CAATCCAAC
    
    Sample Output:
    AATCC
    ATCCA
    CAATC
    CCAAC
    TCCAA
    '''
    return sorted([text[i:i+k] for i in range(len(text)-k+1)])

if __name__ == "__main__":
    # read file and get parameters
    fin = open('c_input.txt','r')
    k = int(fin.readline().rstrip('\n') )
    Dna = fin.readline().rstrip('\n')
    fin.close()
    # run the function 
    kmers = composition(k,Dna)
    
    # output the results
    with  open('c_output.txt','w') as fout:
        for s in kmers:
            fout.write ("%s\n" % s )

    from subprocess import call
    call(["open","c_output.txt"])        


    
