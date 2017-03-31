###_Algorithm Analysis_###

# We are calculating the maximal length of valid parenthesis
# by matching closing parenthesis with opening parenthesis.

# We are utilizing a stack. This stack holds the indexes of parentheses.
# The first index indicates where the current string of parentheses starts.
# If the first index is k and the last index is m, then the string currently
# in the stack is the string from k+1 to m (the first index is not in the string).

# The algorithm then is as follows:

# We iterate through the given string of parentheses:
# If we encounter an opening parenthesis, we push it on the stack.
# If we encounter a closing parenthesis, we do the following:
#    We check if the stack is empty:
#      -If not, we have found a valid substring. We check if it is the max found yet.
#      To do that, we need to find its length. The length of the current substring
#      is the difference between the current index and the last index in the stack
#      (since the valid string is between those two indexes).
#      If that is larger than the maximum length we have found previously, we update it.
#
#      -If the stack is empty, we push the current index on its top. The next (possible)
#      valid string begins after it.

# If we encounter a character other than '(' or ')', we return -1.

# The final value of maxLength is the solution.


###_Complexity Analysis_###

# Iterating over the given index: O(n), since we are making one linear pass.
# Pushing and popping are O(1).
# The rest are O(1) calculations.

# Thus the algorithm is O(n). ( because O(n)*O(1)*O(1) = O(n) )
# Since the algorithm is O(n) and for a solution we have to read the whole string,
# which takes O(n), the algorithm is optimal.


def FindLength(par):
    parLength = len(par);
    maxLength = 0;
    stack = [-1];
    
    for i in range(parLength):
        p = par[i];
        if(p == '('):
            #Add index to stack
            stack.append(i);
        elif(p == ')'):
            stack.pop(); #Pop top item
            stackLength = len(stack);
            if(stackLength > 0):
                #Stack is not empty, calculate maxLength
                lastIndex = stack[-1];
                if(i-lastIndex > maxLength):
                    maxLength = i-lastIndex;
            else:
                #Stack is empty, set it to current index
                stack = [i]
        else:
            #Encountered char other than parentheses
            return -1;

    return maxLength;


###_TESTING_###

par = "()(())";
print FindLength(par);
par = "(((()()))";
print FindLength(par);
