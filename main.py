import json

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

sender_email = "vaggtester@gmail.com"  # Your Gmail address
password = "fyqwmdipdshmlium"  # Your Gmail password

sender = MailSender(sender_email, password)

data = get_data()

url = "https://eee.uniwa.gr/el/anakinoseis/anakoinoseis-grammateias"
test_title = "Ανακοίνωση παράτασης εξεταστικής περιόδου"

notices = get_all_new_notices(url, test_title)
data['last_title'] = send_notices(notices, data['subscribers'])
save_data()
