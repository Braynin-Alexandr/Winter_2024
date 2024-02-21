import re
#������ 16-1 (1-� �������)
def abbreviation(string):
    import re
    first_letters = re.findall(r"\b(\w)\w*\b", string) #����� �� ������ ������ ������ �����
    return "".join([i.upper() for i in first_letters]) #������ ����� �� ������ first_letters ��������� � ����.������� � ���������� � ���� ������ ����� join

text = "�������� ������ �������� ������"
print(abbreviation(text))


#������ 16-1 (2-� �������)
def abbreviation(string):
    import re
    first_letters = re.sub(r"\b(\w)\w*\b", r"\1", string.upper())
    return "".join(re.split(r'\s+', first_letters))

text = "�������� ������ �������� ������"
print(abbreviation(text))
print()


#������ 16-2 (1-� �������)
string="0, 1, 12, 2,45, 46, 100, 1000, 20000"
x=int(input())
res=[]

for i in range(x+1):
    f=re.findall(fr'\b({i})\b', string)
    res.extend(f)

print(", ".join(res))
print()

#������ 16-2 (2-� �������)

string="0, 30, -5 1, 12, 2,45, 46, 100, 1000, 20000"

num=int(input())
pattern= r'\b|\b'.join([str(x) for x in range(-1,num+1)]) #������ �� \b 1 \b | \b 2 \b, �.�. "|" ��� ��� 1 ��� 2 � ��; \b �������� �����, ����� ��� �� ���� ������ ������� �����
pattern+=r'\b'#����� \b �� ������� � ������
print(pattern)
print(", ".join(re.findall(fr'{pattern}', string)))
print()
#������ 16-3

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