class Homework:
    def __init__(self, name, description, complexity, status):
        self.name = name
        self.description = description
        self.complexity = complexity
        self.status = status
        self.grade = 0

    def __str__(self):
        return f"{self.name}, {self.description}, {self.complexity}, {self.status}"


class Student:
    def __init__(self, name, age, subscribed_course):
        self.name = name
        self.age = age
        self.avarage_grade = 0
        self.subscribed_course = subscribed_course
        self.homeworks = []

    def __str__(self):
        ret = f"{self.name}, age: {self.age}, grade: {self.avarage_grade}, course: {self.subscribed_course}\n"
        ret = ret + "Homeworks:\n"
        for h in self.homeworks:
            ret = ret + "\t" + str(h) + "\n"
        return ret

    def add_homework(self, homework):
        self.homeworks.append(homework)

    def homework_status(self, status):
        ret_status = False
        if status == "+":
            ret_status = True
        for i in students:
            for h in i.homeworks:
                if ret_status == True:
                    h.status = True


# Helpers functions
def show_students(students):
    for s in students:
        print(s)

def sort_by_age(students):
    return sorted(students, key=lambda s: s.age)

def sort_by_grade(students):
    return sorted(students, key=lambda s: s.avarage_grade, reverse=True)

class Table:
    def __init__(self, name, age, subscribed_course):
        self.name = name
        self.age = age
        self.avarage_grade = 0
        self.subscribed_course = subscribed_course
        self.homeworks = []

    def show_studentss(studentss):
        for s in studentss:
            print(s)

    def add_homeworks(self, homework):
        for i in homework:
            self.homeworks.append(i)

students = [
    Student("Student 1", 12, "Python")
    , Student("Student 2", 16, "Python")
    , Student("Student 3", 15, "Python")
    , Student("Student 4", 14, "Python")
    , Student("Student 5", 10, "Python")
]

studentss = [
    Student("Student 1", 12, "Python")
    , Student("Student 2", 16, "Python")
    , Student("Student 3", 15, "Python")
    , Student("Student 4", 14, "Python")
    , Student("Student 5", 10, "Python")
    , Student("Student 6", 14, "Python")
    , Student("Student 7", 11, "Python")
]

homeworks = [
    Homework ("Homework 1", "Description 1", 2, False)
    ,Homework ("Homework 2", "Description 2", 5, False)
]



print("Initial")
show_students(studentss)
