# Enter your code here. Read input from STDIN. Print output to STDOUT
def symdif(n,m,M,N):
    lis = M.split()
    for i in range(len(lis)-m):
        lis.pop()

    newlis = list(map(int, lis))
    lis2 = N.split()
    for i in range(len(lis2)-n):
        lis2.pop()
    newlis2 = list(map(int, lis2))


    setm=set(newlis)
    setn=set(newlis2)


    setc=setm - setn
    setd=setn- setm
    setf=setc|setd

    lis3= list(setf)

    lis3.sort()


    for i in lis3:
        print("\n",i)


m=int(input())
M=input()
n=int(input())
N=input()

symdif(n,m,M,N)

