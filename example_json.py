#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json

from box import SBox

MASKS = {
    '姓名': lambda name: '*' * (len(name) - 1) + name[-1],
    '手机': lambda phone: phone[:3] + '*' * 4 + phone[7:],
    '专业': lambda s: '一流专业',
}
with open('data.json', encoding='utf-8') as jsondata:
    ALL = json.load(jsondata)
for data in ALL.values():
    data['Students'] = []
with open('data.csv', encoding='utf-8-sig', newline='') as csvin:
    csvreader = csv.DictReader(csvin)
    for row in csvreader:
        university = row.pop('大学')
        student_fmt = MASKS.get('HTML', lambda s: '')(row.pop('HTML', ''))
        if not student_fmt:
            student_fmt = f'<li class=\\"{row.pop("CSS", "")}\\">'
            student_fmt += f'{MASKS["姓名"](row.pop("姓名"))}<ul>'
            for field, value in row.items():
                if not value:
                    continue
                value = MASKS.get(field, lambda s: '')(value)
                if not value:
                    continue
                student_fmt += f'<li>{field}：{value}</li>'
            student_fmt += '</ul></li>'
        # Need no escape 'cause json would do it
        # Actual value vs written value
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
