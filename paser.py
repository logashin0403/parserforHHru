import requests
from bs4 import BeautifulSoup as bs

headers = {
    'accept': '*/*',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

base_url = 'https://kazan.hh.ru/search/vacancy?search_period=7&clusters=true&area=88&text=Python&enable_snippets=true'

def hh_purser(base_url, headers):
    jobs = []
    session = requests.Session()
    request = session.get(base_url, headers = headers)
    if request.status_code == 200:
        soup = bs(request.content, 'html.parser')
        divs = soup.find_all('div', attrs = {'data-qa': 'vacancy-serp__vacancy'})
        for div in divs:
            title = div.find('a', attrs = {'data-qa': 'vacancy-serp__vacancy-title'}).text
            href = div.find('a', attrs = {'data-qa': 'vacancy-serp__vacancy-title'})['href']
            company = div.find('a', attrs = {'data-qa': 'vacancy-serp__vacancy-employer'}).text
            text1 = div.find('div', attrs = {'data-qa': 'vacancy-serp__vacancy_snippet_responsibility'}).text
            text2 = div.find('div', attrs = {'data-qa': 'vacancy-serp__vacancy_snippet_requirement'}).text
            allrules = text1 + " " + text2
            jobs.append({
                'title': title,
                'href': href,
                'company': company,
                'allruels': allrules,
            })
            print(jobs)
    else:
        print("You do something wrong")
hh_purser(base_url, headers)
