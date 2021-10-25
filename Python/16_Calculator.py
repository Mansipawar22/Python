from Airthmetic_opr import *

print("What would you like to do?")
print("4 Types of calculation you can perform here")

rep=True
while rep==True:
    choice=input("""
    Press + for Additon
    Press - for Substraction
    Press * for Multiplication
    Press / for division
    Enter your choice: """)



    x=[]
    if choice=='+':
        n=int(input("How many no. you want to add: "))
        print("Enter values")
        for i in range(n):
            temp=int(input())
            x.append(temp)

        add(x)

    elif choice=='*':
        n = int(input("How many no. you want to multiply: "))
        print("Enter values")
        for i in range(n):
            temp = int(input())
            x.append(temp)
        mul(x)

    elif choice=='-':
        n = int(input("How many no. you want to substract: "))
        print("Enter values")
        for i in range(n):
            temp = int(input())
            x.append(temp)
        sub(x)

    elif choice=='/':
        n = int(input("How many no. you want to divide: "))
        print("Enter values")
        for i in range(n):
            temp = int(input())
            x.append(temp)
        divi(x)

    else:
        print("Invalid choice!")

    s=input("Do you want to continue yes or no: ")
    if s!='yes':
        print("Thank you for using our service for FREE")
        rep=False