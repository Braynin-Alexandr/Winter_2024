# # #Задача 17-1
#
# def func(string):
#     import re
#     result = re.sub(r'\b(\w+)\b\s*[#№&+\-*.,:;"<>/!?]*\s*\b\1\b', r'\1',string, flags=re.I) # ищем два повторяющихся слова в паттерне \w+ и \1, но учитываем одно из них благодаря r'\1'
#     return result
#
# text = 'Напишите напишите программу программу, которая устраняет повторение повторение слов, т.е. результат результат должен быть следующим'
# # text=input("Введите предложение: ")
# res = func(text)
# print(res)
# print()
#
#
# #Задача 17-2
# def dec(func):
#     def wrapper(*args, **kwargs):
#         result_lst = []
#         result_lst.extend([word.upper() for word in args if type(word)==str]) #args
#         # for word in args:
#         #     word_up=word.upper()
#         #     result_lst.append(word_up)
#
#         result_lst.extend([value.upper() for value in kwargs.values() if type(value)==str]) #kwargs
#         # for value in kwargs.values():
#         #     value_up=value.upper()
#         #     result_lst.append(value_up)
#
#         return result_lst
#     return wrapper
#
# @dec
# def some_func(*args, **kwargs):
#     return
#
# result=some_func(1, "кошка", 2, 'собака', тип="домашние животные", уход='кормление', количество = 2)
# print(result)
# print()


#Задача 17-3
class Shape:
    def __init__(self, colour, square):
        self.colour = colour
        self.square = square

    def set_colour(self, new_colour):
        self.colour=new_colour
        print(f'Новый цвет объекта: {self.colour}')

    def show_colour(self):
        print(f'Цвет объекта: {self.colour}')

    def set_square(self,new_square):
        self.square=new_square
        print(f'Новая площадь объекта: {self.square}')

    def show_square(self):
        print(f'Площадь объекта: {self.square}')



a=Shape('Красный', 5)  #создали объект
print(a.__dict__)

a.set_colour('Синий') #установили новый цвет объекта
a.show_colour() #напечатали актуальный цвет объекта
a.set_square(10) #установили новую площадь объекта
a.show_square() #напечатали актуальную площадь объекта