from functools import reduce
def add(x):
    sum=reduce(lambda a,b:a+b,x)
    print("The SUM of the no. is: ",sum)


def sub(x):
    subs = reduce(lambda a, b: a - b, x)
    print("The SUBSTRACTION of the no. is: ",subs)

def mul(x):
    prod = reduce(lambda a, b: a*b, x)
    print("The MULTIPLICATION of no. is: ",prod)

def divi(x):
    div = reduce(lambda a, b: a / b, x)
    print("The DIVISION of no. is: ",div)

