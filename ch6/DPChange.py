# global 
INF = 999999
def DPChange(money, coins): 
    '''
    Dynamic Programming Change. 
    Problem: how can a cashier make change using the fewest number of coins?
    
    CODE CHALLENGE: Solve the Change Problem.
    Input: An integer money and an array coins = (coin1, ..., coind).
    Output: The minimum number of coins with denominations coins that changes money.
    
    Sample Input:
    40 (money)
    50,25,20,10,5,1 (coins)
    
    Sample Output:
    2    
    ===
    Algorithm: (concerpt of dynamic programming) 
    DPCHANGE(money, coins)
     MinNumCoins(0) <- 0
     for m <- 1 to money
            MinNumCoins(m) <- infinity
            for i <- 1 to |coins|
                if m >= coini
                    if MinNumCoins(m - coini) + 1 < MinNumCoins(m)
                        MinNumCoins(m) <- MinNumCoins(m - coini) + 1
        output MinNumCoins(money)
    ===
    MinNumCoins(m) = min{MinNumCoins(m - 6) + 1,MinNumCoins(m - 5) + 1, MinNumCoins(m - 1) + 1}
    '''
    #MinNumCoins(0,coins) =0 
    MinNumCoins_dic = {0:0}
    
    for m in range(1,money+1):
        MinNumCoins_dic[m] = INF
        for i in range(len(coins)):
            if m >= coins[i]:
                if MinNumCoins_dic[m - coins[i]] + 1 < MinNumCoins_dic[m]:
                    MinNumCoins_dic[m] = MinNumCoins_dic[m-coins[i]] + 1
    return MinNumCoins_dic[money]

if __name__ == "__main__":
    # read file and get parameters
    fin = open('dpc_input.txt','r')
    money = int(fin.readline().rstrip('\n') )
    coins = [int(a) for a in fin.readline().rstrip('\n').split(',')]
    fin.close()
    # run the function 
    output = DPChange(money,coins)
    
    # output the results
    with  open('dpc_output.txt','w') as fout:
        fout.write ("%s\n" % str(output) )

    from subprocess import call
    call(["open","dpc_output.txt"])        

