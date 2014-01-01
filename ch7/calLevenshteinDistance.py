#from functools import lru_cache
#@lru_cache(maxsize=4095)
import sys
sys.setrecursionlimit(10000)
count = 0
def calLevenshteinDistance(s, t):
    '''
    Edit Distance Problem: Find the edit distance between two strings.
    Input: Two strings.
    Output: The edit distance between these strings.
    
    CODE CHALLENGE: Solve the Edit Distance Problem.
    
    Sample Input:
    PLEASANTLY
    MEANLY
    
    Sample Output:
    5


    In 1966, Vladimir Levenshtein introduced the notion of the edit
    distance between two strings as the *minimum number* of edit
    operations needed to transform one string into another.

    Here, an edit operation is the insertion, deletion, or substitution
    of a single symbol. For example, TGCATAT can be transformed into
    ATCCGAT with five edit operations, implying that the edit distance
    between these strings is at most 5.  

    ref: http://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm
    ---- Dynamical programming 
    http://rosettacode.org/wiki/Levenshtein_distance#Python
    '''
    # count
    global count
    count +=1
    print count
    
    # empty str handle
    if not s: return len(t)
    if not t: return len(s)

    # no operation 
    if s[0]==t[0]:
        return calLevenshteinDistance(s[1:],t[1:])

    # choose the minimal edit operation backwards
    l_del = calLevenshteinDistance(s[1:],t)
    l_ins = calLevenshteinDistance(s,t[1:])
    l_subs = calLevenshteinDistance(s[1:],t[1:])

    return 1 + min(l_del,l_ins,l_subs)
    
if __name__ == "__main__":
    # read file and get parameters
    with open('cld_input.txt','r') as fin:
        s = fin.readline().rstrip('\n') 
        t = fin.readline().rstrip('\n') 
    
    # run the function 
    distance = calLevenshteinDistance(s,t)
    
    # output the results
    with  open('cld_output.txt','w') as fout:
        fout.write ("%d\n" % distance)

    from subprocess import call
    call(["open","cld_output.txt"])        

