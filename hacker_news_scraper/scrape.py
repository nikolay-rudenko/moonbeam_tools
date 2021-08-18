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


class Scrape_Hacker_News(object):
    def __init__(self, page, votes, quantity):
        self.page = page
        self.votes = votes
        self.quantity = quantity

    def link_generator(self):
        links_list = []
        subtext_list = []
        counter = 1

        while counter < self.quantity:
            page = requests.get(f'https://news.ycombinator.com/news?p={counter}')

            soup = BeautifulSoup(page.text, 'html.parser')
            links = soup.select('.storylink')
            links_list += links

            subtext = soup.select('.subtext')
            subtext_list += subtext

            counter += 1

        return links_list, subtext_list

sc = Scrape_Hacker_News(page=5,votes=300, quantity=3)

pprint.pprint(create_custom_hn(sc.link_generator()[0], sc.link_generator()[1], votes=sc.votes))
