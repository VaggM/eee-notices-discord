from bs4 import BeautifulSoup
import requests

def get_all_new_notices(announcements, last_url):

    data = requests.get(announcements)
    text = data.text

    soup = BeautifulSoup(text, features="html.parser")

    article = soup.find('article')
    a = article.find('a')

    title = a.get_text().strip()

    eee = "https://eee.uniwa.gr"
    url = eee + a['href']

    notices = []

    while url != last_url:

        notices.append(
            {
                'title': title,
                'url': url
            }
        )

        article = article.find_next('article')
        a = article.find('a')

        title = a.get_text().strip()
        url = eee + a['href']

    return notices
