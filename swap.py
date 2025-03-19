def swap(a, b):
    a, b = b, a
    return a, b
x = int(input("value of X= "))
y = int(input("value of y=  "))
x, y = swap(x, y)

print(f"Swapped values: x = {x}, y = {y}")


