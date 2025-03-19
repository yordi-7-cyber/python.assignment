def multiplication(number,upto):
    for i in range(1, upto + 1):
        print(f"{number} x {i} ={number * i}")
number=int(input("Enter your number:"))
upto=int(input("Enter the range:"))
    
    
multiplication(number, upto)    