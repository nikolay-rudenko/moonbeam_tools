import requests
from bs4 import BeautifulSoup
import pprint


def sort_story_by_votes(hnlist):
    return sorted(hnlist, key= lambda k: k['votes'], reverse=True)

def create_custom_hn(pages):
    hn = []
    for page in pages:
        soup = BeautifulSoup(page.text, 'html.parser')
        links = soup.select('.storylink')
        subtext = soup.select('.subtext')

        for idx, item in enumerate(links):
            title = links[idx].getText()
            href = links[idx].get('href', None)
            vote = subtext[idx].select('.score')

            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points > 400:
                    hn.append({'title': title, 'link': href, 'votes': points})
        return sort_story_by_votes(hn)


def check_pages(quantity):
    pages = []

    for page in range(1, quantity + 1):
        pages.append(requests.get(f'https://news.ycombinator.com/news?p={quantity}'))

    return pages

for page_num in range(1,3):
    print(f'Page #{page_num} --------------------------------------------------------------------------------------')
    if len(create_custom_hn(check_pages(page_num))) > 0:
        pprint.pprint(create_custom_hn(check_pages(page_num)))








