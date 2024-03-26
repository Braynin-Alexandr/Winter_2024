# -*- coding: utf-8 -*-
#Задача 29-1


# numbers=[5,5,2,5]
#1-й вариант
# from collections import Counter
# print(*[num for num, count in Counter(numbers).items() if count==1])

# #2-й вариант
# print(*[num for num in set(numbers) if numbers.count(num)==1])


#Задача 29-2
# def Hamming(str_1,str_2):
#     return len([i for i in range(len(str_1)) if str_1[i]!=str_2[i]]) #if ( len(str_1)==len(str_2) and (type(str_1)==str and type(str_2)==str) ) else 'Ошибка'
#
# print(Hamming('abc','xyz'))


#Задача 29-3
# def isomorphic_words(w_1, w_2):
#
#     if len(w_1)!=len(word_2): return False
#
#     len_w=len(w_1)
#     map_w = tuple((w_1.index(w_1[i]), w_2.index(w_2[i])) for i in range(len_w))
#
#     for point_1, point_2 in map_w:
#         if point_1!=point_2:
#             return False
#     else:
#         return True

# True:
# CBAABC DEFFED
# XXX YYY
# RAMBUNCTIOUSLY THERMODYNAMICS
# False:
# AB CC
# XXY XYY
# ABAB CD

# while True:
#     word_1= input('Введите 1-е слово: ')
#     word_2= input('Введите 2-е слово: ')
#     print('Ответ:', isomorphic_words(word_1,word_2))
#     print()

