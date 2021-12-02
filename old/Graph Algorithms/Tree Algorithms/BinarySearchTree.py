from BinaryTree import *;


#Binary Search Tree Class#
class BinarySearchTree(BinaryTree):
    ###BASICS###
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



b = BinarySearchTree();

b.Insert(3);
b.Insert(1);
b.Insert(2);
b.Insert(4);
b.Insert(-5);
b.Insert(11);
b.Insert(13);
b.Insert(0);

b.PrintTree();
