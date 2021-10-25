if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    for i in range(len(arr)-n):
        arr.pop()
    arr.reverse()
    for i in arr:
        print(i, end=" ")
