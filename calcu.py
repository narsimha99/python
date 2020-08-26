import math


print("1.additon")
print("2.subtraction")
print("3.divison")
print("4.multiplication")
print("5.sqaroot")
print("6.square")
#here chose the option which operaton you want
option=int(input("enter your option:"))
#addition
if option ==1:

        add1=int(input("enter first number : "))
        add2=int(input("enter second number : "))
        ans=add1+add2
#subtraction
if option==2:


    sub1 = int(input("enter first number : "))
    sub2 = int(input("enter second number : "))
    ans = sub1-sub2
#Division
if option==3:

    div1= int(input("enter first number : "))
    div2 = int(input("enter second number : "))
    ans = div1/div2
#multiplication
if option==4:

    mul1 = int(input("enter first number : "))
    mul2 = int(input("enter second number : "))
    ans = mul1 * mul2
#squaring
if option==5:
    no1 = int(input("enter first number : "))
    no2 = int(input("enter second number : "))
    ans = no1**no2
#squaroot
if option == 6:
        no1 = int(input("enter square  number : "))

        ans = no1 *no1

print("output: " ,ans  )
