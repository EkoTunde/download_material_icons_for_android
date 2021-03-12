import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import datetime
from time import sleep
from random import randint
import os
from os.path import expanduser

home = expanduser("~")
downloads_path= f"{home}/Downloads"

headers = {"Accept-Language": "en-US, en;q=0.5"}
page = requests.get(f"https://github.com/google/material-design-icons/blob/master/android/", headers=headers)
main_soup = BeautifulSoup(page.text, "html.parser")

item_divs = main_soup.find_all('div', class_='Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item')

types_and_names = {}

for item in item_divs:
    _type = item.find('a', class_='js-navigation-open link-gray-dark').text.strip() if item.find('a', class_='js-navigation-open link-gray-dark') else ''
    page = requests.get(f"https://github.com/google/material-design-icons/blob/master/android/{_type}", headers=headers)
    soup = BeautifulSoup(page.text, "html.parser")
    names_divs = soup.find_all('div', class_='Box-row Box-row--focus-gray py-2 d-flex position-relative js-navigation-item')
    names = []
    for item in names_divs:
        name = item.find('a', class_='js-navigation-open link-gray-dark').text.strip() if item.find('a', class_='js-navigation-open link-gray-dark') else ''
        names.append(name)
    types_and_names[_type] = names

for _type, names in types_and_names.items():
    for name in names:
        sleep(randint(1,3))
        url = f"https://github.com/google/material-design-icons/blob/master/android/{_type}/{name}/materialiconsoutlined/black/res/drawable/outline_{name}_24.xml"
        final_page = requests.get(url, headers=headers)
        final_soup = BeautifulSoup(final_page.text, "html.parser")
        tr_lines = final_soup.find_all('tr')
        for line in tr_lines:
            code_line = line.find('td', 'blob-code blob-code-inner js-file-line').text.strip() if final_soup.find('td', 'blob-code blob-code-inner js-file-line') else ''
            dir_path = home+f"/Downloads/ic_{name}.xml"
            with open(dir_path,'a') as f:
                f.write(code_line)