class Course:
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration

    def get_details(self):
        return f"This course is called {self.course_name}, and it lasts for {self.duration} months."

class WebDevClass(Course):
    def __init__(self, course_name, duration, technologies_taught):
        super().__init__(course_name, duration)
        self.technologies_taught = technologies_taught
    def get_details(self):
        details = super().get_details()
        return f"{details} In this course, you'll learn systems  like {', '.join(self.technologies_taught)}."
web_dev_course = WebDevClass("Web Development", 3, ["HTML", "CSS", "JavaScript", "React"])
print(web_dev_course.get_details())
