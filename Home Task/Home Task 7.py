print("Задача 7.1. Рассчитываем НОК")
def find_NOK(a,b):

    if a<1 or b<1:
        return "Ошибка"
    else:
        while a!=b:
            if a>b:
                a,b = b,a-b
            else:
                b,a =a, b-a

    return a

a,b=list(map(int,input("Введите 2 натуральных числа: ").split()))
print(find_NOK(a,b))



print("Задача 7.2. Шифр Цезарь")
def сaesar (string, n):

    res=""

    for x in string:
        if x.isalpha():
            x=chr((ord(x)+n))
            res+=x
        else:
            res+=x

    return res

string=input("Строка: ")
n=int(input("Сдвиг: "))

print(сaesar(string,n))

print("Задача 7.3.Функция, сортирующая двумерный массив чисел)
def sort_list(a):

    result_lst=[]

    for x in a: #перебираем подсписок
        for y in x: #перебираем элементы подсписка
            result_lst.append(y) #добавляем элем. подсписка в общий рез. список

    res=sorted(result_lst)[-3:]
    return res

x=[[1,6,3],[4,5,4]] #условный 2-мерный массив чисел

print(sort_list(x))