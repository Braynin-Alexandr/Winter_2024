# -*- coding: utf-8 -*-
# Задача 20-1
class Cafe:
    def __init__(self, name, menu):
        self.name=name
        self.menu=menu
        self.income=0

    def get_menu(self):
        for product, price in self.menu.items():
            print(f'{product}: {price} руб.')

    def sell_product(self, consumer, products):
        for product in products:
            if product in self.menu:
                price = self.menu[product]
                if consumer.money>= price:
                    print(f"Продукт '{product}' куплен за {price} руб.")
                    self.income+=price
                    consumer.money -= price
                    consumer.expenses += price
                else:
                    print(f"Не хватает денежных средств")
            else:
                print(f"'{product}' не найден в меню")

    def get_income(self):
        print(f'\'{self.name}\' заработала: {self.income} руб.')

class Consumer:
    def __init__(self, name, money_card, money_cash):
        self.name=name
        self.money_card=money_card
        self.money_cash=money_cash
        self.money=self.money_card+self.money_cash
        self.expenses=0

    def get_cofe_food(self, name_cafe, *products):
        name_cafe.sell_product(self, products)

    def get_expenses(self):
        print(f'{self.name} потратил(а): {self.expenses} руб.')


cafe1=Cafe('Кофейня', {'Американо':100, 'Капучино': 200, 'Пирожок':70})
man1=Consumer('Алексей',500, 100)

man1.get_cofe_food(cafe1,'Американо', 'Пирожок')

cafe1.get_income()
man1.get_expenses()
print()

#Задача 20-2
import pandas as pd
def func(df):
    result=0

    for i in df.index:
        for j in df.columns:
            try:
                check_if_number=float(df.loc[i,j])
                result+= check_if_number
            except ValueError:
                continue

    return f'Cумма всех чисел: {result}'

data = {'A': [1, 2, 'строка 1', 4], 'B': [5, 'строка 2', 7, 8]}
df = pd.DataFrame(data)
print(func(df))
print()

# Задача 20-3
class GenLetterNumbers:
    import itertools
    def __init__(self):
        self.lst=[1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E', 6, 'F', 7, 'G', 8, 'H', 9, 'I', 10,
        'J', 11, 'K', 12, 'L', 13, 'M', 14, 'N', 15, 'O', 16, 'P', 17, 'Q', 18, 'R', 19, 'S', 20,
        'T', 21, 'U', 22, 'V', 23, 'W', 24, 'X', 25, 'Y', 26, 'Z']
        self.generator = itertools.cycle(self.lst)
    def __iter__(self):
        return self
    def __next__(self):
        return next(self.generator)


Gen = GenLetterNumbers()

for x in range(100):
    print(next(Gen), end=", ")