# def su(x, y):
#     res=x+y
#     return res
# print(su(10, 20))
#
#
# def name(x):
#     return x**2
# print(name(5))



# def tax(dohod, n13=13, n15=15):
#     if dohod<5000000:
#         pod_nalog = dohod * n13 / 100
#         # return pod_nalog
#     else:
#         d5 = dohod - 5000000
#         pod_nalog= d5 * n15/100 + 5000000 * n13/100
#         return pod_nalog
#
# while True:
#     x=float(input("Введите доход: "))
#     if x==0:break
    # else:print(f"{x}: {tax(x)}")



# def su(*args):
#     prod = 1
#
#     for x in args:
#         prod*=x
#     return prod
#
# print(su(1,2,3,4,5))


# создаёт словарь
# def xyz(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#
# print((xyz(x=10, y=20)))


# def xyz(**kwargs):
    # res1= 1
    # res2=""
    # for k in kwargs:
    #     v=kwargs[k]
    #
    # if type(v) == int:
    #         res1*=v
    # elif type(v) == str:
    #         res2+=v
    # return res1, res2


# print(xyz(a=123, b="xxx"))


# def uni_let(lst):
#     res=set()
#
#     for word in lst:
#         res=res.union(set(list(word)))
#     result=" ".join(sorted(res))
#     return result, len(result)
#
# print(uni_let(["all", "your","need", 'is', 'love']))
# print(uni_let["all", "your"])


for x in zip(["1","2","3"],[1,2,3,4]):
    print(x)

# print(list(zip(["1","2","3"],[1,2,3,4]))