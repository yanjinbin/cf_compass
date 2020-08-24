#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import urllib.request
from bs4 import BeautifulSoup
import os
import csv
import time

id = "1347F1"

l = len(id)
h2 = id[l-1:l]
if h2.isalpha():
    h1 = id[0:l - 1]
    h2 = id[l - 1:l]
else:
    h1 = id[0:l - 2]
    h2 = id[l - 2:l]
link = f'https://codeforces.com/problemset/problem/{h1}/{h2}'
print(link)


regular_v1 = re.findall('(?i)[A-Z][0-9]*',"1Af1G2")
print(regular_v1)
