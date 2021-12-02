#C(i) = min(j=1 to n){C(i-V[j])+1}

coins = [1,3,5]; #The list of available coins.
amount = 9;
    #The amount we want to make change for.
    #In the comments we will represent it with n.

coinReq = [0]*(amount+1);
    #The minimum amount of coins needed to make change for i.
    #The optimal solution for the problem will be stored in coinReq[n].
    #If for an amount j we cannot make change, then coinReq[j] = -1 at the end.
    #If in our coins we have a coin of value 1, then it is guaranteed that
    #we can make change for any amount.

aCoins = [0]*len(coins); #additionalCoins.
    #These are the coins we can add to our current amount.
    #If aCoins[i] = -1 then we cannot add coins[i] to our current amount.

for i in range(1,amount+1):
    for j in range(len(coins)):
        #resetting aCoins for new amount
        aCoins[j] = -1;

    for j in range(len(coins)):
        #Checking if a coin can be added to a previous amount to make change
        #for the current amount, aka coins[j] is smaller than current amount (i)
        #If no coin can be added, then aCoins[j] will equal -1.
        if(coins[j] <= i):
            aCoins[j] = coinReq[i-coins[j]] + 1;

    coinReq[i] = -1;
        #If we cannot make change for this amount, it will remain -1 in the end.
        #Else, it will be given a value in the next loop.

    for j in range(0,len(coins)):
        if(aCoins[j] > 0 and (coinReq[i] == -1 or coinReq[i] > aCoins[j])):
            #Either coinReq[i] hasn't been calculated before (= -1)
            #or our new aCoins value is smaller than coinReq[i]
            #and thus shall replace it.
            #If aCoins[j] <= 0, then no such coin can be added,
            #as it is larger than the amount (i).
            coinReq[i] = aCoins[j];

print coinReq[amount];
