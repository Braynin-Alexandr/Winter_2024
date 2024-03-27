# -*- coding: utf-8 -*-
#Задача 29-1

numbers=[int(x) for x in input('Введите цифры через пробел: ').split()]

#1-й вариант
from collections import Counter
print(*[num for num, count in Counter(numbers).items() if count==1])

#2-й вариант
print(*[num for num in set(numbers) if numbers.count(num)==1])
print()



# #Задача 29-2
def Hamming(str_1,str_2):
    return len([i for i in range(len(str_1)) if str_1[i]!=str_2[i]])

string_1=input('Введите первую строку: ')
string_2=input('Введите вторую строку: ')
print(f'Количество несовпадающих букв: {Hamming(string_1, string_2)}')
print()



#Задача 29-3
def isomorphic_words(w_1, w_2):

    if len(w_1)!=len(w_2) or (type(w_1)!=str and type(w_2)!=str): return False

    len_w=len(w_1)
    map_w = tuple((w_1.index(w_1[i]), w_2.index(w_2[i])) for i in range(len_w))

    for point_1, point_2 in map_w:
        if point_1!=point_2:
            return False

    return True

while True:
    word_1= input('Введите 1-е слово: ')
    word_2= input('Введите 2-е слово: ')
    print('Ответ:', isomorphic_words(word_1,word_2))
    print()


#Задача 29-3, 2-й вариант
def isomorphic_words(w_1, w_2):

    if len(w_1)!=len(w_2) or (type(w_1)!=str and type(w_2)!=str): return False

    pairs_letters_key_w1={}
    pairs_letters_key_w2={}

    for i in range(len(w_1)):
        pairs_letters_key_w1.setdefault(w_1[i], set()).add(w_2[i])
        pairs_letters_key_w2.setdefault(w_2[i], set()).add(w_1[i])

    for letter in pairs_letters_key_w1.values():
        if len(letter)>1: return False

    for letter in pairs_letters_key_w2.values():
        if len(letter)>1: return False

    return True


while True:
    word_1=input('Введите 1-е слово: ')
    word_2=input('Введите 2-е слово: ')
    print('Ответ:', isomorphic_words(word_1,word_2))
    print()
