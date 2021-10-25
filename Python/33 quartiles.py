def median(quart_arr):
    median = 0
    N = len(quart_arr)
    if N % 2 == 0:
        for i in range(N):
            if i == ((N // 2) - 1):
                A = quart_arr[i]
                B = quart_arr[i + 1]
                median = ((A + B) / 2)

    else:
        for i in range(N):
            if i == (N // 2):
                median = quart_arr[i]

    return (int(median))


def quartiles(arr):
    for i in range(len(arr)-n):
        arr.pop()
    arr.sort()
    arr1 = []
    arr2 = []

    if n%2 == 0:
        for i in range(n):
            if i <= ((n//2)-1):
                arr1.append(arr[i])
            else:
                arr2.append(arr[i])

    else:
        for i in range(n):
            if i <= ((n//2)-1):
                arr1.append(arr[i])
            elif i > (n//2):
                arr2.append(arr[i])

    Q1 = median(arr1)
    Q2 = median(arr)
    Q3 = median(arr2)
    quar = []
    quar.append(Q1)
    quar.append(Q2)
    quar.append(Q3)

    return quar


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    data = list(map(int, input().rstrip().split()))



    res = quartiles(data)
    print(res)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')

