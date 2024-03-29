print('Задача 9-1. ДНК в РНК')
def do_rnk(a):

    dct={"G":"C", "T":"A","C":"G", "A":"T"}
    res=f"РНК: "

    for x in s:
        if x in dct:
            res+=dct.get(x)
        else: return "Ошибка ввода"
    return res

#GGCTAA
s=input("Ввод ДНК: ").upper()

print(do_rnk(s))
print()

#поросенок, титан, итог, лавка, погост, кино
#Вывод - слова, похожие на питон: титан, погост, кино

print("Задача 9-2.Частотный анализ текста")

letters=("а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е")

s1=input("Первое слово: ").lower()
n=int(input("Кол-во слов: "))

dct1={} #для первого слова
for i, x in enumerate(s1): #создаём словарь для первого слова, где ключ - слово, значения - индексы гласных букв
    if x in letters:
        dct1.setdefault(s1, []).append(i)


dct2={} #для остальных слов
с=0 #счётчик кол-ва слов (n)

for x in range(n):#через цикл добавляём слова в s2
    a=input(f"Введите слово (остальась {n-с} шт.): ").lower()
    for i, y in enumerate(list(a)):
        if y in letters:
            dct2.setdefault(a, []).append(i)
    с+=1

res=[]
for word, values in dct2.items():
    if values == dct1[s1]: #сравниваем значения двух словарей
        res.append(word)

print(f"Похожие слова на {s1.title()}: {', '.join(res).title()}" if res else f"Со словом {s1.title()} cовпадений нет")
print()


#Мама мыла раму
print('Задача 9-3.Частотный анализ текста')
s=input("Ввод текста: ")

dct = {}
for x in s:
    dct[x] = dct.get(x, 0) + 1

sorted_dct = sorted(dct.items(), key=lambda x: (-x[1], x[0])) # в x передаём картеж: x[0] - ключ(буква), -x[1] - значение (кол-во повторений), "-x[1]"  от большего к меньшему

i=0
for x in sorted_dct:
    print(f"\'{x[0]}\' - {x[1]}")
    i+=1
    if i>=10: break
