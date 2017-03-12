from random import randint;

w = input();

V = [[1 for x in range(w)] for y in range(w)];

for i in range(len(V)):
    for j in range(len(V)):
        V[i][j] *= randint(0,5);

for i in range(len(V)):
    print V[i];
