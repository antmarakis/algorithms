#Path(i, j) = min(Path(i-1, j), Path(i, j-1)) + Matrix(i, j)


def CalculatePath(i, j):
    if(s[i][j] > 0):
        #We have already calculated solution for i,j; return it.
        return s[i][j];

    m1 = CalculatePath(i-1, j) + matrix[i][j]; #Optimal solution for i-1,j (top)
    m2 = CalculatePath(i, j-1) + matrix[i][j]; #Optimal solution for i,j-1 (left)

    #Store and return the optimal (minimum) solution
    if(m1 < m2):
        s[i][j] = m1;
        return m1;
    else:
        s[i][j] = m2;
        return m2;



f = open("_matrix.txt", 'r');
m = f.read().splitlines(); #Read from file line by line
f.close();

l = len(m); #The amount of lines in the matrix

#Initialize matrix array with lxl
matrix = [[0 for i in range(l)] for j in range(l)];
#Initialize solution array.
#A node of i,j in solution has an equivalent node of i,j in matrix
s = [[0 for i in range(l)] for j in range(l)];


for i in range(l):
    t = m[i].split(','); #Split a line by commas and input elements in t

    for j in range(l):
        #Add the elements in t into matrix
        matrix[i][j] = int(t[j]);

matrix = [[5, 3, 10, 17, 1],
          [4, 2, 9, 8, 5],
          [11, 12, 3, 9, 6],
          [1, 3, 4, 2, 10],
          [7, 11, 13, 7, 3]];

#Initialize first node as its matrix equivalent
s[0][0] = matrix[0][0];

#Initialize first column as the matrix equivalent + the above solution
for i in range(1, l):
    s[i][0] = matrix[i][0] + s[i-1][0];

#Initialize first row as the matrix equivalent + the left solution
for j in range(1, l):
    s[0][j] = matrix[0][j] + s[0][j-1];

print CalculatePath(l-1, l-1);
