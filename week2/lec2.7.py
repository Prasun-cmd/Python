#Cieser Cipher in cryptography

alpha='abcdefghijklmnopqrstuvwxyz'
i=25
print(alpha[(i%26)])
print(alpha[(i+1)%26])
print(alpha[(i+2)%26])

s='prasun'
# i expect result to be qsbtvo
r=''
i=0
k=1
r=r+(alpha[(((alpha.index(s[i]))+k)%26)])
r=r+(alpha[(((alpha.index(s[i+1]))+k)%26)])
r=r+(alpha[(((alpha.index(s[i+2]))+k)%26)])
r=r+(alpha[(((alpha.index(s[i+3]))+k)%26)])
r=r+(alpha[(((alpha.index(s[i+4]))+k)%26)])
r=r+(alpha[(((alpha.index(s[i+5]))+k)%26)])

print(r)
print(len(alpha))