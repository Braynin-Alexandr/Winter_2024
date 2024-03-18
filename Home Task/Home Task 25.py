# -*- coding: utf-8 -*-
#Задача 25-1
import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QPushButton
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Задача 25-1')
        self.count = 0
        self.button=QPushButton(str(self.count))
        self.button.clicked.connect(self.the_button_was_clicked)
        self.setCentralWidget(self.button)
        self.button.setEnabled(True)

    def the_button_was_clicked(self):
        self.count+=1
        self.button.setText(str(self.count))


app = QApplication(sys.argv)
window =  MainWindow()
window.show()
app.exec()


#Задача 25-2
def is_palindrome(s):
    if type(s) != str: return 'Ошибка'

    if len(s)==1 or len(s)==0: return True
    else:
        if s[0] == s[-1]: return is_palindrome(s[1:-1])
        else: return False

# s='ффавфф'
s=input('Введите строку: ')
print(is_palindrome(s))


#Задача 25-3
def CamelStyle(string):
    if type(string) != str: return 'Ошибка'

    res = ''
    for s in string.split(): res += s.title()
    return res

s=input('Введите строку:' )
# s='camel case woRd'
print(CamelStyle(s))


