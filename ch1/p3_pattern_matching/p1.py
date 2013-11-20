
    # divide the string get a kmers string list
def devide_str(input_str,kmer):
    output = []
    for i in range(len(input_str)-kmer):
        output.append(input_str[i:i+kmer])
    return output

def find_kmer(input_str,kmer):
    '''Input a string, kmer_length. find the most frequent kmer sub_string'''
    kmer_list = devide_str(input_str,kmer)
    kmer_set = set(kmer_list)
    kmer_count = {x: kmer_list.count(x) for x in kmer_set}
    return kmer_count
        
