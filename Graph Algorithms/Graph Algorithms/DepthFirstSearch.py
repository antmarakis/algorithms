from Graph_Transformation import Build;


def DFS(node):
    used.append(node);
    for n in node.edges:
        c = n[0];
        if c in used:
            continue;

        edges.append([node,n[0],n[1]]);
        DFS(n[0]);


nodes = Build();
used = [];
edges = [];

for n in nodes:
    if(n not in used):
        DFS(n);

print used;
print edges;
