# #������ 14-1
def count_num(number, count=0):
    number = str(number)
    if len(number)>0:
        return count_num(number[1:], count+1)
    else:
        return f'���������� ����: {count}'


number=int(input("�������� ���������� ���� ���������� ������ ����� n (n>=0): "))
print(count_num(number))
print()


# #������ 14-2
class NotNaturalNumberError(Exception):
    pass
def check_natural_number(x):
    if x<=0: raise NotNaturalNumberError(x)

def sum_nat_num(n):

    try:
        check_natural_number(n)

    except NotNaturalNumberError as e:
        return f"������, {e} �� �������� ����������� ������"

    else:
        if n==1: return 1
        else:
            return n + sum_nat_num(n-1)


number=int(input("�������� ����� ���� ������������ �����: "))
print(sum_nat_num(number))
print()



# ������ 14-3
def tri_2(n):
    if n==1:
        print("*")
        return
    else:
        print("*"*n)
        tri_2(n-1)
        print("*"* n)

tri_2(int(input("������� �����, ����� ���������� ��� ������������: ")))