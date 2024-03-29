print("Задача 4-1. Калькулятор")

while True:
    s = input("Ввод: ").split()
    if "00" in s: #для завершения программы
        print("Завершение программы")
        break
    else:
        dct = dict(n_1 = float(s[0]), n_2=float(s[-1]))

        if "+" in s:
            print(f"Ответ: {dct['n_1'] + dct['n_2']}")
        elif "-" in s:
            print(f"Ответ: {dct['n_1'] - dct['n_2']}")
        elif "*" in s:
            print(f"Ответ: {dct['n_1'] * dct['n_2']}")
        elif "/" in s:
            if dct['n_1']==0 and dct['n_2']==0:
                print("Ошибка")
            elif dct['n_2'] == 0:
                print("Ошибка")
            else:
                print(f"Ответ: {dct['n_1'] / dct['n_2']}")
print()


print("Задача 4-3. Анаграммы")
s_1 = input("Ввод первого предложения: ").lower()
s_2 = input("Ввод второго предложения: ").lower()

dct_1, dct_2 = {},{}

for k,v in enumerate(s_1):#побуквенно проверяем первую строку (предложение)
     if v.isalpha(): #оставляем только буквы
          if v not in dct_1: #проверяем наличие буквы в словаре
               dct_1[v]=0 #добавляем букву в словарь, если её там ещё нет
          dct_1[v]+=1 #увеличиваем значение на 1

for k,v in enumerate(s_2): #то же самое со вторым предложением
     if v.isalpha():
          if v not in dct_2:
               dct_2[v]=0
          dct_2[v]+=1
print(dct_1==dct_2) #сравниваем два словаря, то есть их ключи-значения, независимо от их порядка в словаре
print()


print("Задача 4-3.Анаграммы. Альтернатива")
s=input("Введите предложения, между ними должет быть символ \"#\": ").lower().split("#")
dct_1, dct_2= {}, {}

for k, v in enumerate(s):
     if k==0: #берем первое предложение
          for v_1 in v: #перебираем предложение посимвольно
               if v_1.isalpha(): #оставляем буквы
                    if v_1 not in dct_1: #далее добавляем в словарь
                         dct_1[v_1]=0
                    dct_1[v_1]+=1
     if k==1: #берем второе предложение
          for v_2 in v:
               if v_2.isalpha():
                    if v_2 not in dct_2:
                         dct_2[v_2]=0
                    dct_2[v_2]+=1
print(f"Ответ: {dct_1==dct_2}")