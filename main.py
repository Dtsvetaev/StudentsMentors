

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

cool_lecturer1 = Lecturer('John', 'Doe')
cool_lecturer1.courses_attached += ['Python', 'Git']
cool_lecturer1.grades = {'Python': [9, 9, 10], 'Git': [10, 10, 9]}

cool_lecturer2 = Lecturer('Jane', 'Smith')
cool_lecturer2.courses_attached += ['Python', 'Git']
cool_lecturer2.grades = {'Python': [8, 9, 9], 'Git': [7, 8, 9]}

cool_reviewer1 = Reviewer('Some', 'Buddy')
cool_reviewer1.courses_attached += ['Python', 'Git']

cool_reviewer2 = Reviewer('Another', 'Reviewer')
cool_reviewer2.courses_attached += ['Python', 'Git']

best_student1 = Student('Ruoy', 'Eman', 'your_gender')
best_student1.courses_in_progress += ['Python', 'Git']
best_student1.finished_courses += ['Введение в программирование']
best_student1.grades = {'Python': [10, 9, 8], 'Git': [9, 8, 7], 'Введение в программирование': [10, 10, 9]}

best_student2 = Student('Anna', 'Smith', 'her_gender')
best_student2.courses_in_progress += ['Python', 'Git']
best_student2.grades = {'Python': [8, 7, 6], 'Git': [7, 6, 8]}


print(cool_lecturer1)
print(cool_lecturer2)
print(cool_reviewer1)
print(cool_reviewer2)
print(best_student1)
print(best_student2)

def average_hw_grade_for_course(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    if len(total_grades) == 0:
        return 0
    return sum(total_grades) / len(total_grades)


def average_lecture_grade_for_course(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    if len(total_grades) == 0:
        return 0
    return sum(total_grades) / len(total_grades)

students = [best_student1, best_student2]
lecturers = [cool_lecturer1, cool_lecturer2]

course = 'Python'
print(f"Средняя оценка за домашние задания по курсу '{course}': {average_hw_grade_for_course(students, course):.1f}")

course = 'Git'
print(f"Средняя оценка за домашние задания по курсу '{course}': {average_hw_grade_for_course(students, course):.1f}")

course = 'Python'
print(f"Средняя оценка за лекции по курсу '{course}': {average_hw_grade_for_course(students, course):.1f}")


# best_reviewer = Reviewer('Bob', 'Don')
#
# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python', 'Git']
# best_student.finished_courses += ['Введение в программирование']
# best_student.grades = {'Python': [10, 9, 8], 'Git': [9, 8, 7], 'Введение в программирование': [10, 10, 9]}
#
# cool_student = Student('Jane', 'Smith', 'her_gender')
# cool_student.courses_in_progress += ['Python', 'Git']
# cool_student.grades = {'Python': [8, 7, 6], 'Git': [7, 6, 8]}
#
# cool_lecturer = Lecturer('John', 'Doe')
# cool_lecturer.courses_attached += ['Python', 'Git']
# cool_lecturer.grades = {'Python': [9, 9, 10], 'Git': [10, 10, 9]}
#
# print(best_reviewer)
# print(cool_lecturer)
# print(best_student)
# print(cool_student)
#
# if best_student < cool_student:
#     print("У студента cool_student средняя оценка за домашние задания выше")
# else:
#     print("У студента best_student средняя оценка за домашние задания выше")

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