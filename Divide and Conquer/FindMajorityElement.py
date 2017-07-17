def FindMajorityElement(a):
    l = len(a);

    if(l == 2):
        #If a has just two elements, we just need to compare the two.
        if(a[0] == a[1]):
            #They are the same, so they are the majority element of a.
            #That is because they appear more than l/2 times.
            #Return them.
            return a[0];
        else:
            #They aren't the same, so a doesn't have a majority element
            #Return -1. We treat -1 as a non-element.
            return -1;

    #Find the majority elements (if they exist) of the two halves.
    element1 = FindMajorityElement(a[:l/2]); #First half
    element2 = FindMajorityElement(a[l/2:]); #Second half

    #Compare the two to see if we have a majority element

    #If only one of them is a non-element, then the other is a majority element.
    #Return it.    
    if(element1 == -1 and element2 >= 0):
        return element2;
    elif(element2 == -1 and element1 >= 0):
        return element1;

    if(element1 == element2):
        #If they are the same, then they are the majority element of a.
        #Return them.
        return element1;
    else:
        #They aren't the same, so a doesn't have a majority element
        #Return -1. We treat -1 as a non-element.
        return -1;
            
A = [1, 3, 1, 3, 1, 1, 3, 1]; #Our array
print FindMajorityElement(A);
