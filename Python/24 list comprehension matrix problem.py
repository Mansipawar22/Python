from functools import reduce

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    mat = [[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1) for k in range(0, z + 1)]
    print(mat)
    final = []
    sum = 0
    for i in mat:
        sum = reduce(lambda a, b: a + b, i)
        if sum != n:
            final.append(i)
    print(final)