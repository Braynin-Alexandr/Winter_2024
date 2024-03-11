# -*- coding: utf-8 -*-

#Задача 22.2
def rec_function(lst, res=None):

    if res is None:
        res = []

    lst=sorted(lst)

    if len(lst)==1:
        res.extend(*lst)
        return
    else:
        rec_function(lst[1:], res)
        if lst[0][1] in res:
            res.append(lst[0][0])
        return f'Максимальная длина: {len(res)-1} {sorted(res)}'

lst=[(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8)]
print(rec_function(lst))
print()

#Задача 22.3
def check_kw_in_string(string):
    import re, keyword

    if type(string) != str: raise ValueError (f'Значение должно быть str')
    def check_word(word):
        if word.group() in keyword.kwlist: return '<kw>'
        else: return word.group()

    result = re.sub(r'\b\w+\b', check_word, string)
    return result


s='Этот урок поможет вам изучить, как использовать операторы True, False, if, for, while в Python'
print(check_kw_in_string(s))
