# -*- coding: utf-8 -*-

from time import time
from openpyxl import load_workbook, Workbook
from collections import Counter
from pprint import pprint

def get_test_mark(pupil_answers):
    test_points_marks={6:2,11:3,15:4}
    for test_point, mark in test_points_marks.items():
        if sum(pupil_answers)<=test_point: return mark
    else: return 5

def count_marks(marks):
    test_marks=Counter([mark[0] for mark in marks.values()])
    quarter_3_marks=Counter([mark[1] for mark in marks.values()])
    return test_marks, quarter_3_marks

def count_good_bad_marks(marks):
    good_marks, bad_marks = (marks[4]+marks[5]), (marks[2]+marks[3])
    return good_marks, bad_marks

def get_quality(marks):
    pass


pupils_all_info = {}
pupils_test_answers=[]
pupil_absent=0

wb=load_workbook('Форма.xlsx')
ws=wb.active

for row in range(2, ws.max_row+1):
    pupil_name=ws.cell(row, 1).value
    pupil_answers = []
    for column in range(2, ws.max_column):
        answer = ws.cell(row, column).value
        if answer == 'отсутствовал':
            pupil_absent+=1
            break
        else:
            if answer is not None: pupil_answers.append(answer)
    else:
        pupils_test_answers.append(pupil_answers)
        pupil_test_mark=get_test_mark(pupil_answers)
        pupil_quarter_3_mark=ws.cell(row, ws.max_column).value
        pupils_all_info[pupil_name] = (pupil_test_mark, pupil_quarter_3_mark)
wb.save('Форма.xlsx')

count_test_marks, count_quarter_3_marks = count_marks(pupils_all_info)

test_good_marks, test_bad_marks = count_good_bad_marks(count_test_marks)

quarter_3_good_marks, quarter_3_bad_marks = count_good_bad_marks(count_quarter_3_marks)

print(quarter_3_good_marks)
