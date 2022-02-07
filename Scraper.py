import requests
from bs4 import BeautifulSoup
import csv

def data_call():
    # the url to open the website
    url = "https://www.worldometers.info/coronavirus"
    page_info = requests.get(url)

    soup = BeautifulSoup(page_info.content, 'html.parser')
    table = soup.find('table', attrs={'id': 'main_table_countries_today'})

    rows = table.find_all("tr", attrs={"style": ""})
    data = []
    for i, item in enumerate(rows):
        if i == 0:
            data.append(item.text.strip().split("\n")[:13])
            with open("covid-19-results1.csv", "w", encoding='utf-8') as file:
                writer = csv.writer(file)
                rows = table.find_all("tr")
                for row in rows:
                    csv_row = []
                    for cell in row.findAll(['td', 'th']):
                        csv_row.append(cell.get_text())
                    writer.writerow((csv_row))
        else:
            data.append(item.text.strip().split("\n")[:12])
            # print(data)

data_call()
