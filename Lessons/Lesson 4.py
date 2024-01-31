#Словари

# hm={}
# s=input("Текст:")
#
# for k in s:
#     if k not in hm:
#         hm[k] = 0
#     hm[k] = hm[k]+1
#     if k in hm:
#         print(k, hm[k])
#



# person = {
#     "name": "Маша",
#     "login": "masha",
#     'age': 25
# }
# print(person)
# person['name'] = "Миша"
# print(person)

# dct={1:123, 2:"xdsfjslfkjsdklf", 345:True}
# print(dct[345])


#добавляем ключ и значение
# dict={}
#
# while True:
#     s=input()
#     if s=="0":
#         break
#     else:
#         if s not in dict:
#             dict[s]=0
#         dict[s]+=1
#         continue
# print(dict)


#если ключи и значеия равны, то True. порядок не имеет значения
# dct_1=
#     {
#     False: 456,
#     True: 123
#     }
#
# dct_2=
#     {
#     True: 123,
#     False: 456
#     }
# print(dct_1 == dct_2)

#последнее значение всегда вытесняет предыдущее
# dct_1=
#     {
#     False: 456,
#     True: 123
#     }
#print(dct_1)



#
# dict= {
#     "1":"один",
#     "2":"два",
#     "3":"три",
#     "4":"четыре",
#     "5":"пять",
#     "6":"шесть",
#     "7":"семь",
#     "8":"восемь",
#     "9":"девять",}
#
# s=input()
# for x in s:
#     if x in dict:
#         print(dict[x], end=" ")
#     else:print("*", end=" ")



#как создать словарь
# dct_1={"a": 123, "b": 234}
#
# dct_2={}
# dct_2["a"] = 16
#
# dct_3=dict(a=123, b=234)
#
# letter= ["a","b"]
# digit = [123, 123]
# dct_4=dict(zip(letter, digit))
# print(dct_1,dct_2, dct_3,dct_4)


#Задача
# months={1:31, 2:28, 3:31, 4:31, 5:31, 6:30, 7:31, 8:31,9:30, 10:31, 11:30, 12:31}
# while True:
#     year=int(input("Введите год "))
#     month=int(input("Введите месяц "))
#     if year+month==0: break
#     if year%4==0 and month==2:
#         print("29")
#     else:
#         print(months[month])

# # удаление элемента
# dct={"чтото":2}
# del dct["чтото"]
# print(dct)


#функция длины словаря
# dct={1:11, 2:22}
# print(len(dct))


# задача
# string=input().split()
# dct={}
#
# for x in string:
#     if x not in dct:
#         dct[x]=0
#     dct[x] += 1
# print(dct)



# задача
# dct={}
# s=input("Введите буквы: ").split()
#
# for x in s:
#     if x not in dct:
#         dct[x]=0
#     dct[x] += 1
# print(dct)
#
# word=s[0]
# for k in dct:
#     if dct[k] > dct[word]:
#         word=k
#
# print(word, dct[word])



# s=input("Ввод: ").split()
# dct_1, dct_2 = {},{}
#
# for word in s[0]:
#     if word not in dct_1:
#         dct_1[word]=0
#     dct_1[word]+=1
#
# for word in s[1]:
#     if word not in dct_2:
#         dct_2[word] = 0
#     dct_2[word] += 1
#
# print(dct_1)
# print(dct_2)
# print(dct_2==dct_1)


# tpl=(1,2,3, [1,2,3])
# tpl[3].clear()
# print(tpl)

# tpl=(123,234,345, 456, 567, 678, 789, 890)
# x=int(input())
# res=0
#
# if x<=123:res = (x,)+tpl
# elif x>= 890: res = tpl + (x,)
# else:
#     for k,v in enumerate(tpl[1:],1):
#         if x>= tpl[k-1] and x <= v:
#             res = tpl[:k] + (x,) + tpl[k:]
#             break
# print(res)

