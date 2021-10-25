from array import*
from functools import reduce

def stdDev(arr,n):
    sum_of_vals=reduce(lambda a,b:a+b,arr)

    mean=sum_of_vals/n

    sqr = []
    for i in arr:
        a=i-mean
        b=a*a
        # print(int(b))
        sqr.append(b)


    sum_of_sqr = reduce(lambda a,b:a+b,sqr)
    std_dev = (sum_of_sqr/n)**0.5
    print(round(std_dev,1))

if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))
    for i in range(len(vals)-n):
        vals.pop()
    vals = array('i',vals)
    # print(vals)

    stdDev(vals,n)