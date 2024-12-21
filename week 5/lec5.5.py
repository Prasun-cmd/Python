r1=[1,4,6]
r2=[6,9,4]
r3=[2,6,4]

A=[]
A.append(r1)
A.append(r2)
A.append(r3)

s1=[3,9,7]
s2=[6,7,3]
s3=[2,0,5]

B=[]
B.append(s1)
B.append(s2)
B.append(s3)

c=[[0,0,0],[0,0,0],[0,0,0]]

dim=3
for i in range(dim):
    for j in range(dim):
        for k in range(dim):
            c[i][j]=c[i][j]+(A[i][k]*B[k][j])
print(c)