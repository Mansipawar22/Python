a = 10


# def man():
#     a=20
#     print(a)
# print(a)
# man()
# print(a)        #no chnage coz it is alocal variable

# def pan():
#     global a
#     print(a)
#     a=15
#     print(a)
# print(a)
# pan()
# print(a)        #since it is globally change


# global function

# x=22
# print(x,id(x))
# def nam():
#     globals()['x']=15
#     #print(m,id(m))
#     print(x,id(x))
# nam()
# print(id(x))
#


# passing a list to a function

def function(list):
    even = odd = 0
    for i in list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


n = int(input("enter the no. of elements in the list: "))
L = []
for j in range(n):
    ele = int(input("enter the element: "))
    L.append(ele)
print(L)
E, O = function(L)
print("the no. of even elements: ", E)
print("the no. of odd elements: ", O)
