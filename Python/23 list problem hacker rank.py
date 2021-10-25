from array import *


n = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)-n):
    arr.pop()

arr.sort()

arr.reverse()

runup=arr[0]

for i in range(n):

    if runup!=arr[i+1]:
        runup=arr[i+1]
        break

print(runup)



