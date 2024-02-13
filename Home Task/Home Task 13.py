# -*- coding: utf-8 -*-
#
# #Задача 13-1
def fun_1(): #бесконечный генератор
    x=1
    while True:
        yield x if x%2 else -x
        x+=1


gen_fun_1=fun_1()

for _ in range(int(input("Сколько чисел вызвать из генератора?: "))): #способ ограничить бесконечный вывод чисел
    print(next(gen_fun_1), end=" ")
print()




#Задача 13-2

def fun_2():
    x=1
    while True:
        x_str=str(x)
        if x_str==x_str[::-1]: yield x
        x+=1


gen_3=fun_2()

for _ in range(int(input("Укажите кол-во палиндромов: "))): #способ ограничить бесконечный вывод чисел
    print(next(gen_3), end=" ")
print()


#Задача 13-3
def fun_3(lst):

    for i in lst:
        if i%2: yield i


# lst=[-5,1,4,6,8,9,33,2,55,3,5,7,0]
lst=list(map(int, input("Введите целые числа через пробел: ").split()))

gen_fun = fun_3(lst)

for i in gen_fun:
    print(i, end=" ")