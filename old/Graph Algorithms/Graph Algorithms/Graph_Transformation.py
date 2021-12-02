from Graph_Node import Node;
from CreateDirectedGraph import BuildDirectedGraph;
from CreateUndirectedGraph import BuildUndirectedGraph;

def Build(size=-1,directed=True):
    nodes = [];

    if(size > 0):
        if(directed):
            BuildDirectedGraph(size);
        else:
            BuildUndirectedGraph(size);

    f = open("_graph_matrix.txt",'r');
    l = f.read().splitlines();
    f.close();

    for i in range(len(l)):
        nName = chr(i + ord('A'));
        nodes.append(Node(nName));

    for i in range(len(l)):
        dis = l[i].split(' ');

        for j in range(len(dis)):
            if(int(dis[j]) > 0):
                nodes[i].edges.append([nodes[j],int(dis[j])]);

    return nodes;
