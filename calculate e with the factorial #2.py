#-----------------------------------------------------------------------------#
#Written by Dimitris Sinanis on 03/11/2017.
#This program calculate e with the factorial.
#Python version: 3.6.4
#-----------------------------------------------------------------------------#
#Find out what the factorial is, there: https://en.wikipedia.org/wiki/Factorial
#Find what is e there: https://en.wikipedia.org/wiki/E_(mathematical_constant)
#Note: When the accurency number goes to infinity you take back as a result e.
#So, accurency number ---> oo : result = e.
#-----------------------------------------------------------------------------#
"=================================The_code_begins_here===================================="

import math
def factorial(x):
    n=1
    for i in range(1,x+1):
       n=n*i
    return n
#x=int(input("Find the factorial of a number : "))
#print("The factorial of number {} is : {}".format(x,paragontiko(x)))
def e(accurency):
    s=0
    for i in range(0,accurency):
        s+=(1/factorial(i))
    return s
accurency=int(input("Give accurency number (for example: 44): "))
print("The number e with precision value {} equals to : {}".format(accurency,e(accurency)))
input("Press enter to close.")        

"=======================================The_end==========================================="

