# -*- coding: utf-8 -*-
#Задача 26-1

def func_compare_strings(str1, str2):
    if len(str1+str2)<1:return False
    if (str1 in str2) and (abs(len(str1)-len(str2))<=1): return True

    difference = 0
    try:
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                difference += 1
        else:
            return True if difference <= 1 else False
    except: return False


while True:
    str1=input('Строка 1:')
    str2=input('Строка 2:')
    print('Ответ:',func_compare_strings(str1,str2))
    print()

#Задача 26-2


def dis(self):
    for k,v  in self.__dict__.items(): print(f'атрибут: \'{k}\', значение: \'{v}\'')

Pet = type('Pet', (), {'dis':dis})
my_pet = Pet()
my_pet.name='Tom'
my_pet.age=1
my_pet.dis()
print()

#Задача 26-3
class Person:
    def __init__(self, age):
        self.__age =age
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, other_age):
        if 1<other_age<100: self.__age=other_age
        else: print('Недопустимый возраст')
    @age.deleter
    def age(self):
        del self.__age

man1=Person(3)
print(man1.age)

man1.age=101
print(man1.age)
