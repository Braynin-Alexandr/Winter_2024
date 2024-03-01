# -*- coding: utf-8 -*-

##Задача 19-1
import itertools

wallet= [10,50,100,200,500,1000,2000,5000]

count=1
for i in range(2, len(wallet)+1):
    for j in itertools.combinations(wallet, i):
        print(f'Набор №{count}. Купюры набора: {j}. Общая сумма: {sum(j)} руб.')
        count+=1
print()

##Задача 19-2
class Fibonacci:
    def __init__(self):
        self.a=0
        self.b=1
        self.c=0
    def __next__(self):
        self.c = self.a
        self.a = self.b
        self.b = self.c+self.b
        return self.c
    def __iter__(self):
        return self


Fabi=Fibonacci()

for _ in range(8):
    print(next(Fabi))
print()


##Задача 19-3
class Person:
    def __init__(self,  surname, name, patronymic):
        self.surname=surname
        self.name=name
        self.patronymic=patronymic
    def __str__(self):
        result_full_name=str(self.surname)+str(self.name)+str(self.patronymic)
        return result_full_name[::-1]


p=Person("Иванов", "Михаил", "Федорович")
print(p)