from array import *


arr = array('i', [])

size_array = int(input("Enter the size of the array:"))

print(f"Size of the array is {size_array}.")

for i in range(size_array):
    val1 = int(input(f"Enter {i+1}th value:"))
    arr.append((val1))

print(arr)


search = input("Do you want to search any number in the array?")

if search == 'yes' or search == 'Yes':
    val2 = int(input("Enter the Value you want to search."))
    index = -1
    for e in arr:
        if e == val2:
            index = arr.index(e);
            print(f"Your number present at index {index}.")
            break
    if index == -1:
        print("Your number is not present in th array.")

else:
    print("Thanks for using the app.")

# for e in arr:
#     print(e)