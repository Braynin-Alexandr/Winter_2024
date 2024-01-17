#Задача №1
print("Задача №1")
x=float(input("Введите первое число x: "))
y=float(input("Введите второе число y: "))
print(f"Ответ: x*y={x*y}; x+y={x+y}")


#Задача №2
print("""
Задача №2, найти наибольшее из чисел: x+y, x–y, x*y, x/y, x//y
""")
x=float(input("Введите число x: "))
y=float(input("Введите число y: "))
a=x+y #a сложение
b=x-y #b вычитание
c=x*y #c умножение

if y==0: #если знаменатель равен 0, то не учитывае операции деления
    if a>b:
       if a>c:
            print(f"Наибольшее из чисел: {a}")
       else:
            print(f"Наибольшее из чисел: {c}")
    else:
        if b>c:
            print(f"Наибольшее из чисел: {b}")
        else:
            print(f"Наибольшее из чисел: {c}")

else: #если знаменатель не равен 0, то:
    d=x/y #d деление
    e=x//y #e деление нацело
    if a>b and a>c and a>d and a>e:
        print(f"Наибольшее из чисел: {a}")
    else:
        if b>c and b>d and b>e:
            print(f"Наибольшее из чисел: {b}")
        else:
            if c>d and c>e:
                print(f"Наибольшее из чисел: {c}")
            else:
                if d>e:
                    print(f"Наибольшее из чисел: {d}")
                else:
                    print(f"Наибольшее из чисел: {e}")


#Задача №2 (альтернативное решение)
print("""
Задача №2 (альтернативное решение)""")
x=float(input("Введите число x: "))
y=float(input("Введите число y: "))
a=x+y #сложение
b=x-y #вычитание
c=x*y #умножение

if y==0: #если знаменатель равен 0, то не учитываем деление
    print(f"Наибольшее из чисел: {max(x+y, x-y, x*y)}")
else: #если знаменатель не равен 0, то учитываем деление
    d = x/y  # деление
    e = x//y   #деление нацело
    print(f"Наибольшее из чисел: {max(x+y, x-y, x*y, x/y, x//y)}")


#Задача №3
print("""
Задача №3, Напечатать ВТОРОЕ ПО ВЕЛИЧИНЕ из чисел: x + y, x – y, x*y, x/y, x//y
""")
x=float(input("Введите число x: "))
y=float(input("Введите число y: "))
a=x+y #a сложение
b=x-y #b вычитание
c=x*y #c умножение

if y==0: #если знаменатель равен 0, то не учитывае операции деления
    if b<a<c:
            print(f"Второе по величине число: {a}")
    else:
        if a<b<c:
            print(f"Второе по величине число: {b}")
        else:
            print(f"Второе по величине число: {c}")

else: #если знаменатель не равен 0, то:
    d=x/y #d деление
    e=x//y #e деление нацело

    if a>b and a>c and a>d and a>e: #если самое большое число а
        if b>c and b>d and b>e:
            print(f"Второе по величине число: {b}")
        else:
            if c>d and c>e:
                print(f"Второе по величине число: {c}")
            else:
                if d>e:
                    print(f"Второе по величине число: {d}")
                else:
                    print(f"Второе по величине число: {e}")

    if b>a and b>c and b>d and b>e: #если самое большое число b
        if a>c and a>d and a>e:
            print(f"Второе по величине число: {a}")
        else:
            if c>d and c>e:
                print(f"Второе по величине число: {c}")
            else:
                if d>e:
                    print(f"Второе по величине число: {d}")
                else:
                    print(f"Второе по величине число: {e}")

    if c>a and c>b and c>d and c>e: #если самое большое число c
        if a>b and a>d and a>e:
            print(f"Второе по величине число: {a}")
        else:
            if b>d and b>e:
                print(f"Второе по величине число: {b}")
            else:
                if d>e:
                    print(f"Второе по величине число: {d}")
                else:
                    print(f"Второе по величине число: {e}")

        if d>a and d>b and d>c and d>e: #если самое большое число d
            if a>b and a>c and a>e:
                print(f"Второе по величине число: {a}")
            else:
                if b>c and b>e:
                    print(f"Второе по величине число: {b}")
                else:
                    if c>e:
                        print(f"Второе по величине число: {c}")
                    else:
                        print(f"Второе по величине число: {e}")

        if e>a and e>b and e>c and e>d: #если самое большое число e
            if a>b and a>c and a>d:
                print(f"Второе по величине число: {a}")
            else:
                if b>c and b>d:
                    print(f"Второе по величине число: {b}")
                else:
                    if c>d:
                        print(f"Второе по величине число: {c}")
                    else:
                        print(f"Второе по величине число: {d}")

#Задача 3
print("""
Задача №3, Напечатать ВТОРОЕ ПО ВЕЛИЧИНЕ из чисел: x + y, x – y, x*y, x/y, x//y (альтернативное решение)
""")
x=float(input("Введите число x: "))
y=float(input("Введите число y: "))
a=x+y  #a сложение
b=x-y  #b вычитание
c=x*y  #c умножение

if y==0:
    lst=[a,b,c]
    lst_sorted=sorted(lst, reverse=True)
else:
    d=x/y #d деление
    e=x//y #e деление нацело
    lst = [a, b, c, d, e]
    lst_sorted=sorted(lst, reverse=True)

print(lst_sorted[1])