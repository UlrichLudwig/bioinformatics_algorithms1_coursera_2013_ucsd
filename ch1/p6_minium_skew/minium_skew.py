# read the genome
fin = open('input.txt')
genome = fin.readline().rstrip('\n')
fin.close()

# calculate the skew(ind):
skew_till_now = 0 
skew_ind = [0]
skew_dic ={'C':-1,'G':1,'A':0,'T':0}
for i in genome:
    skew_till_now += skew_dic[i]
    skew_ind.append(skew_till_now)

min_ind = min(skew_ind)    
print [i for i,v in enumerate(skew_ind) if v == min_ind]




