#!/usr/bin/python3

import requests
from datetime import datetime
from lxml import html


# get html tree
page = requests.get("https://www.worldometers.info/coronavirus/country/belgium/")
root = html.fromstring(page.text)

# print belgium stats
date = datetime.today().strftime('%Y-%m-%d')
strongs = root.get_element_by_id(f'newsdate{date}').findall('.//strong')
print(strongs[0].text)
print(strongs[1].text)

