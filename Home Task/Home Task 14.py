# -*- coding: utf-8 -*-
# #Задача 14-1
def count_num(number, count=0):
    number = str(number)
    if len(number)>0:
        return count_num(number[1:], count+1)
    else:
        return f'Количество цифр: {count}'


number=int(input("Вычислим количество цифр введенного целого числа n (n>=0): "))
print(count_num(number))
print()

#Альтернативное решение задача 14-1
def count_num(n):
    if n<10:
        return 1
    else:
        return 1 + count_num(n//10)


number=int(input("Вычислим количество цифр введенного целого числа n (n>=0): "))
print(count_num(number))



# #Задача 14-2
class NotNaturalNumberError(Exception):
    pass
def check_natural_number(x):
    if x<=0: raise NotNaturalNumberError(x)

def sum_nat_num(n):

    try:
        check_natural_number(n)

    except NotNaturalNumberError as e:
        return f"Ошибка, {e} не является натуральным числом"

    else:
        if n<10: return n
        else:
            return n%10 + sum_nat_num(n//10)

number=int(input("Вычислим сумму цифр натурального числа: "))
print(sum_nat_num(number))
print()



# Задача 14-3
def tri_2(n):
    if n==1:
        print("*")
        return
    else:
        print("*"*n)
        tri_2(n-1)
        print("*"* n)

tri_2(int(input("Введите число, чтобы напечатать два треугольника: ")))