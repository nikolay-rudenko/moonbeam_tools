import requests
from bs4 import BeautifulSoup
import pprint

page = requests.get('https://news.ycombinator.com/news?p=1')
soup = BeautifulSoup(page.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')

page1 = requests.get('https://news.ycombinator.com/news?p=2')
soup1 = BeautifulSoup(page1.text, 'html.parser')
links1 = soup1.select('.storylink')
subtext1 = soup1.select('.subtext')

slink = links + links1
ssubtext = subtext + subtext1


def sort_story_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []

    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')

        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 100:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_story_by_votes(hn)


pprint.pprint(create_custom_hn(slink, ssubtext))
