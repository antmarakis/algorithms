from Graph_Transformation import Build;

nodes = Build();
used = [];
edges = [];

for n in nodes:
    if(n in used):
        continue;

    used.append(n);

    for c in n.edges:
        d = c[0];
        if(d in used):
            continue;

        used.append(d);
        edges.append([n,c[0],c[1]]);

print used;
print edges;
