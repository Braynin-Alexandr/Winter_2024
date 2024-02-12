# -*- coding: utf-8 -*-
#
# #Задача 12-1
def lst_min_max (lst):

    if len(lst)>1:
        res_max=[i for i, x in enumerate(lst) if x==max(lst)]
        res_min=[i for i, x in enumerate(lst) if x==min(lst)]
        return print(res_min, res_max, sep=", ")

    else: return print(f'Недостаточно элементов в списке (минимум 2)')

    #расшифровка
    # res_max=[]
    # for i, x in enumerate(lst):
    #     if x==max(lst):
    #         res_max.append(i)
    #
    # res_min=[]
    # for i, x in enumerate(lst):
    #     if x==min(lst):
    #         res_min.append(i)

#
x=[1,2,3,4,1,2,3,4,1,4]
lst_min_max(x) #вызов функции
print()

#Задача 12-2

lst=[i for i in range(1,11) for j in range (1, i+1)]
print(*lst, sep=", ")
print()

#расшифровка
# for i in range(1,11):
#     for j in range(1,i+1):
#         print(i, end=" ")


#Задача 12-3
def natural_number (x):

    lst0=x.replace(" ", "").split(",") # ['1-2', '4-4', '3-6']
    lst1=[i.split("-") for i in lst0] # [['1', '2'], ['4', '4'], ['3', '6']]
    lst2=[[int(first_num), int(second_num)] for first_num, second_num in lst1] #[[1, 2], [4, 4], [3, 6]]

    res_lst=[]
    for first_num, second_num in lst2:
        for j in range(first_num, second_num + 1): #диапазоны между числами добавляем в range
            res_lst.append(j)
    return res_lst

# '1-2,4-4,3-6'
s=input("Введите диапазон натуральных чисел: ")
print(natural_number(s))

