'''
The theoretical spectrum of a cyclic peptide Peptide, denoted Cyclospectrum(Peptide), is the collection of all of the masses of its subpeptides, in addition to the mass 0 and the mass of the entire peptide. Note that the theoretical spectrum may contain duplicate elements, as is the case for NQEL (shown below), where NQ and EL have the same mass.

0	113	114	128	129	227	242	242	257	355	356	370	371	484
L	N	Q	E	LN	NQ	EL	QE	LNQ	ELN	QEL	NQE	NQEL

Generating Theoretical Spectrum Problem: Generate the theoretical spectrum of a cyclic peptide.
     Input: An amino acid string Peptide.
     Output: Cyclospectrum(Peptide).

CODE CHALLENGE: Solve the Generating Theoretical Spectrum Problem.

Sample Input:
     LEQN

Sample Output:
     0 113 114 128 129 227 242 242 257 355 356 370 371 484
'''
with open("integer_mass_table.txt","r") as f:
    peptide_spectrum_dic = {line.split()[0]:int(line.split()[1]) for line in f}

def Cyclospectrum(peptide_str):

    def subStringLen(str, length):
        str += str
        return [str[i:i+length] for i in range(len(str)/2)]

    peptide_str_all=[]
    for i in range(1,len(peptide_str)):
        peptide_str_all += subStringLen(peptide_str,i) 
        
    peptide_str_all.append(peptide_str)

    # str to spectrum
    result =  [sum([peptide_spectrum_dic[i] for i in str]) for str in peptide_str_all]
    result.append(0)
    result.sort()
    return result

def CyclospectrumVal(val_list):
    peptide = valToPeptide(val_list)
    return Cyclospectrum(peptide)

def valToPeptide(val_list):
    result = ''
    for val in val_list:
        result+=peptide_spectrum_dic.keys()[peptide_spectrum_dic.values().index(val)] 
    return result
