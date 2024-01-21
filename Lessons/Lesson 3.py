# lst= [1,2,3,4,5]
# lst2=[]
# summa = 0
# for i,x in enumerate(lst):
#     for y in range(i+1):
#         summa+=lst[y]
#     lst2.append(summa)
# print(lst2)


# lst= [1,2,3,4,5]
# res=[]
#
# for i,x in enumerate(lst):
#     res.append(sum(lst[0:i+1]))
#
# print(res)





# lst=[[1,2,3],[10,20, 30],[100,200,300]]
# res=0
#
# for i, x in enumerate(lst):
#     res+=sum(x)
# print(res)

# for i, subject_1 in enumerate(lst):
#     for subject_2 in subject_1:
#         res+=subject_2
# print(res)



# a="Hello world!"
# # for i in range(-12, 12):
# #     print(a[i], end= "")
#
# print(a.split("e"))





# a=input("Введите строку: ")
# b=a[::-1]

# if a==b:
#     print(True)
# else:
#     print(False)



# lst=input()
#
# for i in range(len(lst)):
#     if lst[i] != lst[-i-1]:
#         print(False)
#         break
# else:
#     print(True)

# res=[]
# n=int(input())
#
# for i in range(1,n+1):
#     for y in range(i):
#         res.append(i)
# print(res)

# res=[]
# lst="abcdefghijklmnopqrstuvwxyz"
# for i in range(len(lst)):
#     for y in range(i+1):
#         res.append(lst[i])
#
# print(*res)
# res=[]
#
# lst="abcdefghijklmnopqrstuvwxyz"
#
# for i,z in enumerate(lst):
#     i+=1
#     print(i*z, end=" ")
#     #res.append(lst[i])
#
# #print(*res)