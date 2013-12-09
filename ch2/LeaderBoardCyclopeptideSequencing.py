# lib 
from Cyclospectrum import CyclospectrumVal
from CylopeptideSequencing import expand

# globle:
with open("integer_mass_table2.txt","r") as f:
    peptide_spetrum_dic2 = {line.split()[0]:int(line.split()[1]) for line in f}
    
spectrum_list =  peptide_spetrum_dic2.values()


# score function 
def score(peptides,spectrum):
    '''
    Select the peptide whose theoretical spectrum matches the given experimental spectrum the most closely
    
    eg:
    Spectrum = {0, _99_, 113, 114, 128, 227, 257, _299_, 355, 356, 370, 371, 484}
    Score(NQEL, Spectrum) = 11
    '''
    calculate = CyclospectrumVal(peptides)
    count = 0
    for i in spectrum:
        if i in calculate:
            count+=1
    return count 

def cut(leaderboard,spectrum,N):
    '''
    Returns the top N highest-scoring peptides in Leaderboard (including ties) with respect to Spectrum (output could be more than N)
    '''
    score_list = [score(peptide,spectrum) for peptide in leaderboard]

    score_unique = list(set(score_list))
    score_unique.sort()
    output =[[]]
    for i in range(len(score_list)):
        if score_list[i] in score_unique[:N]:
            output.append(leaderboard[i])
    return output
    
def LeaderboardCyclopeptideSequencing(spectrum,N):
    '''
    Input: Integer N and a collection of integers Spectrum.
    Output: LeaderPeptide after running LEADERBOARDCYCLOPEPTIDESEQUENCING(Spectrum, N). 
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    Sample Input:
    10
    0 71 113 129 147 200 218 260 313 331 347 389 460
    
    Sample Output:
    113-147-71-129
    
    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
     LEADERBOARDCYCLOPEPTIDESEQUENCING(Spectrum, N)
        Leaderboard <- {0-peptide}
        LeaderPeptide <- 0-peptide
        while Leaderboard is non-empty
            Leaderboard <- Expand(Leaderboard)
            for each Peptide in Leaderboard
                if Mass(Peptide) = ParentMass(Spectrum)
                    if Score(Peptide, Spectrum) > Score(LeaderPeptide, Spectrum)
                        LeaderPeptide <- Peptide
                else if Mass(Peptide) > ParentMass(Spectrum)
                    remove Peptide from Leaderboard
            Leaderboard = cut(Leaderboard, Spectrum, N)
        output LeaderPeptide
    '''
    leaderboard =[[]] # hold the best score peptides
    leader_peptide = []

    while len(leaderboard)!=0:
        leaderboard = expand1(leaderboard,spectrum_list,spectrum)
        tmp = leaderboard[:]
        for peptide in tmp:
            if sum(peptide) == spectrum[-1]:
                if score(peptide,spectrum) > score(leader_peptide,spectrum):
                    leader_peptide = peptide
            elif sum(peptide) > spectrum[-1]:
                tmp.remove(peptide)
        tmp = cut(leaderboard,spectrum,N)

        print len(leaderboard)

    return leader_peptide

if __name__ == "__main__":
        
    # read the input RNA pattern
    fin =  open('lbcs_input.txt')
    N = int(fin.readline().rstrip('\n'))
    spectrum = [[int(v) for v in line.split()] for line in fin][0]
    fin.close()
        
    #print output
    result = LeaderboardCyclopeptideSequencing(spectrum,N)
    # output
    format_str= "%d-" * (len(result)-1)+"%d "
    with  open('lbcs_output.txt','w') as fout:
        fout.write (format_str % tuple(result))
            
    from subprocess import call
    call(["open","lbcs_output.txt"])        
        
