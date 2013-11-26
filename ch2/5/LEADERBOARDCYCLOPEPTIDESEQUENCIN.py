
#import urllib
#urllib.urlretrieve ("https://beta.stepic.org/media/attachments/lessons/98/integer_mass_table.txt", "integer_mass_table.txt")
# modified the integer_mass_table to combine IL and KQ together. 
# now 18 keys:values in the dic
with open("integer_mass_table2.txt","r") as f:
    peptide_spetrum_dic2 = {line.split()[0]:int(line.split()[1]) for line in f}

spectrum_list =  peptide_spetrum_dic2.values()

# read the input RNA pattern
fin =  open('input.txt')
N = int(fin.readline().rstrip('\n'))
spectrum = [[int(v) for v in line.split()] for line in fin][0]
fin.close()

# lib 
from Cyclospectrum import Cyclospectrum

# score function 
def Score(peptides,spectrum):
    calculate = Cyclospectrum.Cyclospectrum(peptides)
    count = 0
    for i in spectrum:
        if i in calculate:
            count+=1
    return count 
    

def LeaderboardCyclopeptideSequencing(spectrum,N):
    leaderboard =[[]] # hold the best score peptides
    leaderPeptide = []

    tmp_list = spectrum_list
    output_list = [[]]
    while len(tmp_list) !=0:
        tmp_list = expand(output_list,spectrum_list,spectrum)
        if len(tmp_list) !=0:
            output_list = list(tmp_list)
            
    return [val_list for val_list in output_list if CyclospectrumVal(val_list) == spectrum]


# subroutine: expandkey is the expand. 


def expand(output_list,spectrum_list,spectrum):
    '''Input/output: output_list: 2d list, each item is a val seq match the spectrum'''

    output =[]
    for val1 in output_list:
        for val2 in spectrum_list:
            if sum(val1)+val2 in spectrum:# and val2 not in val1:
                # add val2 into list(val1)
                tmp = list(val1)
                tmp.append(val2)
                output.append(tmp)
    return output

result = cyclopeptideSequencing(spectrum,spectrum_list)

#print output

# output
format_str= "%d-" * (len(result[0])-1)+"%d "
with  open('output.txt','w') as fout:
    for i in result:
            fout.write (format_str % tuple(i))

from subprocess import call
call(["open","output.txt"])        
        
