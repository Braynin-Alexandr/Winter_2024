# #Задача 17-1
#
# def func(string):
#     import re
#     result = re.sub(r'\b(\w+)\b\s*[.,]*\b\1\b', r'\1',string) # ищем два повторяющихся слова в паттерне \w+ и \1, но учитываем одно из них благодаря r'\1'
#     return result
#
# # text = 'Напишите программу программу, которая устраняет повторение повторение слов, т.е. результат результат должен быть следующим'
# text=input("Введите предложение: ")
# res = func(text)
# print(res)
# print()

#Задача 17-2
def dec(func):
    def wrapper(*args, **kwargs):
        values=func(*args, **kwargs)
        result_lst = []

        for word in args:
            word_up=word.upper()
            result_lst.append(word_up)

        for value in kwargs.values():
            value_up=value.upper()
            result_lst.append(value_up)

        return result_lst
    return wrapper

@dec
def some_func(*args, **kwargs):
    return (args, kwargs)


result=some_func("кошка",'собака', тип="домашние животные")
print(result)
print()