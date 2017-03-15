from Graph_Transformation import Build;


def BFS(node):
    for n in node.edges:
        c = n[0];
        if c in used or c in queue:
            continue;

        edges.append([node,n[0],n[1]]);
        queue.append(c);


nodes = Build();
used = [];
edges = [];
queue = [nodes[0]];

while queue:
    n = queue[0];
    queue = queue[1:];
    BFS(n);
    used.append(n);

print used;
print edges;
