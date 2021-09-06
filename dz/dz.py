class Table:
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

class Homeworks:
    def __init__(self, title, theme, course):
        self.title = title
        self.theme = theme
        self.course = course

    def __str__(self):
        return f"{self.title}, {self.theme}, {self.course}"

homework = [Homeworks("Homework 1", "Variables","Python"),
            Homeworks("Homework 2", "Lists", "Python")]

def add_homework(homework):
    SH = []
    for i in homework:
        SH.append(str(i))
    for h in students:
        h.homeworks.append(SH)

def show_students(students):
    for i in students:
        print(i)

students = [Table("Richard", 14, 78, "Python"),
            Table("Nikolai", 17, 34, "Python"),
            Table("Maria", 16, 97, "Python")]

add_homework(homework)
show_students(students)
