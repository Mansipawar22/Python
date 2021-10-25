n=int(input("enter the number"))
# def fact(n):
#     fac=1
#     if n==1:
#         return fac
#     else:
#         for i in range(n,0,-1):
#             fac=fac*i
#     print(fac)
# fact(n)

#recurssion

def fact(n):
    if n==0:
        return 1
    if n==1:
        return 1
    fac = n * fact(n - 1)
    return fac

print(fact(n))



