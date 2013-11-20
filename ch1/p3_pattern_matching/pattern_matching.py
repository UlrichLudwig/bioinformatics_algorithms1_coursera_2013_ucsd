#fin = open(sys.argv[1]):
fin = open('input.txt')
pattern = fin.readline().rstrip('\n')
genome = fin.readline().rstrip('\n')

fin.close()

# function patternFind
def patternFind(pattern,genome):
    index_list = []
    kmer = len(pattern)
    for i in range(len(genome)-kmer+1):
        if pattern == genome[i:i+kmer]:
            index_list.append(i)

    return index_list

index_list = patternFind(pattern,genome)

with  open('output.txt','w') as fout:
    for i in index_list:
        fout.write ("%d " % i )
