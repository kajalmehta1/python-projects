#Write a Python program to get the Factorial number of given number.

from math import factorial
from re import I


num=int(input("enter the number:  "))
factorial=1
if num<0:
    print("sorry")
elif num==0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num +1):
        factorial=factorial*i
    print("the fac is",num,"is",factorial)

