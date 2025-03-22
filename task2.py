class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

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
        result = f'Лектор: {self.name} {self.surname}\n'
        for course, grades in self.grades.items():
            result += f'Курс: {course}, Оценки: {grades}\n'
        return result    
        
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'    

best_student1 = Student('Ruoy', 'Eman', 'your_gender')
best_student2 = Student('Vanya', 'Ivanov', 'your_gender')
best_student1.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Ruby']
 
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
 
cool_mentor.rate_hw(best_student1, 'Python', 10)
cool_mentor.rate_hw(best_student1, 'Python', 10)
cool_mentor.rate_hw(best_student1, 'Python', 10)
 
print(best_student1.grades)


best_lecturer1 = Lecturer('Johny', 'Ivanov')
best_lecturer2 = Lecturer('Stan', 'Petrov')
best_lecturer1.courses_attached += ['Ruby']
best_lecturer2.courses_attached += ['Python']


best_student1.rate_lecturer(best_lecturer2,'Python', 9)
best_student1.rate_lecturer(best_lecturer2,'Python', 9)
best_student2.rate_lecturer(best_lecturer1,'Ruby', 10)
best_student2.rate_lecturer(best_lecturer1,'Ruby', 9)

print(best_lecturer1)
print(best_lecturer2)