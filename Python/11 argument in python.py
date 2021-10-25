# function argument

def person (name,**data):
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)

person('mansi',age=24,weight=63,height=5.5)

