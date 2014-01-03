import globalAlign as ga

def fittingAlignment(v,w):
    '''
    Fitting Alignment Problem: Construct a highest-scoring fitting
    alignment between two strings. 
    
    Input: Two nucleotide strings v and w, where v has length at most
    1000 and w has length at most 100. 
    
    Output: A highest-scoring fitting alignment between v and w. Use the
    simple scoring method in which matches count +1 and both the
    mismatch and indel penalties are 1. 


    Sample Input:
    GTAGGCTTAAGGTTA
    TAGATA
    
    Sample Output:
    2
    TAGGCTTA
    TAGA--TA

    "Fitting" w to v requires finding a substring v' of v that
    maximizes an alignment score the global alignment score between v'
    and w among all substrings of v. For example, the best global,
    local, and fitting alignments of v = GTAGGCTTAAGGTTA and w = TAGATA
    are shown below (with mismatch and indel penalties equal to 1). 

    Note that the optimal local alignment is not a valid fitting
    alignment. On the other hand, the score of the optimal global
    alignment (-3) is smaller than that of the best fitting alignment
    (+2). 
    '''
    v_subs = getSubstring(v,w)
    sigma = 1
    #results = map(lambda v_sub: ga.globalAlign(w,v_sub,sigma),v_subs)
    best_score, best_align  = -555, []
    for idx, v_sub in enumerate(v_subs):
        if idx % 100 == 0:
            print str(idx) + '/' + str(len(v_subs))
        align_tmp, score_tmp = ga.globalAlign(v_sub,w,sigma)
        if score_tmp > best_score:
            best_score = score_tmp
            best_align = align_tmp

    return best_align, best_score

# all substrings:
# http://stackoverflow.com/questions/127704/algorithm-to-return-all-combinations-of-k-elements-from-n
# Thanks to Claudiu, recursive solution
def subStringLen(str, length):
    return [str[i:i+length] for i in range(len(str)-length+1)]


def getSubstring(v,w):
    output = []
    for i in range(len(w),int(1.5*len(w))+1):
        output += subStringLen(v,i) 
    return list(set(output))
     
    
if __name__ == "__main__":
    # read file and get parameters
    with open('fa_input.txt','r') as fin:
        v = fin.readline().rstrip('\n') 
        w = fin.readline().rstrip('\n') 
    
    # run the function 
    align, score = fittingAlignment(v,w)
    
    # output the results
    with  open('fa_output.txt','w') as fout:
        fout.write("%d\n" % score)
        fout.write ("%s\n" % align[0])
        fout.write ("%s\n" % align[1])

    from subprocess import call
    call(["open","fa_output.txt"])        

