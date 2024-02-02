print("Задание 6-1. Римские цифры в десятичное число")

dct = dict(IV=4, IX=9, XC=90, XL=40, CD=400, CM=900, I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
s = input("Введите римские цифры: ").upper()
res=0

while s!="": #в цикле идет уменьшение/обрезка длины введенной строки через срезы ниже
    for i in dct:
        if s.startswith(i):
            res+=dct[i]
            s = s[len(i):] #обрезаем строку "s" c помошью среза s[len(i):] и пересохраняем её
            break #переходим в цикл While после каждый интерации (определения буквы)
print(res)
print()


print("Задание 6-1. Римские цифры в десятичное число. Альтернатива")

dct = dict(I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000, IV= 4, IX = 9, XC = 90, XL = 40, CD = 400, CM = 900)
string = input("Введите римские цифры: ").upper()
res=0
index=0

while len(string)>index:
    current_roma_number = string[index] #присваеваем римскую цифру переменной current_roma_number

    if index+1<len(string): #конструкция, чтобы проверить, есть ли здесь двойная римская цифры, и не выйти за границы индексов в строке string
            key_double_number=current_roma_number+string[index+1] #находим возможный ключ для двойных римских цифр
            if key_double_number in dct:
                res+=dct[key_double_number]
                index+=2 #прибавляем к индексу 2, тк. взяли 2 римских цифры
            else:
                res+=dct[current_roma_number]
                index+=1 #прибавляем к индексу 1, тк. взяли 1 римскую цифру
    else:
        res+=dct[current_roma_number] #последняя буква; это нужно, чтобы не вызвать ошибку и не выйти за индексы в стркое if index+1<len(string)
        break

print(res)




print("Задание 6-2")
# Получает на вход две строки, в которых перечисляются
# книги, прочитанные двумя учениками.
#Выводит количество книг, которые прочитали оба ученика.

s1=set(input("Список книг 1: ").split(", "))
s2=set(input("Список книг 2 :").split(", "))
print(len(s1.intersection(s2)))
print()


print("Задание 6-3")
s=set(input("Ввод: "))
letters, numbers, sym= "", "", ""

for x in s:
    if x.isalpha():
        letters+=x
    elif x.isdigit():
        numbers+=x
    elif not x.isalnum(): # al (pha) + num (ber)
        sym+=x

print(" ".join(list(letters)), " ".join(list(numbers)), " ".join(list(sym)),  sep="\n")
