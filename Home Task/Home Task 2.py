# #Задание 2-1
n = int(input("Задание 1. Введите целое число n: "))

if 1<=n<=9:
    for x in range(1, 10):
        print(f"{x}х{n}={x*n}")
else: print("Ошибка")
print()


#Задание 2-2
lst=[7, 0, -1, 5, -10]
min_elememt=lst[0] #путь первый элемент списка будет минимальный; далее через цикл сравним его с остальными элементами

for element in lst[1:]:
    if element <= min_elememt:
        min_elememt=element
print(f"Задание 2. Минимальный элемент списка {lst}: {min_elememt}")
print()


# Задание 2-3
n = int(input("Задание 3. Введите число: "))

if n<0:print("Ошибка, введено отрицательное число")
elif n==0: print(f"факториал 0! = 1")
else:
    f = 1  #первое число в произведении факториала
    for x in range(1,n+1):
        f=f*x
    print(f"факториал {n}! = {f}")