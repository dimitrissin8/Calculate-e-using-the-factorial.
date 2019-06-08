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
