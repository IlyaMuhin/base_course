class SchoolJournal:
    def __init__(self, subject, student):
        self.subject = subject
        self.student = student
        self.grade_list = []

    def grade(self):
        for i in range(int(input('Введите количество оценок: '))):
            self.grade_list.append(int(input(f'Введите {i+1} оценку: ')))
        
    def printer(self):
        print(f'Имя ученика:{self.student}')
        print(f'Название предмета:{self.subject}')
        print(f'Список оценок:{self.grade_list}')

    def final_grade(self):
        print("Средний балл:", sum(self.grade_list)/len(self.grade_list))


student1 = SchoolJournal('math', 'Илья')
student1.grade()
print("Оценки:", student1.grade_list)
student1.final_grade()


