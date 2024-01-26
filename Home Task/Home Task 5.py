# print("Задача 5-1. Не сделал")
# number=int(input("Ввод: "))
# lst=[] #итоговый список
#
# for row in range(1,number+1):
#     lsts=[1]*(row) #создаём строки из "1"
#
#
#     for index in range(row-1):  #в строчке 1 перебираем все элементы по индексу, потом в  срочке 2 и т.д.
#         if index!=0 and index!=number+1: #крайние цифры пирамиды - "1"
#
#
#         lst.append(lsts)  # добавляёем подсписок в общий список
#
# for c in lst:
#     print(c)
# #


print("Задача 5-2. Напечатать все делители. Простой вариант")
n=int(input())
lst=[]

for x in range(1, n+1):
    if n%x==0:
        print(x, end= " ")

print()
print()


print("Задача 5-3. Фибоначчи")
n=int(input("Ввод: "))
a,b=1,1

for k in range(n):
    print(a, end=" ")
    a, b = b, a+b