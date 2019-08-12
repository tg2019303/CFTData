#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json

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
    csvreader = csv.DictReader(csvin)
    for row in csvreader:
        university = row.pop('大学')
        student_fmt = row.pop('HTML', '')
        if not student_fmt:
            student_fmt = f'<li class=\\"{row.pop("CSS", "")}\\">'
            student_fmt += f'{row.pop("姓名")}<ul>'
            for field, value in row.items():
                if value:
                    student_fmt += f'<li>{field}：{value}</li>'
            student_fmt += '</ul></li>'
        print(student_fmt)
        if university in ALL:
            ALL[university]['Students'].append(student_fmt)
        else:
            ALL[university] = {'Students': [student_fmt],
                               'BResult': {}}

with open('data.json', 'w', encoding='utf-8') as jsonout:
    json.dump(ALL, jsonout, ensure_ascii=False, indent=2, sort_keys=True)
