#fin = open(sys.argv[1]):
fin = open('input.txt')
genome = fin.readline().rstrip('\n')
pars = [int(i) for i in fin.readline().split()]
k = pars[0]
L = pars[1]
t = pars[2]
fin.close()

import frequent_words
out = []
for i in range(len(genome)-L+1):
    out += (frequent_words.frequent_word(genome[i:i+L],k,t))
output = set(out)

with  open('output.txt','w') as fout:
    for i in output:
        fout.write ("%s " % i )

from subprocess import call
call(["open","output.txt"])        
