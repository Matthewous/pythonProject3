class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(self, Student) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        recent_courses = ", ".join(self.courses_in_progress)
        finished_courses = ", ".join(self.finished_courses)
        res_name = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{average_grade(self)}\nКурсы в процессе изучения: {recent_courses}\nЗавершенные курсы: {finished_courses}'
        return res_name

    def compare(self, competitor_2):
        grade_1 = average_grade(self)
        grade_2 = average_grade(competitor_2)
        if grade_1 == grade_2:
            print('Оценки равны')
        elif grade_1 > grade_2:
            print(
                f"Средняя оценка студента {self.name} {self.surname} больше оценки студента {competitor_2.name} {competitor_2.surname} на {grade_1 - grade_2}")
        else:
            print(
                f"Средняя оценка студента {competitor_2.name} {competitor_2.surname} больше оценки студента {self.name} {self.surname} на {grade_2 - grade_1}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


class Lecturer(Mentor):

    def __str__(self):
        res_name = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции:{average_grade(self)}'
        return res_name

    def compare(self, competitor_2):
        grade_1 = average_grade(self)
        grade_2 = average_grade(competitor_2)
        if grade_1 == grade_2:
            print('Оценки равны')
        elif grade_1 > grade_2:
            print(
                f"Средняя оценка лектора {self.name} {self.surname} больше оценки лектора {competitor_2.name} {competitor_2.surname} на {grade_1 - grade_2}")
        else:
            print(
                f"Средняя оценка лектора {competitor_2.name} {competitor_2.surname} больше оценки лектора {self.name} {self.surname} на {grade_2 - grade_1}")


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
        res_name = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res_name


def average_grade(self):
    sum = 0
    grades = 0
    for a in self.grades.values():
        for grade in a:
            sum += grade
            grades += 1
    av_grade = sum / grades
    return round(av_grade, 1)


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

student_2 = Student('Mat', 'Daman', 'male')
student_2.courses_in_progress += ['Python']

cool_Reviewer = Reviewer('Some', 'Buddy')
cool_Reviewer.courses_attached += ['Python']

cool_Reviewer.rate_hw(best_student, 'Python', 10)
cool_Reviewer.rate_hw(best_student, 'Python', 8)
cool_Reviewer.rate_hw(best_student, 'Python', 9)

cool_Reviewer.rate_hw(student_2, 'Python', 5)
cool_Reviewer.rate_hw(student_2, 'Python', 7)
cool_Reviewer.rate_hw(student_2, 'Python', 9)

print(best_student.grades)

cool_Lecturer_1 = Lecturer('Mr', 'Smith')
cool_Lecturer_1.courses_attached += ['Python', 'Git']

cool_Lecturer_2 = Lecturer('Mrs', 'Brown')
cool_Lecturer_2.courses_attached += ['Python', 'Git']

# добавил логику, что студент может выставлять оценки только по завершенным курсам, добавил курс Git лектору ранее

best_student.finished_courses += ['Git']
best_student.rate_lec(cool_Lecturer_1, 'Git', 5)
best_student.rate_lec(cool_Lecturer_1, 'Git', 4)
best_student.rate_lec(cool_Lecturer_1, 'Git', 5)

best_student.rate_lec(cool_Lecturer_2, 'Git', 3)
best_student.rate_lec(cool_Lecturer_2, 'Git', 4)
best_student.rate_lec(cool_Lecturer_2, 'Git', 4)

print(cool_Lecturer_1.grades)
print()
print(cool_Reviewer)
print()
print(cool_Lecturer_1)
print()
print(best_student)
print()
cool_Lecturer_1.compare(cool_Lecturer_2)
best_student.compare(student_2)

# работает ли гит?


