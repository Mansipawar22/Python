#time comparison of list comprehension and for loop

import time


def for_loop(n):
    result = []
    for i in range(n):
        result.append(i ** 2)
    return result


# define function to implement list comprehension
def list_comprehension(n):
    return [i ** 2 for i in range(n)]


# Driver Code

# Calculate time takens by for_loop()
begin = time.time()
for_loop(10 ** 6)
end = time.time()

# Display time taken by for_loop()
print('Time taken for_loop:', round(end - begin, 2))

# Calculate time takens by list_comprehension()
begin = time.time()
list_comprehension(10 ** 6)
end = time.time()

# Display time taken by for_loop()
print('Time taken for list_comprehension:', round(end - begin, 2))

#time taken in list comprehension is less as compared to for loop


print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])

print([[i, j, k] for i in range(0, 1) for j in range(0, 2) for k in range(0, 3)])

# this is equivalent to
# >>> results = []
# >>> for x in [1, 2, 3]:
# ...     for y in [4, 5, 6]:
# ...         results.append([x, y])
# ...
# >>> print(results)        in for loops

ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0]
print(ListOfThreeMultiples)