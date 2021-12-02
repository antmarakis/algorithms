#N(n) = min(1<i<sqrt(n)){N(n-i^2)+1}

import math;
import sys;


def FindSum(n):
    if(solutions[n] > 0):
        #We have already calculated the solution for this number.
        #Return said solution.
        return solutions[n];

    if(n == 0):
        #For 0, we return 0
        return 0;

    #The square root of n, floored and converted to an integer.
    #This will be the upper bound of the values we can add to get n.
    #If a value is larger than x, then x^2 will be larger than n.
    x = int(math.floor(math.sqrt(n)));

    #Find minimum of possible solutions
    m = sys.maxint;
    for i in range(1,x+1):
        s = i*i; #The square to be added
        #From the number n-s, we need one move to reach n,
        #as we just need to add s.
        #So, we must calculate the solution for n-s and add one to it.
        temp = FindSum(n-s) + 1;

        if(temp < m):
            #Found new min
            m = temp;
        
    solutions[n] = m; #Found the solution for n
    return solutions[n]; #Return solution for n


number = 13;
solutions = [0 for y in range(number+1)]; #Our table of subset solutions

print FindSum(number);
