

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __int__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_lecture(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.finished_courses:
            if course in self.grades:
                self.grades[course] += [grade]
            else:
                self.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = sum(sum(grades) for grades in self.grades.values()) / sum(
            len(grades) for grades in self.grades.values())
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}"
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            lecturer.rate_lecture(self,course,grade)
        else:
            return 'Ошибка'

    def __str__(self):
        avg_grade = sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values())
        courses_in_progress_str = ", ".join(self.courses_in_progress)
        finished_courses_str = ", ".join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {avg_grade:.1f}\nКурсы в процессе изучения: {courses_in_progress_str}\nЗавершенные курсы: {finished_courses_str}"
    def __lt__ (self, other):
        return sum(sum(grades) for grades in self.grades.values()) / sum(len(grades) for grades in self.grades.values()) < sum(sum(grades) for grades in other.grades.values()) / sum(len(grades) for grades in other.grades.values())

best_reviewer = Reviewer('Bob', 'Don')

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']
best_student.grades = {'Python': [10, 9, 8], 'Git': [9, 8, 7], 'Введение в программирование': [10, 10, 9]}

cool_student = Student('Jane', 'Smith', 'her_gender')
cool_student.courses_in_progress += ['Python', 'Git']
cool_student.grades = {'Python': [8, 7, 6], 'Git': [7, 6, 8]}

cool_lecturer = Lecturer('John', 'Doe')
cool_lecturer.courses_attached += ['Python', 'Git']
cool_lecturer.grades = {'Python': [9, 9, 10], 'Git': [10, 10, 9]}

print(best_reviewer)
print(cool_lecturer)
print(best_student)
print(cool_student)

if best_student < cool_student:
    print("У студента cool_student средняя оценка за домашние задания выше")
else:
    print("У студента best_student средняя оценка за домашние задания выше")

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_lecturer = Lecturer('Some', 'Buddy')
# cool_lecturer.courses_attached += ['Python']
#
# best_student.rate_lecture(cool_lecturer, 'Python', 8)
#
# print(cool_lecturer.grades)
# print(cool_lecturer.grades)

# print(best_student.grades)