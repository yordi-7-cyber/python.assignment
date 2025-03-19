class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
student1= Student("Yordanos Tesfaye", 21, "software engineering")
student2= Student("Misgana Teklu", 24, "computer engineering")
student3= Student("Hanun Adere", 22, "Medical labratory")
student1.display_info()
student2.display_info()
student3.display_info()
