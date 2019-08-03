#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json

FIELDS = ['专业：', '电话：']
try:
    with open('data.json', encoding='utf-8') as jsondata:
        ALL = json.load(jsondata)
    for data in ALL.values():
        data['Students'] = []
except FileNotFoundError:
    ALL = {}
# If newline='' is not specified, newlines embedded inside quoted fields
# will not be interpreted correctly, and on platforms that use \r\n
# linendings on write an extra \r will be added. It should always be safe
# to specify newline='', since the csv module does its own (universal)
# newline handling.
with open('data.csv', encoding='utf-8-sig', newline='') as csvin:
    csvreader = csv.reader(csvin)
    for row in csvreader:
        name, university, *info, class_, student_fmt = row
        if not student_fmt:
            student_fmt = f'<li class=\\"{class_}\\">' if class_ else '<li>'
            student_fmt += f'{name}<ul>'
            for field, value in zip(FIELDS, info):
                if value:
                    student_fmt += f'<li>{field}{value}</li>'
            student_fmt += '</ul></li>'
        print(student_fmt)
        if university in ALL:
            ALL[university]['Students'].append(student_fmt)
        else:
            ALL[university] = {'Students': [student_fmt],
                               'BResult': {}}

with open('data.json', 'w', encoding='utf-8') as jsonout:
    json.dump(ALL, jsonout, ensure_ascii=False, indent=2, sort_keys=True)
