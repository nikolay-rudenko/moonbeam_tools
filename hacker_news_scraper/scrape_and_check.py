from urllib import response
import requests
from bs4 import BeautifulSoup
import pprint


class Scrape_Dou(object):

    def link_generator(self):

        url = "https://jobs.dou.ua/vacancies/?category=Python"

        payload = {}

        headers = {
            'content-type': 'application/json',
            'cookie': '',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        print('Python Lead, Global Music Company' in response.text)

        return response.text


scrape = Scrape_Dou()
scrape.link_generator()
