n=int(input())


for i in range(n):
    even=""
    odd=""
    str1=input()
    for j in range(len(str1)):
        if j%2==0:
            even=even+str1[j]
        else:
            odd=odd+str1[j]

    print(even,odd)




