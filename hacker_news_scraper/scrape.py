import requests
from bs4 import BeautifulSoup
import pprint

def sort_story_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext, votes=100):
    hn = []

    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > votes:
                hn.append({'title': title, 'subtext': href, 'votes': points})

    return sort_story_by_votes(hn)


def link_generator(quantity):
    links_list = []
    subtext_list = []
    counter = 1

    while counter < quantity:
        page = requests.get(f'https://news.ycombinator.com/news?p={counter}')

        soup = BeautifulSoup(page.text, 'html.parser')
        links = soup.select('.storylink')
        links_list += links

        subtext = soup.select('.subtext')
        subtext_list += subtext

        counter += 1

    return links_list, subtext_list


class Scrape_Hacker_News(object):
    def __init__(self, page, votes):
        self.page = page
        self.votes = votes


pprint.pprint(create_custom_hn(link_generator(3)[0], link_generator(3)[1], votes=500))
