#24.Python program to implement matrix addition .
X=[[2,3,1],[3,3,5],[2,3,2]]
Y=[[8,5,3],[8,5,2],[8,3,12]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]
for R in result:
    print(R)

