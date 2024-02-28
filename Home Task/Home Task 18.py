# -*- coding: utf-8 -*-

#в данной программе сравниваются условные знания и возможности ученика с уровнем сложности задачи
class Tasks:
    def __init__(self, spisok):
        self.spisok = spisok  #список со словарями, где ключ - это названием задачи, а зачение - это сложность задачи

class Teacher:
    def __init__(self, name):
        self.name = name #имя учителя
        self.answers=[] #при отправке задачи ученику, изначальный уровень сложности задачи сохраним в answers, чтобы потом его применить в методе receive_task

    def send_home_task(self, home_task): #отправляем задачи всем ученикам
        for i in Pupil.group:
            i.take(home_task)
        self.answers.extend(home_task) #отправляём исхоную задачу в атрибут answers

    def receive_task(self, pupil_name, home_task):
        for pupil in Pupil.group:  # перебираем всех учеников
            if pupil.name == pupil:  # находим ученика по имени
                for pupil_answers in home_task:
                    for task_name, task_answer in pupil_answers.items():
                        for teacher_answer in self.answers:
                            if task_name in teacher_answer:
                                if task_answer >= teacher_answer[task_name]:
                                    pupil.set_tasks_mark(task_name, True)
                                else:
                                    pupil.set_tasks_mark(task_name, False)

class Pupil:
    group = []  #список всех учеников
    def __init__(self, name, knowledge, time, luck):
        self.name = name  # имя ученика
        self.knowledge = knowledge  #уровень знаний ученика
        self.time = time  #наличие времени на решение задач у ученика
        self.luck = luck  #удача ученика
        self.possibility = self.knowledge + self.time + self.luck  #совокупность условных умений и возможностей ученика для решения задач
        self.tasks_to_do = []  #список, где хранятся задачами от учителя
        self.tasks_done = [] #список, где хранятся задача и решения ученика; если неверное решение, то статус у задачи 'False'
        Pupil.group.append(self)

    #далее ученик получает задачу, например: {'ООП':3}, где 3- это уровень сложности задачи.
    #если ученик имеет необходимые качества, то есть совокупность знаний, времени и удачи, которые в сумме дают число >=3, то он получит "зачет", иначе "незачет"

    def take(self, home_task):
        self.tasks_to_do.extend(home_task) #добавили задачи в список, т.е. в "task to do" (атрибут ученика)

    def do_home_task(self):
        for task in self.tasks_to_do: # передаём задачу с её названием и сложностью
            for name_task, diffic_task in task.items():
                result={name_task:self.possibility} #указываем в качестве значения умение и возможность ученика решить задачу
                self.tasks_done.append(result) #добавляём в атрибут ученика tasks_done задачу (ключ) и условное умение ученика решить задачу (значение)

    def send_tasks_to_teacher(self, teacher):
        teacher.receive_task(self.name, self.tasks_done)

    def set_tasks_mark(self, task_name, mark):
        for task in self.tasks_done:
            print(task)
            if task.get(task_name):
                task[task_name] = mark


home_task_18 = Tasks([{'ООП': 5},{'RE':3},{'Рекурсия':4}]) #создаём задачи, где значения - уровени сложности

teacher = Teacher('Мастер') #создаём учителя

pupil_1 = Pupil('Люк Скайукоер', 2, 2, 0) #создаём учеников
pupil_2 = Pupil('Оби Ван', 3, 0, 2)
pupil_3 = Pupil('R2D2', 2, 0, 1)

teacher.send_home_task(home_task_18.spisok) #отправляем задачи ученикам

pupil_1.do_home_task() #ученики решают задачи
pupil_2.do_home_task()
pupil_3.do_home_task()

pupil_1.send_tasks_to_teacher(teacher) #ученики отправляют свои рещения учителю
pupil_2.send_tasks_to_teacher(teacher)
pupil_3.send_tasks_to_teacher(teacher)