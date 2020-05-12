import requests
from bs4 import BeautifulSoup


def my_scraper(site):
    r = requests.get(site).text
    soup = BeautifulSoup(r, 'html.parser')

    strings = []

    match1 = soup.find('div')
    top = list(match1.find_all('a'))
    for i in top:
        i = i.get_text()
        strings.append('\033[34m' + i.strip() + '\033[39m')
    try:
        h1 = soup.find('h1')
        h1 = h1.get_text()
    except Exception as e:
        h1 = ''
    strings.append(h1.strip())

    p = soup.find('p')
    a = p.find('a')
    for a in p.find_all('a'):
        a = a.replace_with('\033[34m' + a.string + '\033[39m')
    p = p.text
    strings.append(p.strip())

    S = soup.find_all('strong')

    b = 0
    for table in soup.find_all('table'):

        strong_p = (S[b].text)
        strings.append(strong_p.strip())

        tr = table.find('tr')
        for tr in table.find_all('tr'):
            td = tr.find('td')
            for td in tr.find_all('td'):
                p = td.find('p')
                for p in td.find_all('p'):
                    a = p.find('a')
                    for a in p.find_all('a'):
                        a = a.replace_with('\033[34m' + a.string + '\033[39m')

                    p = p.text
                    strings.append(p)
        b += 1
    site_content = '\n'.join(strings)
    return site_content

