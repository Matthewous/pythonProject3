def average_grade(self):
    sum = 0
    grades = 0
    for a in self.grades.values():
        for grade in a:
            sum += grade
            grades += 1
    av_grade = sum / grades
    return round(av_grade, 1)

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

    def __eq__(self, other):
        return average_grade(self) == average_grade(other)
    def __ne__(self, other):
        return average_grade(self) != average_grade(other)
    def __gt__(self, other):
        return average_grade(self) > average_grade(other)
    def __lt__(self, other):
        return average_grade(self) < average_grade(other)
    def __ge__(self, other):
        return average_grade(self) >= average_grade(other)
    def __le__(self, other):
        return average_grade(self) <= average_grade(other)
    

def av_course(st_list, course):
    course = course
    st_list = list(st_list)
    summary = 0
    quantity = 0

    for stud in st_list:
        for key, val in stud.grades.items():
            if key is course:
                for grade in val:
                    summary += int(grade)
                    quantity += 1
    if quantity == 0:
        phrase = 'Оценок нет'
    else:
        phrase = f'Средняя оценка на курсе {course} - {round(summary / quantity,1)}' 
    return phrase


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

    def __eq__(self, other):
        return average_grade(self) == average_grade(other)
    def __ne__(self, other):
        return average_grade(self) != average_grade(other)
    def __gt__(self, other):
        return average_grade(self) > average_grade(other)
    def __lt__(self, other):
        return average_grade(self) < average_grade(other)
    def __ge__(self, other):
        return average_grade(self) >= average_grade(other)
    def __le__(self, other):
        return average_grade(self) <= average_grade(other)

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





best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

student_2 = Student('Mat', 'Daman', 'male')
student_2.courses_in_progress += ['Python']

cool_Reviewer_1 = Reviewer('Some', 'Buddy')
cool_Reviewer_1.courses_attached += ['Python']

cool_Reviewer_1.rate_hw(best_student, 'Python', 10)
cool_Reviewer_1.rate_hw(best_student, 'Python', 8)
cool_Reviewer_1.rate_hw(best_student, 'Python', 9)

cool_Reviewer_1.rate_hw(student_2, 'Python', 5)
cool_Reviewer_1.rate_hw(student_2, 'Python', 7)
cool_Reviewer_1.rate_hw(student_2, 'Python', 9)

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
print(cool_Reviewer_1)
print()
print(cool_Lecturer_1)
print()
print(best_student)
print()

# для начала вывожу значения для сравнения(для наглядности)
print("Сравнение лекторов")
print(average_grade(cool_Lecturer_1))
print(average_grade(cool_Lecturer_2))
print(cool_Lecturer_1 == cool_Lecturer_2)
print(cool_Lecturer_1 != cool_Lecturer_2)
print(cool_Lecturer_1 > cool_Lecturer_2)
print(cool_Lecturer_1 < cool_Lecturer_2)
print(cool_Lecturer_1 >= cool_Lecturer_2)
print(cool_Lecturer_1 <= cool_Lecturer_2)


# для начала вывожу значения для сравнения(для наглядности)
print("\nСравнение студентов")
print(average_grade(best_student))
print(average_grade(student_2))
print(best_student == student_2)
print(best_student != student_2)
print(best_student > student_2)
print(best_student < student_2)
print(best_student >= student_2)
print(best_student <= student_2)


python_students = [best_student, student_2]
python_lecturers = [cool_Lecturer_1, cool_Lecturer_2]

print(av_course(python_students, "Python"))
print(av_course(python_lecturers, "Git"))