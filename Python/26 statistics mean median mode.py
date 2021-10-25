from functools import reduce

N = int(input())
lis = input()
xi = lis.split()
for i in range(len(xi) - N):
    xi.pop()
mean=0
xi = list(map(int, xi))
sum= reduce(lambda a,b:a+b,xi)
mean=(sum/N)
print(round(mean,1))

xi.sort()
median=0
if N%2==0:

    for i in range(N):

        if i==((N//2)-1):
            A=xi[i]
            B=xi[i+1]
            median=((A+B)/2)

else:
    for i in range(N):
        if i==(N//2):
            median=xi[i]
print(round(median,1))
mode=xi[0]
count1=1

for i in range(N):
    count2=0
    for j in range(i,N):
        if xi[i]==xi[j]:
            count2=count2+1
    if count2>count1:
        count1=count2
        mode=xi[i]

print(mode)
