from random import randint;

def BuildUndirectedGraph(size):
    V = [[1 for x in range(size)] for y in range(size)];

    for i in range(size):
        for j in range(i,size):
            if(i == j):
                V[i][j] = 0;
                continue;
        
            V[i][j] *= randint(0,9);
            V[j][i] = V[i][j];


    f = open("_graph_matrix.txt",'w');

    for i in range(size):
        l = "";

        for j in range(size):
            l += str(V[i][j]) + ' ';

        l = l[:len(l)-1];

        if(i < len(V)-1):
            l += '\n';

        f.write(l);

    f.close();
