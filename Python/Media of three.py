print("Enter three value to calculate the median.")

number = []
for i in range(3):
    temp = int(input(f"Enter {i+1} value:"))
    number.append(temp)

def Median(number):
    number.sort()
    mid = len(number) // 2
    return number[mid]

print(f"Median of these number is {Median(number)}.")
