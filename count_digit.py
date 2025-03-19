def count_digits(number):
    if number == 0:
        return 1
    count = 0
    number = abs(number)  
    while number > 0:
        count += 1
        number //= 10
    return count
num = int(input("Enter a number: "))
print(f"The number of digits in {num} is = {count_digits(num)}")
