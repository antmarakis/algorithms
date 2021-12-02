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
