#Let our two sequences be A,B and i,j their indexes, starting from the end.
#The recursive function to find longest common subsequence is the following:
#LS(A[i],B[j]) = 0, if i=0 or j=0
#LS(A[i],B[j]) = 1 + LS(A[i-1],B[j-1]), if A[i]=B[j]
#LS(A[i],B[j]) = max(LS(A[i-1],B[j]), LS(A[i],B[j-1])), otherwise


def FindSubsequence(s1,s2):
    l1 = len(s1) - 1;
    l2 = len(s2) - 1;

    if(l1 < 0 or l2 < 0):
        #One of our strings ended
        return 0;

    if(s1[l1] == s2[l2]):
        #The last char of the strings is the same.
        #We will remove it from the strings and try again.
        #Because, though, we found a common char, we add 1 to our solution.
        solutions[l1][l2] = 1 + FindSubsequence(s1[:l1],s2[:l2]);
    else:
        #The last chars of the strings are different.
        t1 = FindSubsequence(s1[:l1],s2); #remove char1, try again
        t2 = FindSubsequence(s1,s2[:l2]); #remove char2, try again

        #We pick the best of the two
        if(t1 > t2):
            solutions[l1][l2] = t1;
        else:
            solutions[l1][l2] = t2;

    return solutions[l1][l2];


S1 = ['a','c','b','a','e','d'];
S2 = ['a','b','c','a','d','f'];

#Our solutions will be stored here.
#The last integer in the matrix will be our final answer.
solutions = [[-1 for y in range(len(S2))] for x in range(len(S1))];

FindSubsequence(S1,S2);
print solutions[len(S1)-1][len(S2)-1];
