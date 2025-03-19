class MathOperation:
    def add(self, num1, num2, num3=0):
        return num1 + num2 + num3
math = MathOperation()

print(math.add(3, 5))
print(math.add(3, 5, 7))   