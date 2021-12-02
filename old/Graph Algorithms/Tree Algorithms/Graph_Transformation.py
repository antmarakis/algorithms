from Graph_Node import Node;

nodes = [];

f = open("_distance_matrix.txt",'r');
l = f.read().splitlines();
f.close();

for i in range(len(l)):
    nName = chr(i + ord('A'));
    nodes.append(Node(nName));

for i in range(len(l)):
    dis = l[i].split(' ');

    for j in range(len(dis)):
        if(int(dis[j]) > 0):
            nodes[i].children.append([nodes[j],int(dis[j])]);

for n in nodes:
    print n.children;
