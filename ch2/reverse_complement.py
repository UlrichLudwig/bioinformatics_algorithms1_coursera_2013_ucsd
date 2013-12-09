def reverse_complement(input_str):
    # DNA dictionary
    DNA_dic = {'A':'T','G':'C','T':'A','C':'G'}
    revese_complement_str =''.join([DNA_dic[s] for s in input_str[::-1]])
    return revese_complement_str

