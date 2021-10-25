matrix = []

for i in range(3):

    # Append an empty sublist inside the list
    matrix.append([])

    for j in range(5):
        matrix[i].append(j)
print(matrix)

#same thing using list comprehension
mat = [[j for j in range(5)] for i in range(3)]
print(mat)

mat = [[i for j in range(2)] for i in range(3)]
print(mat)

# using lambda to print table of 5
numbers = []
for i in range(1, 6):
    numbers.append(i * 10)
print(numbers)

#using list comprehension
numbers = [i * 10 for i in range(1, 6)]
print(numbers)

# using lambda to print table of 5
numbers = list(map(lambda i: i * 10, [i for i in range(1, 6)]))
print(numbers)