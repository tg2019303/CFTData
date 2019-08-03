#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from box import SBox

with open('data.json', encoding='utf-8') as jsondata:
    DATA = json.load(jsondata)

ALL = list()
for university, data in DATA.items():
    print(data)
    # No need to fucking escape
    data = SBox(data)
    result = data.BResult.results
    try:
        telephone = result.telephone
    except:
        telephone = ''
    ALL.append({'University': university,
                'Students': data.Students,
                'Address': result.address,
                'Telephone': telephone,
                'Lat': result.location.lat,
                'Lng': result.location.lng})
s = json.dumps(ALL, ensure_ascii=False, sort_keys=True)
with open('release.json', 'w', encoding='utf-8') as jsonout:
    jsonout.write("data = 'universities = " + s + "'")
