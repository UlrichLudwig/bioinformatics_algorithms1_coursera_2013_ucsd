import sys
for line in open(sys.argv[1]):
    input_str = line.rstrip('\n')

# DNA dictionary
DNA_dic = {'A':'T','G':'C','T':'A','C':'G'}

revese_complement_str =''.join([DNA_dic[s] for s in input_str[::-1]])

print revese_complement_str

