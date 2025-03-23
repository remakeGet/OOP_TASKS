class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        avg_grd = self.average_grade()
        result += f'Средняя оценка за домашние задания: {avg_grd}\n'
        result += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
        result += f'Завершенные курсы: {", ".join(self.finished_courses)}\n'    
        return result       

    def average_grade(self):
        total_grades = 0
        total_courses = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            total_courses += len(grades)
        return total_grades / total_courses if total_courses > 0 else 0

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'        
         
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        avg_grd = self.average_grade()
        result += f'Средняя оценка за лекции: {avg_grd}\n'
        return result    
    
    def average_grade(self):
        total_grades = 0
        total_courses = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            total_courses += len(grades)
        return total_grades / total_courses if total_courses > 0 else 0
    
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        result =  f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return result 
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'    

some_student = Student('Ruoy', 'Eman', 'Male')
some_student2 = Student('Vanya', 'Ivanov', 'Male')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']

some_student2.courses_in_progress += ['Ruby']
 
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
 
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 4)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 5)

best_lecturer1 = Lecturer('Johny', 'Ivanov')
best_lecturer2 = Lecturer('Stan', 'Petrov')
best_lecturer1.courses_attached += ['Ruby']
best_lecturer2.courses_attached += ['Python']


some_student.rate_lecturer(best_lecturer2,'Python', 9)
some_student.rate_lecturer(best_lecturer2,'Python', 5)
some_student2.rate_lecturer(best_lecturer1,'Ruby', 10)
some_student2.rate_lecturer(best_lecturer1,'Ruby', 3)

print(some_reviewer)
print(best_lecturer1)
print(best_lecturer2)
print(some_student)

print(some_student > some_student2)  # Сравнение студентов по средней оценке
print(best_lecturer1 < best_lecturer2)  # Сравнение лекторов по средней оценке