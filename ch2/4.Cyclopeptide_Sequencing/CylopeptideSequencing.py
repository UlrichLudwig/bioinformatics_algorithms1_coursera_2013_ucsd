'''
CODE CHALLENGE: Implement CYCLOPEPTIDESEQUENCING (pseudocode reproduced below).

Note: After the failure of the first brute-force algorithm we considered, you may be hesitant to implement this algorithm for fear that its runtime will be prohibitive. The potential problem with CYCLOPEPTIDESEQUENCING is that it may generate incorrect k-mers at intermediate stages (i.e., k-mers that are not subpeptides of a correct solution). You may wish to wait to implement CYCLOPEPTIDESEQUENCING until after the next section, where we will analyze this algorithm.

    CYCLOPEPTIDESEQUENCING(Spectrum)
        List ← {0-peptide}
        while List is nonempty
            List ← Expand(List)
            for each peptide Peptide in List
                if Cyclospectrum(Peptide) = Spectrum
                    output Peptide
                    remove Peptide from List
                else if Peptide is not consistent with Spectrum
                    remove Peptide from List

Sample Input:
     0 113 128 186 241 299 314 427

Sample Output:
     186-128-113 186-113-128 128-186-113 128-113-186 113-186-128 113-128-186
'''

#import urllib
#urllib.urlretrieve ("https://beta.stepic.org/media/attachments/lessons/98/integer_mass_table.txt", "integer_mass_table.txt")
# modified the integer_mass_table to combine IL and KQ together. 
# now 18 keys:values in the dic
with open("integer_mass_table2.txt","r") as f:
    peptide_spetrum_dic2 = {line.split()[0]:int(line.split()[1]) for line in f}

spectrum_list =  peptide_spetrum_dic2.values()

# read the input RNA pattern
with open('input.txt') as fin:
    spectrum = [[int(v) for v in line.split()] for line in fin][0]

# main function
from Cyclospectrum import CyclospectrumVal

def cyclopeptideSequencing(spectrum,spectrum_list):
    '''Input spectrum, and given the peptide:val dic
    Output: the possible peptides combinations in terms of the value
    '''
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
        
