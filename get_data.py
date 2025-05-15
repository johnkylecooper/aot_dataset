import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

base_url = 'https://attackontitan.fandom.com'
URL = f'{base_url}/wiki/Scout_Regiment_(Anime)'
response = requests.get(URL)
html_data = response.text

soup = BeautifulSoup(html_data, "html.parser")
military_member_links = soup.find_all(class_='military-members')

military_member_pages = []
for link in military_member_links:
    for aref in link.find_all('a'):
        military_member_pages.append(aref['href'])

for page in military_member_pages:

    military_member_page = ('').join([base_url, page])
    military_member_name = military_member_page.split('/')[-1]

    path_to_file = os.path.join('military_member_data', f'{military_member_name}.csv')
    if not os.path.exists(path_to_file):

        military_member_html = requests.get(military_member_page).text
        military_member_soup = BeautifulSoup(military_member_html, "html.parser")

        labels = [label.text for label in military_member_soup.find_all(class_='pi-data-label')]
        values = [value.text for value in military_member_soup.find_all(class_='pi-data-value')]

        df = pd.DataFrame(data=values, index=labels)
        df.to_csv(path_to_file)
    
    else:
        print(f'File already created for {military_member_name}. Skipping ...')