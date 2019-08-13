#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re


def student_escape(student):
    student = re.sub(r'(\d{3})\d{4}(\d{4})', r'\g<1>****\g<2>', student)
    student = re.sub(r'<li>专业：.*?</li>', r'<li>专业：一流专业</li>', student)
    try:
        i = next(re.finditer(r'>([\u4e00-\u9fa5]{2,4})<', student))
        student = student[:i.start()+1]+'*'*(len(i.group(1))-1) + \
            i.group(1)[-1]+student[i.end()-1:]
    except StopIteration:
        pass
    print(student)
    return student


with open('release.json', encoding='utf-8') as jsondata:
    data = jsondata.read()[len("data = 'universities = "):-1]
    print(data)
    ALL = json.loads(data)
for data in ALL:
    data['Students'] = [student_escape(s) for s in data['Students']]
s = json.dumps(ALL, ensure_ascii=False, sort_keys=True, indent=4)
with open('dataExample.js', 'w', encoding='utf-8', newline='\n') as jsonout:
    jsonout.write("universities = " + s + ';\ntestGuest();')
