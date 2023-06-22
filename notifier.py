from bs4 import BeautifulSoup
import requests

def get_all_new_notices(url, last_title):

    eee = "https://eee.uniwa.gr"

    data = requests.get(url)
    text = data.text

    soup = BeautifulSoup(text, features="html.parser")

    article = soup.find('article')
    a = article.find('a')

    title = a.get_text().strip()
    url = eee + a['href']

    notices = []

    while title != last_title:

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

    return notices.reverse()


def send_notices(notices, subscribers):

    print("Sending notices about the following:")

    for notice in notices:
        print(notice['title'])

        mail_text = get_mail_text(notice['url'])
        notify_subscribers(sender, mail_text, subscribers)

    last_title = notices[0]['title']
    return last_title


def notify_subscribers(sender, mail_text, subscribers):

    for mail in subscribers:
        sender.send(mail, mail_text)
        print(f"Mail sent! ( {mail} )\n")


def get_mail_text(url):

    data = requests.get(url)
    text = data.text
    soup = BeautifulSoup(text, features="html.parser")
    article = soup.find('article')
    a_tags = article.find_all('a')

    eee = "https://eee.uniwa.gr"

    for tag in a_tags:
        tag['href'] = eee + tag['href']

    return article
