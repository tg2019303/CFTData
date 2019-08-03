#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json

from box import SBox

FIELDS = ['专业：', '电话：']
with open('data.json', encoding='utf-8') as jsondata:
    ALL = json.load(jsondata)
for data in ALL.values():
    data['Students'] = []
with open('data.csv', encoding='utf-8-sig', newline='') as csvin:
    csvreader = csv.reader(csvin)
    for row in csvreader:
        name, university, major, phone, class_, _ = row
        name = '*' * (len(name) - 1) + name[-1]
        if phone:
            phone = phone[:3] + '*' * 4 + phone[7:]
        # Need no escape 'cause json would do it
        # Actual value vs written value
        student_fmt = f'<li class="{class_}">' if class_ else '<li>'
        student_fmt += f'{name}<ul>'
        for field, value in zip(FIELDS, ('一流专业', phone)):
            if value:
                student_fmt += f'<li>{field}{value}</li>'
        student_fmt += '</ul></li>'
        print(student_fmt)
        if university in ALL:
            ALL[university]['Students'].append(student_fmt)
        else:
            ALL[university] = {'Students': [student_fmt],
                               'BResult': {}}
OUT = []
print(ALL)
for university, data in ALL.items():
    data = SBox(data)
    result = data.BResult.results
    try:
        telephone = result.telephone
    except:
        telephone = ''
    OUT.append({'University': university,
                'Students': data.Students,
                'Address': result.address,
                'Telephone': telephone,
                'Lat': result.location.lat,
                'Lng': result.location.lng})
s = json.dumps(OUT, ensure_ascii=False, sort_keys=True, indent=4)
with open('dataExample.js', 'w', encoding='utf-8', newline='\n') as jsonout:
    jsonout.write("universities = " + s + ';\ntestGuest();')
