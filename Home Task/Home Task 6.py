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
