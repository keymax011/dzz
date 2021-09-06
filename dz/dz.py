class Student:
    def __init__(self, name, age, avarage_grade, course):
        self.name = name
        self.age = age
        self.avarage_grade = avarage_grade
        self.course = course
        self.homeworks = []

    def __str__(self):
        ret = f"{self.name}, age: {self.age}, avarage grade: {self.avarage_grade}, course: {self.course}\n"
        ret = ret + "Homeworks:\n"
        for h in self.homeworks:
            ret = ret + "\t" + str(h) + "\n"
        return ret

class Table:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
        self.homeworks = []

    def __str__(self):
        ret = f"{self.name}, age: {self.age}, course: {self.course}\n"
        ret = ret + "Homeworks:\n"
        for h in self.homeworks:
            ret = ret + "\t" + str(h) + "\n"
        return ret

class Homeworks:
    def __init__(self, title, theme, course):
        self.title = title
        self.theme = theme
        self.course = course

    def __str__(self):
        return f"{self.title}, {self.theme}, {self.course}"

homework = [Homeworks("Homework 1", "Variables","Python"),
            Homeworks("Homework 2", "Lists", "Python")]

def add_homework(homework, student):
    SH = []
    for i in homework:
        SH.append(str(i))
    for h in student:
        h.homeworks.append(SH)

def show_students(students):
    for i in students:
        print(i)

def show_table(table):
    for i in table:
        print(i)

students = [Student("Richard", 14, 78, "Python"),
            Student("Nikolai", 17, 34, "Python"),
            Student("Maria", 16, 97, "Python")]

table_students = [Table("Richard", 14, "Python"),
            Table("Nikolai", 17, "Python"),
            Table("Maria", 16, "Python")]

add_homework(homework, students)
add_homework(homework, table_students)
print("Students", "\n")
show_students(students)
print("Table", "\n")
show_table(table_students)
