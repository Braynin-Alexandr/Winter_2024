# # -*- coding: utf-8 -*-
#
# # d={}
# # res={1:0, 2:1}
# # def fibo(n):
# #     d[n] = d.get(n, 0) + 1
# #     if n not in res:
# #         if n>2:
# #             res[n] = fibo(n-1) + fibo(n-2)
# #     return res[n]
# #
# # fibo(15)
# # print(d)
# # print(res)
# # lst=[1,2,[3,4]]
# # res=[]
# # def func(lst):
# #     for i in lst:
# #         if type(i) == int or type(i) == float: res.append(i)
# #         elif type(i) == list:
# #             func(i)
# #
# # func(lst)
# # print(res)
#
# import re
# string='числа 7 2 5 89 sad 999 2 99 и'
# res=re.findall(r"9" ,string)
# print(res)
#
# res1=re.findall(r"99" ,string)
# print(res1)
#
# res1=re.findall(r"[89]" ,string)
# print(res1)
#
# res2=re.findall(r"[7-9]" ,string) #интервал
# print(res2)
#
# res3=re.findall(r"\d" ,string) #все цифры
# print(res3)
#
# res4=re.findall(r"\d\d" ,string) #цифры стоящие подряд 2 раза, так как 2 d
# print(res4)
#
# res5=re.findall(r"\d{2}" ,string) #цифры стоящие 2 и 3 раза подряд
# print(res5)
#
#
# res5=re.findall(r"\d{1,5}" ,string) #цифры стоящие 1 раза подряд, 2 и тд
# print(res5)
#
# string="123 234 234 345 100 199 200 201 сумма"
# regex=r'1\d\d'
# print(re.findall(regex, string))
#
# string1="Косой косой косил траву на покосе"
# regex= r'кос'
# print(re.findall(regex,string1))
import re
# string='Мой номер телефона 123-467-5678'
# regex=r'\b\d{3}-\d{3}-\d{4}\b'
# print(re.findall(regex, string))

# string='номер авто A123BC78 или P456QR178'
# regex=r'\b[A-Z]\d{3}[A-Z]{2}\d{2,3}\b'
# print(re.findall(regex, string))

# text='Java самый Java популярный Java язык программировния в 2024 году'
# res= re.sub(r'Java',r'Python',text)
# print(res)

# text="Четные числа в строке 2 0 1 -2305 5 55 15 124 120 10"
# regex=r'[+-]?\d*[05]\b'
# print(re.findall(regex ,text))
import time

def fabi():
    с=0
    a, b = 0, 1
    while True:
        с+=1
        if a>100000000000000000000000000000000000000000000: break
        yield (f"число {a}, цифра №{с}")
        a,b=b,a+b


for i in fabi():
    print(i)