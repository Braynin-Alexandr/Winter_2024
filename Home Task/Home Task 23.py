# -*- coding: utf-8 -*-
#Задача 23-1
string='aabbaaccddcc'
# string=input('Введите строку: ')
max_palind=''

for index, letter in enumerate(string):
    current_sub_str=''
    current_sub_str+=letter
    for next_letters in string[index+1:]:
        current_sub_str+= next_letters
        if (current_sub_str==current_sub_str[::-1]) and (len(current_sub_str) >= len(max_palind)):
            max_palind=current_sub_str

print(f'Длина подстроки c наибольшим палиндромом: {len(max_palind)} ({max_palind})')
print()

# Задача 23-2
import pandas as pd
import psycopg2

con=psycopg2.connect(
    database='postgres',
    user='postgres',
    password=,
    host='127.0.0.1',
    port='5432'
)

cur=con.cursor()
cur.execute('''SELECT book_id, book_author, book_title, price, amount
                FROM BOOK
                ''')

table={'ID':[], 'АВТОР':[], 'НАЗВАНИЕ КНИГИ':[] ,'СТОИМОСТЬ':[],'КОЛИЧЕСТВО':[]}

rows = cur.fetchall()
for row in rows:
    table['ID'].append(row[0])
    table['АВТОР'].append(row[1])
    table['НАЗВАНИЕ КНИГИ'].append(row[2])
    table['СТОИМОСТЬ'].append(row[3])
    table['КОЛИЧЕСТВО'].append(row[4])

result=pd.DataFrame(table)
print(result)


con.commit()
con.close()
print()

# #Задача 23-3
def biggest_number(lst):

    from itertools import permutations
    max_ver=0
    for current_ver in permutations(lst):
        current_str_ver=''
        for number in current_ver:
            current_str_ver+=str(number)
        else:
            current_int_ver=int(current_str_ver)
            if current_int_ver>max_ver:
                max_ver=current_int_ver
    return f'Cамое большое число, которое можно составить из этих чисел: {max_ver}'
#
lst = [91, 51, 25, 92, 9, 5]
#lst=[int(x) for x in input('Введите числа через пробел: ').split()]
print(biggest_number(lst))
