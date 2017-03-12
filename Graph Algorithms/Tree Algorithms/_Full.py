import math;


class TreeNode:
    def __init__(self,key,parent=None):
        self.key = key;
        
        self.leftChild = None;
        self.rightChild = None;
        self.parent = parent;

        self.deleted = False;
        self.keyLength = len(str(self.key)); #The number of digits in key


class BinarySearchTree:
    def __init__(self,d=-1):
        self.root = None;
        self.nodesIndex = 0; #How many nodes in total
        self.deletedIndex = 0; #How many nodes are deleted
        #The amount of marked for deletion nodes to accept before rearranging.
        #If it is -1, we will not mark nodes for deletion, but delete them.
        self.deletedBound = d;
        #The direction we will go for deleting a node. True:left, False:right
        #For left, we will replace curr with its predecessor.
        #For right, we will replace curr with its successor.
        self.nextDeletion = False;

    def IsEmpty(self):
        #Check whether the root exists or not
        return self.root is None;


    ###BASICS###
    def Search(self,k):
        curr = self.root; #Start from the root

        while(curr is not None):
            if(k < curr.key):
                #k is in the left subtree of curr
                curr = curr.leftChild;
            elif(k > curr.key):
                #k is in the right subtree of curr
                curr = curr.rightChild;
            else:
                if(curr.deleted):
                    #The node has been deleted
                    return False;
                else:
                    #The node was found
                    return True;

        #The node was not found
        return False;

    def Insert(self,k):
        curr = self.root; #Start from the root
        parent = None;

        while(curr is not None):
            #We are moving to a child of curr.
            #So, the current parent is curr.
            parent = curr;
            
            if(k < curr.key):
                #k is in the left subtree of curr
                curr = curr.leftChild;
            elif(k > curr.key):
                #k is in the right subtree of curr
                curr = curr.rightChild;
            else:
                #The node to insert already exists in the tree
                return;

        #Create new node, with its parent being parent
        newNode = TreeNode(k,parent);
        self.nodesIndex += 1; #A new node was added

        if(not self.IsEmpty()):
            #The tree is not empty
            if(k < parent.key):
                parent.leftChild = newNode;
            elif(k > parent.key):
                parent.rightChild = newNode;
        else:
            #The tree is empty
            #newNode is the root
            self.root = newNode;
            nodesIndex = 1; #There is only one node in the tree

    def Delete(self,k):
        curr = self.root; #Start from the root

        if(self.IsEmpty()):
            #Tree is empty, there is nothing to delete
            return;

        while(curr is not None and curr.key != k):
            if(k < curr.key):
                #k is in the left subtree of curr
                curr = curr.leftChild;
            elif(k > curr.key):
                #k is in the right subtree of curr
                curr = curr.rightChild;

            if(curr is None):
                #The node doesn't exist
                return;

        if(curr.leftChild is not None and curr.rightChild is not None):
            if(self.deletedBound >= 0):
                #Deletebound is greater than 0, so we go with this process:
                #If a node has two children, we do not delete it outright,
                #but we flag it as deleted to take care of later.
                curr.deleted = True;
                self.deletedIndex += 1;

                #The ration of deleted nodes over all nodes
                d = self.deletedIndex/float(self.nodesIndex);

                if(d > self.deletedBound):
                    #Too many nodes are flagged as deleted.
                    #We need to rearrange the tree to take care of them.
                    self.Rearrange();
            elif(self.nextDeletion):
                #Left deletion
                temp = curr.leftChild;
                predecessor = None;

                #Find predecessor of curr
                #Predecessor is the largest node in curr's left subtree.
                #It comes right before curr in the inorder traversal.
                #Predecessor will replace curr in the tree.
                while(temp is not None):
                    #To find the predecessor, we move from right child to
                    #right child in the left subtree.
                    predecessor = temp;
                    temp = temp.rightChild;

                if(predecessor.parent != curr):
                    #Predecessor isn't curr's left child.
                    #Replace predecessor with its left child
                    self.Transplant(predecessor,predecessor.leftChild);
                    #The left child of predecessor becomes the left child of the
                    #node to be deleted
                    predecessor.leftChild = curr.leftChild;
                    #Update the child's parent
                    predecessor.leftChild.parent = predecessor;

                #Replace curr with predecessor
                self.Transplant(curr,predecessor);
                #The right child of predecessor becomes the right child of the
                #node to be deleted
                predecessor.rightChild = curr.rightChild;
                #Update the child's parent
                predecessor.rightChild.parent = predecessor;
            else:
                #Right deletion
                temp = curr.rightChild;
                successor = None;

                #Find successor of curr
                #Successor is the smallest node in curr's right subtree.
                #It comes right after curr in the inorder traversal.
                #Successor will replace curr in the tree.
                while(temp is not None):
                    #To find the successor, we move from left child to
                    #left child in the right subtree.
                    successor = temp;
                    temp = temp.leftChild;

                if(successor.parent != curr):
                    #Successor isn't curr's right child.
                    #Replace successor with its right child
                    self.Transplant(successor,successor.rightChild);
                    #The right child of successor becomes the right child of the
                    #node to be deleted
                    successor.rightChild = curr.rightChild;
                    #Update the child's parent
                    successor.rightChild.parent = successor;

                #Replace curr with successor
                self.Transplant(curr,successor);
                #The left child of successor becomes the left child of the node
                #to be deleted
                successor.leftChild = curr.leftChild;
                #Update the child's parent
                successor.leftChild.parent = successor;

            #Reverse the deletion direction
            #If we went left, next we will go right and vise-versa
            self.nextDeletion = not self.nextDeletion;
            del curr; #Delete the node
            self.nodesIndex -= 1; #There is one less node, update nodesIndex
        else:
            if(curr.leftChild is not None):
                #curr has a left child.
                self.Transplant(curr,curr.leftChild); #Replace curr with child
            elif(curr.rightChild is not None):
                #curr has a right child.
                self.Transplant(curr,curr.rightChild); #Replace curr with child

            #Delete curr node, decrement nodesIndex
            del curr;
            self.nodesIndex -= 1;

    def Transplant(self,u,v):
        #This replaces one subtree with another.
        #u gets replaced by v under u's parent.
        if(u.parent is None):
            #u is root
            self.root = v;
        elif(u == u.parent.leftChild):
            #u is a left child.
            u.parent.leftChild = v;
        else:
            #u is a right child
            u.parent.rightChild = v;

        if(v is not None):
            #Update the parent of v.
            v.parent = u.parent;


    ###MIN-MAX###
    def FindMin(self):
        curr = self.root; #Start from the root
        minNode = None;

        while(curr is not None):
            #We go from left child to left child and we keep the latest key.
            #When there are no more left children, the final key is the min.
            minNode = curr.key;
            curr = curr.leftChild;

        return minNode; #If this is None, the tree is empty

    def FindMax(self):
        curr = self.root; #Start from the root
        maxNode = None;

        while(curr is not None):
            #We go from right child to right child and we keep the latest key.
            #When there are no more right children, the final key is the max.
            maxNode = curr.key;
            curr = curr.rightChild;

        return maxNode; #If this is None, the tree is empty


    ###TRAVERSAL###
    #Tree traversal call functions
    def InOrder(self):
        return self.ListInOrder(self.root,[]);

    def PreOrder(self):
        return self.ListPreOrder(self.root,[]);

    def PostOrder(self):
        return self.ListPostOrder(self.root,[]);

    #Tree traversal recursive functions
    def ListInOrder(self,curr,inList):
        if(curr):
            #In in-order traversal you print nodes in this order:
            #a) Left Child
            #b) Node
            #c) Right Child

            #In-Order for left child
            self.ListInOrder(curr.leftChild,inList);

            if(not curr.deleted):
                #curr is not deleted, added to list
                inList.append(curr.key);
            
            #In-Order for right child
            self.ListInOrder(curr.rightChild,inList);

        return inList;

    def ListPostOrder(self,curr,inList):
        if(curr):
            #In post-order traversal you print nodes in this order:
            #a) Left Child
            #b) Right Child
            #c) Node

            #Post-Order for left child
            self.ListPostOrder(curr.leftChild,inList);
            #Post-Order for right child
            self.ListPostOrder(curr.rightChild,inList);

            if(not curr.deleted):
                #curr is not deleted, added to list
                inList.append(curr.key);

        return inList;

    def ListPreOrder(self,curr,inList):
        if(curr):
            #In pre-order traversal you print nodes in this order:
            #a) Node
            #b) Left Child
            #c) Right Child
            
            if(not curr.deleted):
                #curr is not deleted, added to list
                inList.append(curr.key);

            #Pre-Order for left child
            self.ListPreOrder(curr.leftChild,inList);
            #Pre-Order for right child
            self.ListPreOrder(curr.rightChild,inList);

        return inList;

    def FindPath(self,k1,k2):
        #Find the path between k1 and k2#
        #A node's height is the node's distance from the root#
        #The two nodes might not be on the same level.
        #After we get them on the same level, we can keep moving up the path
        #from both of them until we reach their common ancestor.
        info1 = self.NodeHeight(k1);
        info2 = self.NodeHeight(k2);

        h1 = info1[0]; #The height of k1
        c1 = info1[1]; #The node with key = k1
        
        h2 = info2[0]; #The height of k1
        c2 = info2[1]; #The node with key = k2

        k = []; #The list to hold the keys in the path

        if(h1 == -1 or h2 == -1):
            #One of the nodes doesn't exist
            return;

        #We will move c1 and c2 to the same level
        while(h1 != h2):
            if(h1 > h2):
                #c1 is higher than c2
                #We will move up its path.
                k.append(c1.key); #Add c1 to the overall path

                #Move up c1's path. Now c1 is its parent and h1 is one less,
                #as c1 is closer to the root.
                c1 = c1.parent;
                h1 -= 1;
            else:
                #c2 is higher than c1
                #We will move up its path.
                k.append(c2.key);
                
                #Move up c2's path. Now c2 is its parent and h2 is one less,
                #as c2 is closer to the root.
                c2 = c2.parent;
                h2 -= 1;

        #We will ascend the respective paths towards the root until we reach
        #a common ancestor.
        #Because c1 and c2 are on the same level, they will simultaneously
        #reach the root (if they are on its different subtrees).
        while(c1.key != c2.key):
            #Add c1 and c2 keys to the overall path
            k.append(c1.key);
            k.append(c2.key);

            #Move up on both paths
            c1 = c1.parent;
            c2 = c2.parent;

        k.append(c1.key); #Add the key of their common ancestor
        return k; #Return the path from c1 to c2


    ###TREE DELETION###
    #Deletion call function
    def DeleteTree(self):
        self.DeleteTreeRecursively(self.root);

        #There are no nodes in the tree, reset indices and blank root.
        self.root = None;
        self.nodesIndex = 0;
        self.deletedIndex = 0;

    #Deletion recursive function
    def DeleteTreeRecursively(self,curr):
        if(curr is not None):
            #Delete left and right subtree of curr
            self.DeleteTreeRecursively(curr.leftChild);
            self.DeleteTreeRecursively(curr.rightChild);

            del curr; #Delete curr


    ###WIDTH-HEIGHT-WEIGHT###
    #Width call function
    def Width(self):
        #NOTE: This doesn't return the width in nodes but in digits (keyLength)
        return self.FindWidth(self.root);

    #Width recursive function
    def FindWidth(self,curr):
        if(curr is None):
            #Subtree is empty, width is 0
            return 0;
        
        lWidth = self.FindWidth(curr.leftChild); #Width of left subtree
        rWidth = self.FindWidth(curr.rightChild); #Width of right subtree

        #The width of a tree is the width of the left/right subtrees
        #plus the keyLength of the root.
        return lWidth + rWidth + curr.keyLength;

    #Height call function
    def Height(self):
        return self.FindHeight(self.root);

    #Height recursive function
    def FindHeight(self,curr):
        if(curr is None):
            #Subtree is empty, width is 0
            return 0;

        lHeight = self.FindHeight(curr.leftChild); #Height of left subtree
        rHeight = self.FindHeight(curr.rightChild); #Height of right subtree

        #The height of a tree is the largest height of its subtrees,
        #plus one for the root.
        if(lHeight > rHeight):
            #The left subtree is longer
            return lHeight+1;
        else:
            #The right subtree is longer
            return rHeight+1;

    def NodeHeight(self,key):
        #A node's height is the node's distance from the root#
        curr = self.root; #Start from root
        h = 0; #The height travelled so far. For root, it is zero.

        while(curr is not None):
            if(key < curr.key):
                #key is in the left subtree of curr
                curr = curr.leftChild;
                h += 1;
            elif(key > curr.key):
                #key is in the right subtree of curr
                curr = curr.rightChild;
                h += 1;
            else:
                #Found node. Return height and node
                return [h,curr];

        #Node wasn't found
        return -1;

    def NodeWeight(self,key):
        curr = self.root; #Start searching for node from root

        #Find node with given key
        while(curr is not None and curr.key != key):
            if(key < curr.key):
                curr = curr.leftChild;
            elif(key > curr.key):
                curr = curr.rightChild;
            else:
                break;

        if(curr.key == key):
            #Found node
            subtree = self.ListInOrder(curr,[]); #The subtree rooted at curr
            #The weight of the subtree. We subtract one, to remove the root.
            return len(subtree)-1;

        #Node doesn't exist
        return -1;


    ###PRINT###
    def PrintTree(self):
        if(self.IsEmpty()):
            #The tree is empty, there's nothing to print
            print "Tree is empty";
            return;

        w = self.Width(); #Tree's width
        h = self.Height(); #Tree's height

        #The array to get printed. Empty places are represented by spaces.
        #The array is wxh.
        pArray = [[' ' for i in range(h)] for j in range(w)];

        #We beginning building pArray from the top left element (0,0)
        self.PrintTreeRecursively(self.root,0,0,pArray);

        #Print pArray, by concatating the nodes in pArray to p line-by-line
        p = "";
        for i in range(h):
            for j in range(w):
                p += pArray[j][i];

            print p;
            p = "";

    def PrintTreeRecursively(self,curr,y,x,pArray):
        #y : height index
        #x : width index
        if(curr is not None):
            #Children should be inserted in the array one level below curr (y+1)

            #We insert elements in this order:
            #a) Left Child
            #b) Current Node (curr)
            #c) Right Child
            
            #Every time we insert a node, we need to move x.
            #That's way each functions returns a new x.
            x = self.PrintTreeRecursively(curr.leftChild,y+1,x,pArray);
            x = self.PassToArray(curr,y,x,pArray); #Insert curr to pArray
            x = self.PrintTreeRecursively(curr.rightChild,y+1,x,pArray);

        return x;

    def PassToArray(self,curr,y,x,pArray):
        #We pass the digits of the key to pArray one-by-one.
        temp = str(curr.key);
        for i in range(curr.keyLength):
            pArray[x+i][y] = temp[i];

        #Move x keyLength (the number of digits in curr.key) to the right.
        x += curr.keyLength;
        return x;


    ###RE-ARRANGING###
    def Rearrange(self):
        ####
        #iList contains the inorder represantation of the tree.
        #a and b points each time to a different subtree.
        #Every time the middle element is the root of the subtree.
        #Elements on the left are on its left subtree.
        #Elements on the right are on its right subtree.
        #Recursively we build the tree by going from root to root.
        ###
        inOrder = self.InOrder(); #The inorder traversal of tree
        temp = len(inOrder); #Number of non-deleted nodes
        
        self.DeleteTree(); #Delete the current tree
        #Rebuild the tree from the beginning
        self.BuildFromInOrder(inOrder,0,temp-1,temp);

    def BuildFromInOrder(self,iList,a,b,maxNodes):
        #index points to the middle of inorder list (iList)
        index = int(math.ceil((a+b)/2.0));

        if(index < maxNodes):
            #index is less than maxNodes, so not all nodes have been inserted.
            #Insert node in the middle of iList
            self.Insert(iList[index]);

        if(a < b):
            #The subtree on the left of index
            self.BuildFromInOrder(iList,a,index-1,maxNodes);
            #The subtree on the right of index
            self.BuildFromInOrder(iList,index+1,b,maxNodes);
        else:
            #Subtree is empty
            return;

        ##Example##
        #
        #Let the inorder represantation 1,3,5,7,10,11 stored in iList.
        #First we find the root of the tree:
        #
        #a=0, b=5, index = ceil((a+b)/2) = 3
        #
        #We insert iList[index] (= 7) to the tree. This is the tree's root.
        #We then work on the left subtree. a=0 b=index-1 (b=2)
        #So the left subtree is 1,3,5.
        #We repeat the process and we insert 3, then 1.
        #Now a=b=0. So (a<b) is False, so the function returns to its caller,
        #where index=1, key=3.
        #We now start working on the right subtree of 3.
        #The parameters we pass are index+1 (2) and b (2).
        #Now root index = ceil((a+b)/2) = 2
        #The subtree root is iList[2] (=5), which we insert in the tree.
        #Because a=b, the function returns to its caller, where index=3, key=7,
        #a=0, b=5.
        #
        #We now work on the right subtree of 7, with index from index+1 (4) to
        #b (5). New root index = ceil((a+b)/2) = 5.
        #We insert iList[index] (=11) and then we add node with key=10.
        #The tree is complete.
        #In the next recursive call, the parameters are a=4 and b=4, so
        #the process has ended and the final tree was built.
        #
        ##End of Example##


    ###IDENTITY###
    #Identity call function
    def Identity(self,rearrange=True):
        if(rearrange):
            #If the user doesn't say otherwise, rearrange the tree before
            #finding its identity array.
            self.Rearrange();

        h = self.Height(); #The height of the tree
        n = pow(2,h)-1; #The number of nodes in a tree of height h, is (2^h)-1
        
        identity = ['']*n; #Create an empty array of n positions
        self.BuildIdentity(self.root,identity,1); #Build identity, from the root

        return identity; #Return the identity array

    #Identity building function
    def BuildIdentity(self,curr,identity,index):
        #To build the identity we replicate the inorder traversal, and we add
        #the current node to the matrix instead of printing it.
        #a) Build for left subtree
        #b) Add curr to identity
        #c) Build for right subtree
        #
        #The positions of the nodes are given by the following:
        #index is the position curr occupies in the identity array
        #index : [1,n]
        lIndex = 2*index; #The left child of curr occupies the 2*index position
        rIndex = 2*index+1; #The right child occupies the 2*index+1 position

        if(curr is not None):
            #curr exists
            if(curr.leftChild is not None):
                #The left child of curr exists, build for the left subtree
                self.BuildIdentity(curr.leftChild,identity,lIndex);

            identity[index-1] = curr.key; #Place curr.key in the identity
            
            if(curr.rightChild is not None):
                #The right child of curr exists, build for the right subtree
                self.BuildIdentity(curr.rightChild,identity,rIndex);



b = BinarySearchTree();

b.Insert(3);
b.Insert(1);
b.Insert(2);
b.Insert(4);
b.Insert(-5);
b.Insert(11);
b.Insert(13);
b.Insert(0);
