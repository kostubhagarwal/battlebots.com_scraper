import csv
import requests
from bs4 import BeautifulSoup

url_1 = "https://battlebots.com/world-championship-vii-robots/"
page_1 = requests.get(url_1)
soup_1 = BeautifulSoup(page_1.content, 'lxml')

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow([','])

    for header in soup_1.find_all('h4', class_='title'):
        team = header.text
        team = team.replace('(', '')
        team = team.replace(')', '')
        team = team.replace(' ', '-')
        team = team.replace('!', '')
        team = team.replace('.', '')
        team = team.strip()

        url_2 = "https://battlebots.com/robot/{}/".format(team)
        page_2 = requests.get(url_2)

        if page_2.status_code == 404:
            continue
        
        else:
            soup_2 = BeautifulSoup(page_2.content, 'lxml')

            items = soup_2.find_all('div', class_='info-grid--item')

            # bot = items[2].h3
            # writer.writerow([bot.text])
            
            # team = items[6].h3
        
            sponsors = items[10]
            for sponsor in sponsors.find_all('a'):
                link = sponsor.get('href')
                writer.writerow([link])

            # website = items[12].h3




