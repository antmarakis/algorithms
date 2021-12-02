from random import randint;

w = input();

V = [[1 for x in range(w)] for y in range(w)];

for i in range(len(V)):
    for j in range(i,len(V)):
        if(i == j):
            V[i][i] = 0;
            continue;
        
        V[i][j] *= randint(0,5);
        V[j][i] = V[i][j];

for i in range(len(V)):
    print V[i];
