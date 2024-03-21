# -*- coding: utf-8 -*-
#Задача 27-1
n = int(input("Введите число n: "))


matrix = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        matrix[i][j] = min(i,j, (n-i-1), (n-j-1)) + 1

for row in matrix:
    print(*row)
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