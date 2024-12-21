#moe on sets
A={1,3,5}
B={1,2,3,4,5}
print(A.issubset(B))
print(A.issuperset(B))

C={1,2,3}
D={4,5,6,3,2}
C1=C.union(D)
C2=C|D
print(C1,C2)

C3=D.intersection(C)
C4=D&C
print(C3,C4)

C5=C.difference(D)
C6=C-D
print(C5,C6)