# # Комментарии преподавателя:
# # В задаче 1:
# # необязательно вычислять среднее каждый раз, можно вне цикла до печати
# # В задаче 2:
# # number=str(int(input("Введите целое число: "))) то же самое, что number = input()
# # Цикл можно такой for check_number in '0123456789':
# # В задаче 3:
# # Непонятно зачем цикл while True ))))
#
#
# print("Задача 3-1. Напечатать среднюю зарплату сотрудников")
#
# summa_lst = [] #будем добавлять зарплаты в список
# res=0
#
# while True:
#     number=float(input("Введите зарплату сотрудника: "))
#     if number == 0: #0 - это окончание цикла
#         print("Программа завершена")
#         break
#
#     if number < 0: #если введено отрицательное число, то не учитываем его
#             print(f"Ошибка, Вы ввели отрицательное число: {number}, попробуйте снова")
#             continue
#     else:
#         summa_lst.append(number)  # добавляем зарплату в список
# res = sum(summa_lst) / len(summa_lst)
# print(f"Средняя зарплата сотрудников: {res}")
# print()
# #




# print("Задача 3-2")
# # lst=list(range(10))
# # print(lst)
#
# number=input("Введите целое число: ") #вводим целое число и переводим его в строку, чтобы найти с помощью метода count
# for check_number in range(10): #range (10), тк ишем цифры от 0 до 9
#     print(f"{check_number}-{number.count(str(check_number))}")
# print()



print("Задача 3-3")
all_words=input("Введите предложение: ").split() #переводим вводимое предложение в список
longest_word = all_words[0] #для первого цикла; пусть первый элемент списка условно будет самым длинным
all_longest_words = []  #для второго цикла; пустой список для добавления в него всех самых длинных слов

for word in all_words: #первое самое длинное слово
    if len(longest_word)<len(word): longest_word=word
for word in all_words: #найдем все слова по их длине, равной самому длинному слову, и добавим их в отдельный список
    if len(longest_word)==len(word): all_longest_words.append(word)

print(f"Первое самое длинное слово: {longest_word}.",  "Список самых длинных слов:",  ", ".join(all_longest_words))