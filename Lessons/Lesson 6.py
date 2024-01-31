#chr - показывает букву из номера
# lst=[]
# for x in range(ord("A"),ord("Z")+1):
#     print(f"буква {chr(x)}, код {x}")




# year=int(input("Год: "))
# if year%4==0 and year%100!=0 or year%400==0: print("Високосный")
# else:print("не високосный")





#гласные и согласные добавляем поочереди
# s=input()
# v,c = "", ""
# for i in s:
#     if i in "aeiou":
#         v+=i
#     else:
#         c+= i
# res=""
#
# if abs(len(v)-len(c))>1:print("Impossible!")
#
# elif len(v)>len(c):
#     for i in range(len(c)):
#         res+= v[i] + c[i]
#     res+=v[-1]
# elif len(c)>len(v):
#     for i in range(len(v)):
#         res+= c[i] + v[i]
#     res += c[-1]
#
# else:
#     for i in range(len(v)):
#         res += c[i] + v[i]
# print(res)



# a=set("ё")
#
# for x in range(ord("а"),ord("а")+32):
#     a.add(chr(x))
#
# print(len(a)==33)
# ten=a
# print(a.difference(a))