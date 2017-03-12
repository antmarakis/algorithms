class Node:
    def __init__(self,v,p=None,w=False):
        self.word = w; #If the node represents the end of a word or not
        self.parent = p; #The parent of the node
        self.value = v; #The char value in the node
        self.children = {}; #Node's children

class Trie:
    def __init__(self):
        self.root = Node(''); #The root of the trie (always empty)


    def Insert(self,word):
        curr = self.root; #curr holds the current node/vertex. Start from root.
        l = len(word); #The length of the word
        for i in range(l):
            last = False;
            if(i == l-1):
                #The last char of the word
                last = True;

            c = word[i];
            if(c not in curr.children):
                curr.children[c] = Node(c,curr,last);
            elif(last):
                #c exists, but as it is the last char of word, it should now
                #be flagged as a word in the trie.
                curr.children[c].word = True;

            curr = curr.children[c];

    def Search(self,word):
        #Start from the root. For every char in word, go down one level.
        #If we can't go down a level, then the word doesn't exist.
        #If we do, and the current char is the last char of the word and
        #the node we are currently is a word, then we have found the word
        #and should return.
        curr = self.root;
        l = len(word);

        for i in range(l):
            c = word[i];
            
            if(c not in curr.children):
                #There is no prefix of cWord + c
                return False; #Word doesn't exist

            if(i == l-1 and curr.children[c].word):
                #Last char of wrod, and the node c of curr is a word
                return True;

            curr = curr.children[c]; #Move to the next level

        return False; #Didn't find the word

    def FindWords(self,prefix):
        #Find all words with the given prefix
        v = self.SearchAndReturn(prefix);
        
        wList = self.FindWordsFunction(v,prefix); #The list of words to return
        if(v is not None and v.word):
            #v exists and the prefix is itself a word, add it to the list.
            wList.append(prefix);
        
        return wList;

    def SearchAndReturn(self,word):
        #Start from the root. For every char in word, go down one level.
        #If we can't go down a level, then the word doesn't exist.
        #If we do, and the current char is the last char of the word and
        #the node we are currently is a word, then we have found the word
        #and should return the final node.
        curr = self.root;
        l = len(word);

        for i in range(l):
            c = word[i];
            
            if(c not in curr.children):
                #There is no prefix of cWord + c
                return None; #Word doesn't exist

            if(i == l-1):
                #Last char of wrod, and the node c of curr is a word
                return curr.children[c];

            curr = curr.children[c]; #Move to the next level

        return None; #Didn't find the word

    def FindWordsFunction(self,v,cWord):
        #cWord : The word built up to v
        if(v is None):
            #v doesn't exist
            return None;

        wList = []; #This will contain the words under v
        for i,k in v.children.iteritems():
            #Iterate through node's children
            tWord = cWord+i; #Add i to the current word
            
            if(k.word):
                #If the iterated prefix is a word, add it to the list
                wList.append(tWord);

            #The list of words under tWord
            wList.extend(self.FindWordsFunction(k,tWord));

        return wList; #Return the list we calculated
