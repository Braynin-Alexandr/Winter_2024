# -*- coding: utf-8 -*-
#Задача 27-1
n = int(input("Введите число n: "))

if 1<=n<=18:
    matrix=[[0]*n for _ in range(n)]
    len_m=len(matrix)
    for i in range(len_m):
        for j in range(len_m):
            matrix[i][j]=min(i, j, len_m-j-1, len_m-i-1)+1
    else:
        for m in matrix:
            print(*m)
else:
    print('Введено неверное число')
print()

#Задача 27-2
class item:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def __getattribute__(self, item):
        if item=='name':
            return object.__getattribute__(self, item).title()
        else:
            return object.__getattribute__(self, item)

    def __getattr__(self, item):
        if item=='total':
            return self.price*self.quantity

pt=item('pencil',100,3)

print(pt.name)
print(pt.total)
print()


#Задача 27-3
def count_elements(lst):
    count = 0
    if len(lst)==0:
        return count
    else:
        for element in lst:
            count+=1
            if type(element)==list:
                count+=count_elements(element)
    return count


# lst=
# print(count_elements(lst))