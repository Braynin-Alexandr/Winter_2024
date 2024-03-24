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


def get_quality(marks):
    good_marks, bad_marks = (marks[4] + marks[5]), (marks[2] + marks[3])
    return round((good_marks / (good_marks+bad_marks))* 100)


def get_school_performance(count_marks):
    performance_marks = 0
    for mark in range(3, 6): performance_marks+=count_marks.get(mark, 0)
    count_all_marks=sum(count_marks.values())
    return round((performance_marks / count_all_marks)* 100)


def get_avarage_mark(count_marks):
    sum_marks=sum([mark*count for mark, count in count_marks.items()])
    all_marks=sum(count_marks.values())
    return round(sum_marks/all_marks)

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
test_quality = get_quality(count_test_marks)
quarter_3_quality = get_quality(count_quarter_3_marks)
test_performance = get_school_performance(count_test_marks)
quarter_3_performance = get_school_performance(count_quarter_3_marks)
test_avarage_mark=get_avarage_mark(count_test_marks)
quarter_3_avarage_mark=get_avarage_mark(count_quarter_3_marks)
