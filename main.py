import json

from dotenv import dotenv_values

from MailSender import MailSender
from notifier import get_all_new_notices, send_notices


def save_data():

    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)


def get_data():

    with open('data.json', 'r') as f:
        json_data = json.load(f)

    return json_data


# Email configuration
env_vars = dotenv_values('.env')
sender_email = env_vars['EMAIL']
password = env_vars['PASSWORD']

sender = MailSender(sender_email, password)

data = get_data()

url = "https://eee.uniwa.gr/el/anakinoseis/anakoinoseis-grammateias"
last_title = data['last_title']
print(f"Checking for any new notices after: {last_title}")
notices = get_all_new_notices(url, last_title)

if len(notices) > 0:
    notices.reverse()
    data['last_title'] = send_notices(sender, notices, data['subscribers'])
else:
    print("None were found.")

save_data()
print("Program finished successfully!")
