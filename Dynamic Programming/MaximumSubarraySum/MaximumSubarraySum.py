#Sum(i) = Max{ Sum(i-1) + S[i], S[i] }

#For a number S[i], we want to decide if it is better to pick it alone,
#or pick the sum that came before that (plus the number S[i]).
#We check which is greater and go with that.
#Essentially, if the previous sum is negative, we pick S[i].
#Else, we pick them both.

def CalculateSubarraySum(n):
    for i in range(1, n+1):
        if(sums[i-1] + S[i-1] > S[i-1]):
            #We pick the previous sum, plus S[i]
            sums[i] = sums[i-1] + S[i-1];
        else:
            #We pick S[i]
            sums[i] = S[i-1];

    return max(sums);


S = [-2, 1, -3, 7, -2, 3, 1, -5, 4];
n = len(S);

sums = [0 for x in range(n+1)];

print CalculateSubarraySum(n);
