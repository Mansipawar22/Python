num = int(input("Enter a Vlaue:"))


sum = 0

for i in range(1, num+1):
    sum = sum + i

print(sum)


def Sumnatural(num):
    if(num == 1):
        return 1
    return num + Sumnatural(num-1)

print(Sumnatural(num))