#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@since 2020-08-24 17:34:18
@author: hakuna_matata
@email: echo "eWFuamluYmluQHFxLmNvbQo=" | base64 -d
"""

import re
import urllib.request
from bs4 import BeautifulSoup
import os
import csv
import time


def spider(url):
    resp = urllib.request.urlopen(url)
    soup = BeautifulSoup(resp, features='html.parser')
    ctx = soup.find_all("table", "problems")[0].find_all("tr")
    for row in ctx:
        item = row.find_all('td')
        try:
            # get the problem id
            id = item[0].find('a').string.strip()
            l = len(id)
            p2 = id[l-1:l]
            # 处理目前赛制题目命名的问题
            if p2.isalpha():
                p1 = id[0:l - 1]
                p2 = id[l - 1:l]
            else:
                p1 = id[0:l - 2]
                p2 = id[l - 2:l]
            link = f'https://codeforces.com/problemset/problem/{p1}/{p2}'
            col2 = item[1].find_all('a')
            title = col2[0].string.strip()
            tags = [foo.string.strip() for foo in col2[1:]]
            score = item[3].find('span').string.strip()
            solved = re.findall('x(\d+)', str(item[4].find('a')))[0]
            codeforces[id] = {'title': title, 'tags': tags, 'score': score, 'solved': solved, 'accepted': 0,
                              "link": link}
            print(codeforces[id])
        except:
            pass


codeforces = {}
wait =3  # wait time to avoid the blocking of spider
last_page = 53  # the total page number of problem set page
url = ['https://codeforces.com/problemset/page/%d' % page for page in range(1, last_page + 1)]
for foo in url:
    print('Processing URL %s' % foo)
    spider(foo)
    print('Wait %f seconds' % wait)
    time.sleep(wait)


#%% mark the accepted problems
# def accepted(url):
#     response = urllib.request.urlopen(url)
#     soup = BeautifulSoup(response.read())
#     pattern = {'name':'table', 'class':'status-frame-datatable'}
#     table = soup.findAll(**pattern)[0]
#     pattern = {'name': 'tr'}
#     content = table.findAll(**pattern)
#     for row in content:
#         try:
#             item = row.findAll('td')
#             # check whether this problem is solved
#             if 'Accepted' in str(row):
#                 id = item[3].find('a').string.split('-')[0].strip()
#                 codeforces[id]['accepted'] = 1
#         except:
#             continue
#     return soup
#
# wait = 15 # wait time to avoid the blocking of spider
# last_page = 10 # the total page number of user submission
# # ⭐
# handle = 'Greenwicher' # please input your handle
# url = ['https://codeforces.com/submissions/%s/page/%d' % (handle, page) for page in range(1, last_page+1)]
# for foo in url:
#     print('Processing URL %s' % foo)
#     accepted(foo)
#     print('Wait %f seconds' % wait)
#     time.sleep(wait)


root = os.getcwd()
with open(os.path.join(root, "CodeForces-ProblemSet.csv"), "w", encoding="utf-8") as f_out:
    f_csv = csv.writer(f_out)
    f_csv.writerow(['ID', 'Title', 'Tags', 'Score', 'Solved', 'Accepted', 'Link'])
    for id in codeforces:
        title = codeforces[id]['title']
        tags = ', '.join(codeforces[id]['tags'])
        score = codeforces[id]['score']
        solved = codeforces[id]['solved']
        accepted = codeforces[id]['accepted']
        link = codeforces[id]['link']
        f_csv.writerow([id, title, tags, score, solved, accepted, link])
    f_out.close()


# 分析题型

# a-f  tag  freq
# a-f tag submission