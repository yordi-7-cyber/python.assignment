def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result
n=int(input("Enter your number:"))        
result=factorial(n)
print(result)