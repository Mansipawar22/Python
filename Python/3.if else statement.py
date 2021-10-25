# #syntax
#
# n=84
#
# if n==84:
#     print("the value is 84")
#     print("yes ")
#
# else:
#     print("the value is not 84")
#
#
#
# name=input("enter your name:")
#
# if name=='mansi':
#     print(f"hello {name} welcome to python")
#
# else:
#     print(f"hello {name},you can not have excess to this course because you are a stranger")

#house price=1million good credit= 10 % bad credit=20% print the downpayment.
#
# price=int(input("the price of the house"))
# credit_score=input("enter the credit score")
#
# if credit_score=='good':
#     down_payment=price*10*.001
#     print(f"you have to pay {down_payment}, as a downpayment"
#           f"coz your credit score is {credit_score}")
#
# else:
#     down_payment=price*20*.001
#     print(f"you have to pay {down_payment}, as a downpayment"
#           f"coz your credit score is {credit_score}")


#good credit = 10%, medium= 15% and bad = 30%

#
# price=int(input("the price of the house"))
# credit_score=input("enter the credit score")
#
# if credit_score=='good':
#     down_payment=price*10*.001
#     print(f"you have to pay {down_payment}, as a downpayment"
#           f"coz your credit score is {credit_score}")
#
# elif credit_score=='medium':
#     down_payment=price*15*.001
#     print(f"you have to pay {down_payment}, as a downpayment"
#           f"coz your credit score is {credit_score}")
#
# elif credit_score=='bad':
#     down_payment=price*30*.001
#     print(f"you have to pay {down_payment}, as a downpayment"
#           f"coz your credit score is {credit_score}")
#
# else:
#     print("you can not afford this house")

#credit=high income= high valid customer
#
# income=int(input("enter your income"))
# credit_score=int(input("enter your credit"))
#
# if income>1000000:
#     high_income=True
# else:
#     high_income=False
#
# if credit_score>30:
#     good_credit=True
# else:
#     good_credit=False
#
# if high_income and good_credit:           #and opr is used in if statement
#     print("you are valid for credit card")
#
#
# else:
#     print("you are not eligible for credit card because "
#           "either your income is too low or your credit score is too low")



#weather condition
#
# temperature=int(input("enter the temp of today"))
#
# if temperature>30:
#     print("it is too hot today")
#
# elif temperature<10:
#     print("it is too cold today ")
#
# else:
#     print("it is a perfect day weather wise")


#name length problem
#
# name=input("enter your name")
# name_length=len(name)
#
# if name_length<=3:
#     print("name is too short")
#
# elif name_length>=20:
#     print("name is too long")
#
# else:
#     print("name is perfect")


#1kg=2.20462 lb   1 lb= 0.453592
#
#
# weight=int(input("enter your weight"))
# weight_type=input("enter the weight type l for pound and k for kg")
#
# if weight_type=='l' or weight_type=='L':
#     weight_kg=0.453592*weight
#     print(f"your weight in kg is {weight_kg}")
#
# elif weight_type=='k' or weight_type=='K':
#     weight_Lb=2.20462*weight
#     print(f"your weight in lb is {weight_Lb}")
#
# else:
#     print("write a proper weight type")



year=int(input("enter the year of your birth"))
month=int(input("enter the month of your birth"))
date=int(input("enter the date of your birth"))

years=2020-year
months=0
days=0

if month>5:
    months=((12-month) + 5)
else:
    years=years+1
    months=5-month

if date>27:
    days=27
else:
    days=27-date

age_yr=(years+(months/12)+(days/365))
print(f"your age in years is {age_yr}")

age_months=(months+(years*12)+(days/30))
print(f"your age in months is {age_months}")

age_days=(days+(years*365)+(months*30))
print(f"your age in days is {age_days}")

print(f"you are {years} years,{months} months and {days} days old")

N = int(input().strip())

if N % 2 == 0:
    if N >= 2 and N <= 5:
        print("Not weird")

    elif N >= 6 and N <= 20:
        print("Weird")

    elif N >= 20:
        print("Not Weird")

else:
    print("Weird")



