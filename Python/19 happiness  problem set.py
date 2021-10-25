from array import*
x=input()
X=x.split()
for i in range(len(X)-2):
    X.pop()
n=int(X[0])
m=int(X[1])

y=input()
a=input()
b=input()

Y=y.split()
for i in range(len(Y)-n):
    Y.pop()
Y=list(map(int,Y))
arr=array('i',Y)

A=a.split()
for i in range(len(A)-m):
    A.pop()
A=list(map(int,A))
B=b.split()
for i in range(len(B)-m):
    B.pop()
B=list(map(int,B))
setA=set(A)
setB=set(B)


ini_happ=0

for i in range(0,n):
    check=arr[i] in setA

    if check==True:
        ini_happ=ini_happ+1

    check=arr[i] in setB
    if check==True:
        ini_happ=ini_happ-1

print(ini_happ)







