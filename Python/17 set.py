myset = {1, 2}
print(myset)
lis = [1, 4, 5, 6, 8]
set1 = set(lis)
print(set1)

set2 = set()
print(set2)
set1.add(10)
print(set1)
print(len(set1))

set1.add('Mansi')
print(set1)

set1 = list(set1)
print(set1)
set1 = set(set1)
print("set1: ", set1)

set2.update([11, 45, 47, 44])
print(set2)

set2.add((1, 5, 4))
print(set2)

set2.update({1, 11, 3})
print(set2)

set2.update({1, 6}, [5, 13])  # not included 1 coz already present in the set
print(set2)

# discard and remove functions take single input only

set2.discard(44)
print(set2)
print(len(set2))
set2.discard(4)  # not found because of ()
print(set2)

set2.remove(47)
print("set2: ", set2)
# set2.remove(20)   #will provide an error since 20 is not present in the set
# print(set2)
print("set1: ", set1)

# union function for values in set a or b

set3 = set1.union(set2)
print("union on set1 and set2 is set3: ", set3)

# Union using "|"
# operator
#set3 = set1|set2

# intersection function for common of a and b sets
set4 = set1.intersection(set2)
print("intersection of set 1 and set2 ie. set4: ", set4)

# Intersection using
# "&" operator
#set3 = set1 & set2

# difference function to get elements which are in a but not in b
set5 = set1.difference(set2)
print("difference() for set1 to set2 ie, set5 : ", set5)
print("difference() for set2 to set1: ", set2.difference(set1))
# Difference of two sets
# using '-' operator
#set3 = set1 - set2

# looping could be used in sets but we cant not refer indexes since set is an un ordered structure

print(set3)
for i in range(3, 7):
    set3.remove(i)  # elements 3, 4, 5, 6 will be removed from the set
print("first 4 elements removed from set3 using looping set3: ", set3)
# note if the element of the range is not present in the set remove will return an error but discard will not return an error it will simply skip that element
print(len(set3))
for i in set3:
    print(i, end=" ")
print("/")
print('Mansi' in set3)
print(20 in set3)

frozen_set = frozenset(["e", "f", "g"])

print("\nFrozen Set")
print(frozen_set)

# Adding elements to the
# set using iterator
people = {"Jay", "Idrish", "Archi"}
for i in range(1, 6):
    people.add(i)

print("\nSet after adding element:", end=" ")
print(people)

print(set3)
set3.clear()
print(set3)

#funvtions for checking relation between two given sets
set6 = set()
set7 = set()

for i in range(1, 6):
    set6.add(i)
for i in range(3, 8):
    set7.add(i)

print("Set6 = ", set6)
print("Set7 = ", set7)
print("\n")
set62=set6
set6 = set6|set7
set7=set62 & set7

# Checking relation between set6 and set7
if set6 > set7:  # set6.issuperset(set7)
    print("Set6 is superset of Set7")
elif set6 < set7:  # set6.issubset(set7)
    print("Set6 is subset of Set7")
else:  # set6 == set7
    print("Set6 is same as Set7")

# displaying relation between set7 and set6
if set7 < set6:  # set7.issubset(set6)
    print("Set7 is subset of Set6")
    print("\n")

# difference between set6 and set7
set8 = set6 - set7

# checkv if set7 and set8 are disjoint sets
if set7.isdisjoint(set8):
    print("Set7 and Set8 have nothing in common\n")
