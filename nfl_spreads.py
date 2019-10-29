from bs4 import BeautifulSoup
import urllib.request
import pprint
import sys
from requests_html import HTMLSession
from selenium import webdriver


def print_table(table):
    for row in table.find_all("tr")[1:]:
        info = [cell.get_text(strip=True) for cell in row.find_all("td")]
        if len(info) == 4:
            print(f"Favorite: {info[1]}, Underdog: {info[3]}, Spread: {info[2]}")

html = None
with urllib.request.urlopen('http://www.footballlocks.com/nfl_point_spreads.shtml') as response:
   html = response.read()

soup = BeautifulSoup(html, 'html.parser')
found = soup.find(text="Date & Time")
table1 = found.findPrevious('table')
table2 = found.findAllNext('table')
#table3 = found.findNext('table')
print_table(table1)
for table in table2:
    print_table(table)
