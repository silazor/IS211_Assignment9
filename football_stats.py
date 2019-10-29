from bs4 import BeautifulSoup
import urllib.request
import pprint
import sys
from requests_html import HTMLSession
from selenium import webdriver

html = None
with urllib.request.urlopen('http://www.cbssports.com/nfl/stats') as response:
   html = response.read()

soup = BeautifulSoup(html, 'lxml')
tags = soup.find_all('a')
t_url = None
for tag in tags:
    if tag.get('href') == '/nfl/stats/playersort/nfl/year-2019-season-regular-category-touchdowns':
        t_url = "http://www.cbssports.com" + tag.get('href')

with urllib.request.urlopen(t_url) as t_response:
    t_link = t_response.read()
    t_soup = BeautifulSoup(t_link, 'lxml')
    table = t_soup.find("table", { "class" : "data"})
    # print 20 rows that have 19 elements
    cnt = 1
    for tr in table.findAll("tr"):
        td = tr.findAll("td")
        row = [i.text for i in td]
        if cnt < 21  and len(row)==19:
            print(f"{cnt}\t{row[0]}\t{row[1]}\t{row[2]}\t{row[6]}")
            cnt+=1
