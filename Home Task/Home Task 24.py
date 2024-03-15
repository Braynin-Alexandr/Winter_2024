# -*- coding: utf-8 -*-
#Задача 24-1
def f_sort_numbers(lst):
    if len(lst)==1: return 'Ошибка, сортировка невозможна'

    check=['Ошибка' for number in lst if not isinstance(number, (float, int))]
    if 'Ошибка' in check: return 'Ошибка, в списке должны быть типы данных \'float\' или \'int\''

    while True:
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                break
        else:
            return lst


lst=[11.2, -76,1.231, 7.4, 21, 110, 33, 66, 39.2, 20,100]
print(f_sort_numbers(lst))
print()

#Задача 24-2
import psycopg2

con=psycopg2.connect(
    database='postgres',
    user='postgres',
    password='',
    host='127.0.0.1',
    port='5432'
)

cur=con.cursor()

cur.execute('''SELECT * FROM public.min_amount''')

print('Минимальное количество книг авторов')
for row in cur:
    print(f'{row[0]}: {row[1]} шт.')

con.commit()
con.close()
print()

#Задача 24-3
def count_brackets(string):
    if type(string) != str or len(string)==0: return 'Ошибка'

    if ')' in string or '(' in string:
        deep = 0
        for s in string:
            if deep > 0: return False
            elif s == '(': deep -= 1
            elif s == ')': deep += 1
    else: return 'Ошибка'

    return True if deep==0 else False
s='(()) (( () () ) () )'
# s=input('Ввод скобок: ')
print(count_brackets(s))

# "()" => true
# ")(()()" => false
# "(" => false
# "(()) (( () () ) () )" => true
# "())(()" => false

