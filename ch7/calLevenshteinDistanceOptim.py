#from functools import lru_cache
#@lru_cache(maxsize=4095)
import sys
sys.setrecursionlimit(10000)
count = 0
def calLevenshteinDistanceDynamic(s, t):
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
    ====
    Use an 2d distance (len(s)+1 * len(t)+1) list to save the tmp results. 
    '''
    # init
    m,n = len(s),len(t)
    d = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m+1):
        d[i][0] = i 
    for j in range(n+1):
        d[0][j] = j

    for j in range(n):
        for i in range(m):
            if s[i] == t[j]:
                d[i+1][j+1] = d[i][j]
            else:
                d[i+1][j+1] = min(d[i][j+1]+1,# a deletion
                              d[i+1][j]+1,# an insertion
                              d[i][j]+1 # a substitution
                              )
    return d[-1][-1]
    
if __name__ == "__main__":
    # read file and get parameters
    with open('cld_input.txt','r') as fin:
        s = fin.readline().rstrip('\n') 
        t = fin.readline().rstrip('\n') 
    
    # run the function 
    distance = calLevenshteinDistanceDynamic(s,t)
    
    # output the results
    with  open('cld_output.txt','w') as fout:
        fout.write ("%d\n" % distance)

    from subprocess import call
    call(["open","cld_output.txt"])        

