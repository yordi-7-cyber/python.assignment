class Car:
    def move(self):
        print("The car is moving fast.")

class Bike:
    def move(self):
        print("The bike is moving slowly.")

def move_speed(speed):
    speed.move()
car = Car()
bike = Bike()

move_speed(car)
move_speed(bike)
