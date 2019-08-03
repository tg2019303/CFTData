#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import re
from time import sleep

import requests

from config import AK

# from box import SBox

PATTERN = re.compile(r'(\{.*\})', re.DOTALL)
ALL = dict()


with open('data.json', encoding='utf-8') as jsondata:
    ALL = json.load(jsondata)

for university, data in ALL.items():
    if data['BResult'] and data['BResult']['status'] == 0:
        continue
    param = {
        'query': university,
        'tag': '高等院校',
        'region': '全国',
        'output': 'json',
        'page_size': 1,
        'ak': AK
    }
    r = requests.get(f'http://api.map.baidu.com/place/v2/search', params=param)
    print(university)
    print(r.text)
    BResult = json.loads(PATTERN.findall(r.text)[0])
    if BResult['status'] == 0:
        results = BResult['results']
        if not results:
            BResult['status'] = 1
        else:
            BResult['results'] = BResult['results'][0]
    data['BResult'] = BResult
    sleep(0.5)


with open('data.json', 'w', encoding='utf-8') as jsonout:
    json.dump(ALL, jsonout, ensure_ascii=False, indent=2, sort_keys=True)
