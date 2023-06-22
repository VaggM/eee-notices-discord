from bs4 import BeautifulSoup
import requests
import json

from MailSender import MailSender


def main():

    # Email configuration

    sender_email = "vaggtester@gmail.com"  # Your Gmail address
    password = "fyqwmdipdshmlium"  # Your Gmail password

    sender = MailSender(sender_email, password)

    with open('data.json', 'r') as f:
        data = json.load(f)

    url = "https://eee.uniwa.gr/el/anakinoseis/anakoinoseis-grammateias"

    # last_notice = get_last_notice(url)
    #
    # mail_text = get_mail_text(last_notice['url'])
    #
    # if last_notice['title'] != data['last_title']:
    #
    #     data['last_title'] = last_notice['title']
    #     save_data(data)
    #     notify_subscribers(sender, mail_text, data['subscribers'])


def save_data(data):

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)


def notify_subscribers(sender, mail_text, subscribers):

    for mail in subscribers:
        sender.send(mail, mail_text)
        print(f"Mail sent! ( {mail} )")


def get_mail_text(url):

    data = requests.get(url)
    text = data.text
    soup = BeautifulSoup(text, features="html.parser")
    article = soup.find('article')

    a_tags = article.find_all('a')

    for tag in a_tags:
        tag['href'] = eee + tag['href']

    return article


def get_all_new_notices(url, last_title):

    data = requests.get(url)
    text = data.text

    soup = BeautifulSoup(text, features="html.parser")

    article = soup.find('article')

    a = article.find('a')

    title = a.get_text().strip()
    href = eee + a['href']

    notification = {
        'title': title,
        'url': href
    }

    return notification


eee = "https://eee.uniwa.gr"
main()
