# Задача 15-1
def dct_func(dct,x):
    res=[]
    for k,v in dct.items():
        if k==x and type(v) != dict:
            res.append(v)
        elif type(v)==dict:
            res.extend(dct_func(v,x))
    return res


dct = {1:1, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}}, 1:11,}, 6:22}
print(dct_func(dct,1))
print()


#Задача 15-2
def car_numbers(x):
    import re
    regex = r"\b[АВСЕНКМОРТХ]\d{3}[АВСЕНКМОРТХ][АВСЕНКМОРТХ]\d{2,3}\b"
    res = re.findall(regex, x)
    return f'Номера машин: {", ".join(res)}' if len(res)!=0 else "Номера машин не найдены"

# lst=input()
lst="Номера автомашин А123ВС78 и Х666ХХ178"
print(car_numbers(lst))
print()


# Задача 15-3
def phone_numbers(string):
    import re
    regex=r"\+7\(812\)\d{3}-\d{4}|\+7\(812\)\d{3}-\d{2}-\d{2}|\+7\(921\)\d{3}-\d{4}|\+7\(921\)\d{3}-\d{2}-\d{2}"
    res=re.findall(regex, string)
    if len(res): return f'Найдены телефонные номера: {", ".join(res)}'
    else: "Телефонные номера не найдены"

#s=input()
s="Телефонные номера: №1 +7(812)987-6543, №2 +7(812)987-65-45,№3 +7(921)456-7890 и №4 +7(921)098-76-54"
print(phone_numbers(s))







