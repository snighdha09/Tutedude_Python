n =int(input("Enter a number: "))
def factorial (a):
    if a<2:
        return 1
    else:
        return a* factorial(a-1)

result = factorial(n)
print ("Factorial of ",n," is: ",result)