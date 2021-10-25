from array import*
from functools import reduce
n=int(input())
X=input()
W=input()
# print(X)
# print(W)
Xi=list(map(int,X.split()))
# Xi=int(X.split())
for i in range(len(Xi)-n):
    Xi.pop()
# print(Xi)
Xi= array('i',Xi)
# print(Xi)
# Wi=int(W.split())
Wi=list(map(int,W.split()))
for i in range(len(Wi)-n):
    Wi.pop()

Wi=array('i',Wi)
mult=array('i',[])
# print(mult)
for i in range(n):
    ele=Xi[i]*Wi[i]
    mult.append(ele)

sum=reduce(lambda a,b:a+b,mult)
sum2=reduce(lambda a,b:a+b,Wi)
Weight_mean=sum/sum2
print(round(Weight_mean,1))



