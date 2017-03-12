import math;


class Heap:
    def __init__(self,array=[]):
        self.heap = array;


    ###BASICS###
    def IsEmpty(self):
        return len(self.heap) == 0;

    def ExtractMin(self):
        self.Delete(self.heap[0]);

    def HeapList(self):
        return self.heap;


    ###SEARCH###
    def Search(self,key):
        return self.SearchHeap(key,0);

    def SearchHeap(self,key,index):
        if(index >= len(self.heap)):
            #index is out of range
            return -1;

        if(self.heap[index] == key):
            #Found key
            return index;

        #The left child is at position = 2*index+1
        #The right child is at position = 2*index+2
        l = self.SearchHeap(key,2*index+1); #Search in the left subtree
        r = self.SearchHeap(key,2*index+2); #Search in the right subtree

        #Return the biggest of the above results.
        #-1 means we haven't found the element.
        #So, if l is bigger, we found the element at l.
        #Otherwise, the element isn't at l.
        #We return r. If r > -1, the element is at r. Otherwise, we haven't
        #found the element.
        if(l > r):
            return l;
        else:
            return r;


    ###HEIGHT-WIDTH-WEIGHT###
    def Height(self):
        #The number of nodes in a complete tree are given by the following
        #formula:
        #n=2^(h-1), where h is the height of the tree. So, the height of the
        #tree is given by: h = log(n,2). We round this up to get the solution.
        n = len(self.heap); #The number of nodes in the heap
        return int(math.floor(math.log(n,2)))+1; #h = log(n,2)+1

    def Width(self):
        index = 0; #Start from the root
        length = len(self.heap); #The length of the heap list
        width = 0;

        #Here we do not need to go from parent to children. We can iterate
        #through the list one-by-one, without concern about the order.
        #We add the iterated element's number of digits to width and we move on.
        while(index < length):
            #Add the number of digits of the element to width
            width += len(str(self.heap[index]));
            index += 1; #Move to the next element in the list

        return width;

    def NodeWeight(self,key):
        index = self.Search(key); #key is placed at index
        length = len(self.heap); #The length of the heap list

        return self.FindNodeWeight(index,length); #Find the weight of node

    def FindNodeWeight(self,index,length):
        lChild = 2*index+1; #The left child
        rChild = 2*index+2; #The right child

        if(lChild >= length):
            #Node at index has no left child, return 1 (for the node itself)
            return 1;

        l = self.FindNodeWeight(lChild,length); #Find the weight of left child
        #For now we assume there is no right child. So, the weight of the
        #right subtree is initially set as 0. If the right child exists, we
        #will update the weight,
        r = 0;

        if(rChild < length):
            #Right child exists, find its weight
            r = self.FindNodeWeight(rChild,length);

        return l+r+1; #Return the weight of the subtrees plus one for the node
        


    ###PRINT###
    def PrintHeap(self):
        if(self.IsEmpty()):
            print "The heap is empty";
            return;

        w = self.Width(); #Heap's width
        h = self.Height(); #Heap's height
        l = len(self.heap); #Number of nodes in heap

        #The array to get printed. Empty places are represented by spaces.
        #The array is wxh.
        pArray = [[' ' for i in range(h)] for j in range(w)];

        #We beginning building pArray from the top left element (0,0)
        self.PrintHeapRecursively(0,0,0,pArray,l);

        #Print pArray, by concatating the nodes in pArray to p line-by-line
        p = "";
        for i in range(h):
            for j in range(w):
                p += pArray[j][i];

            print p;
            p = "";

    def PrintHeapRecursively(self,index,x,y,pArray,length):
        #x : width index
        #y : height index

        if(index < length):
            #Children should be inserted in the array one level below (y+1)

            #We insert elements in this order:
            #a) Left Child (2*index+1)
            #b) Current Node (index)
            #c) Right Child (2*index+2)
            
            #Every time we insert a node, we need to move x.
            #That's why each functions returns a new x.
            x = self.PrintHeapRecursively(2*index+1,x,y+1,pArray,length);
            x = self.PassToArray(index,x,y,pArray); #Insert key to pArray
            x = self.PrintHeapRecursively(2*index+2,x,y+1,pArray,length);

        return x;

    def PassToArray(self,index,x,y,pArray):
        #We pass the digits of the key to pArray one-by-one
        temp = str(self.heap[index]);
        for i in range(len(temp)):
            pArray[x+i][y] = temp[i];

        #Move x to the right by the number of digits in key
        x += len(temp);
        return x;
        
            
class MinHeap(Heap):
    def Min(self):
        return self.heap[0]; #The first element of the heap is the min

    ###INSERT-DELETE###
    def Insert(self,key):
        #Add key to the end of the list
        self.heap.append(key);
        #The position of the inserted element
        index = len(self.heap)-1;

        while(index > 0):
            curr = self.heap[index]; #The element at position = index
            #Parent is at position = floor(index/2)
            pIndex = int(math.floor(index/2)); #The index of curr's parent
            parent = self.heap[pIndex]; #curr's parent
            
            if(curr < parent):
                #curr is less than its parent, the two should be swapped
                self.heap[pIndex] = curr; #curr goes at its parent's position
                self.heap[index] = parent; #parent goes at curr's position
                index = pIndex; #Now the inserted element moves to pIndex
            else:
                #The inserted element got placed in the correct position
                break;

    def Delete(self,key):
        index = self.Search(key); #The position of key
        lIndex = len(self.heap)-1; #The position of last element in heap

        if(index == lIndex):
            #Element is at the end of the list, remove it
            del self.heap[lIndex];
            return;

        #Place the last element of the heap in the deleted key's position
        self.heap[index] = self.heap[lIndex];
        del self.heap[lIndex];

        #Move the last element (now at index) down until heap order is restored
        lElement = self.heap[index]; #The last element
        cIndex1 = 2*index+1; #The left child of last element
        cIndex2 = 2*index+2; #The right child of last element
        length = len(self.heap); #The length of the heap
        
        while(True):
            if(cIndex1 >= length):
                #Last element has no children
                return;

            c1 = self.heap[cIndex1]; #The left child
            #We assume that there is no right child. In this case, we will
            #put in c2 a value greater than c1 (the left child).
            #That way, the last element will get replaced by its left, and only,
            #child. If the right child exists, we will update c2.
            c2 = c1+1;

            if(cIndex2 < length):
                #The right child exists, update c2
                c2 = self.heap[cIndex2];

            if(c1 < c2):
                #The left child is the lesser child, compare it with lElement
                if(c1 < lElement):
                    #The left child is lesser, swap it with the last element
                    #and update index
                    self.heap[index] = c1;
                    self.heap[cIndex1] = lElement;
                    index = cIndex1;
                else:
                    #Last element got placed in the correct position
                    return;
            else:
                #The right child is the lesser child, compare it with lElement
                if(c2 < lElement):
                    #The right child is lesser, swap it with the last element
                    #and update index
                    self.heap[index] = c2;
                    self.heap[cIndex2] = lElement;
                    index = cIndex2;
                else:
                    #Last element got placed in the correct position
                    return;

            #The new children's indices
            cIndex1 = 2*index+1;
            cIndex2 = 2*index+2;


class MaxHeap(Heap):
    def Max(self):
        return self.heap[0]; #The first element of the heap is the max

    ###INSERT-DELETE###
    def Insert(self,key):
        #Add key to the end of the list
        self.heap.append(key);
        #The position of the inserted element
        index = len(self.heap)-1;

        while(index > 0):
            curr = self.heap[index]; #The element at position = index
            #Parent is at position = floor(index/2)
            pIndex = int(math.floor(index/2)); #The index of curr's parent
            parent = self.heap[pIndex]; #curr's parent
            
            if(curr > parent):
                #curr is greater than its parent, the two should be swapped
                self.heap[pIndex] = curr; #curr goes at its parent's position
                self.heap[index] = parent; #parent goes at curr's position
                index = pIndex; #Now the inserted element moves to pIndex
            else:
                #The inserted element got placed in the correct position
                break;

    def Delete(self,key):
        index = self.Search(key); #The position of key
        lIndex = len(self.heap)-1; #The position of last element in heap

        if(index == lIndex):
            #Element is at the end of the list, remove it
            del self.heap[lIndex];
            return;

        #Place the last element of the heap in the deleted key's position
        self.heap[index] = self.heap[lIndex];
        del self.heap[lIndex];

        #Move the last element (now at index) down until heap order is restored
        lElement = self.heap[index]; #The last element
        cIndex1 = 2*index+1; #The left child of last element
        cIndex2 = 2*index+2; #The right child of last element
        length = len(self.heap); #The length of the heap
        
        while(True):
            if(cIndex1 >= length):
                #Last element has no children
                return;

            c1 = self.heap[cIndex1]; #The left child
            #We assume that there is no right child. In this case, we will
            #set c2 as a value less than c1 (the left child).
            #That way, the last element will get replaced by its left, and only,
            #child. If the right child exists, we will update c2.
            c2 = c1-1;

            if(cIndex2 < length):
                #The right child exists, update c2
                c2 = self.heap[cIndex2];

            if(c1 > c2):
                #The left child is the greater child, compare it with lElement
                if(c1 > lElement):
                    #The left child is greater, swap it with the last element
                    #and update index
                    self.heap[index] = c1;
                    self.heap[cIndex1] = lElement;
                    index = cIndex1;
                else:
                    #Last element got placed in the correct position
                    return;
            else:
                #The right child is the greater child, compare it with lElement
                if(c2 > lElement):
                    #The right child is greater, swap it with the last element
                    #and update index
                    self.heap[index] = c2;
                    self.heap[cIndex2] = lElement;
                    index = cIndex2;
                else:
                    #Last element got placed in the correct position
                    return;

            #The new children's indices
            cIndex1 = 2*index+1;
            cIndex2 = 2*index+2;
