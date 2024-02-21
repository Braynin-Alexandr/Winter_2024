import re
#Задача 16-1 (1-е решение)
def abbreviation(string):
    import re
    first_letters = re.findall(r"\b(\w)\w*\b", string) #берем из строки только первые буквы
    return "".join([i.upper() for i in first_letters]) #первые буквы из списка first_letters переводим в верх.регистр и объединяем в одну строку черех join

text = "Институт точной Механики оптики"
print(abbreviation(text))


#Задача 16-1 (2-е решение)
def abbreviation(string):
    import re
    first_letters = re.sub(r"\b(\w)\w*\b", r"\1", string.upper())
    return "".join(re.split(r'\s+', first_letters))

text = "Институт точной механики оптики"
print(abbreviation(text))
print()


#Задача 16-2 (1-е решение)
string="0, 1, 12, 2,45, 46, 100, 1000, 20000"
x=int(input())
res=[]

for i in range(x+1):
    f=re.findall(fr'\b({i})\b', string)
    res.extend(f)

print(", ".join(res))
print()

#Задача 16-2 (2-е решение)

string="0, 30, -5 1, 12, 2,45, 46, 100, 1000, 20000"

num=int(input())
pattern= r'\b|\b'.join([str(x) for x in range(-1,num+1)]) #строка из \b 1 \b | \b 2 \b, т.е. "|" это или 1 или 2 и тд; \b окружает числа, чтобы они не были частью другого числа
pattern+=r'\b'#одной \b не хватает в конеце
print(pattern)
print(", ".join(re.findall(fr'{pattern}', string)))
print()
#Задача 16-3

def decorator(func):
    def wrapper():
        string=func()
        res=string.lower()
        return res
    return wrapper

@decorator
def say_hello():
    return "HELLO, WORLD!"

print(say_hello())