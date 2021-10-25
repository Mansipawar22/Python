list_size = int(input("Enter the size of yhe list."))
list = []

for i in range(list_size):
    print(f"Enter {i + 1} element in the list:")
    temp = int(input())
    list.append(temp)
print(list)

# creating new list
new_list = []
for i in range(len(list)):
    new_list.insert(i, list[-1])
    list.pop(-1)

for i in range(len(new_list)): #copy the element of rever list in tho orginal list
    list.append(new_list[i])

print(list) 
