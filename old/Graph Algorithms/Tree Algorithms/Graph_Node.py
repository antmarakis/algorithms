class Node:
    def __init__(self,name):
        self.name = name;

        self.children = []; #A list of tuples (pointer,weight)

    def __repr__(self):
        return self.name;
