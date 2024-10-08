# bot.py
import os
import json
import discord
from dotenv import load_dotenv
from notifier import get_all_new_notices


def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    channels_file = "./data/channel_ids.txt"
    with open(channels_file, 'r') as f:
        channel_ids = f.readlines()

    # Define intents
    intents = discord.Intents.default()
    intents.messages = True  # Enable the ability to receive message events

    # Initialize a Discord client with intents
    client = discord.Client(intents=intents)

    # Function to send the message
    async def send_message():
        channels = [client.get_channel(int(CHANNEL_ID)) for CHANNEL_ID in channel_ids]

        if channels:
            await message_sending(channels)
        else:
            print("No channels found.")

    # Event handler for when the bot is ready
    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')
        await send_message()
        await client.close()  # Close the bot after sending the message

    # Run the client with your bot token
    client.run(TOKEN)


async def message_sending(channels):

    announce_grammateia = "https://eee.uniwa.gr/el/anakinoseis/anakoinoseis-grammateias"
    announce_mathimaton = "https://eee.uniwa.gr/el/anakinoseis/anakoinoseis-mathimaton"
    announce_ekdiloseis = "https://eee.uniwa.gr/el/anakinoseis/ekdilwseis"

    filename = "./data/last_urls.json"
    with open(filename,'r') as f:
        last_urls = json.load(f)

    notices_grammateia = get_all_new_notices(announce_grammateia, last_urls['grammateia'])
    if notices_grammateia:
        last_urls['grammateia'] = notices_grammateia[0]['url']

    notices_mathimaton = get_all_new_notices(announce_mathimaton, last_urls['mathimaton'])
    if notices_mathimaton:
        last_urls['mathimaton'] = notices_mathimaton[0]['url']

    notices_ekdiloseis = get_all_new_notices(announce_ekdiloseis, last_urls['ekdiloseis'])
    if notices_ekdiloseis:
        last_urls['ekdiloseis'] = notices_ekdiloseis[0]['url']

    with open(filename,'w') as f:
        f.write(json.dumps(last_urls, indent=4))

    notices = []
    notices.extend(notices_grammateia)
    notices.extend(notices_mathimaton)
    notices.extend(notices_ekdiloseis)

    print(channels)

    for channel in channels:

        print(f"Sending message to channel {channel}")

        msg = "@everyone\n"

        msg1 = create_message(notices_grammateia, "γραμματείας")
        msg2 = create_message(notices_mathimaton, "μαθημάτων")
        msg3 = create_message(notices_ekdiloseis, "εκδηλώσεων")

        if msg1 or msg2 or msg3:
            msg += msg1 + msg2 + msg3
            await channel.send(msg)



def create_message(notices, nickname):

    message = ""

    if notices:

            notice_num = len(notices)

            message = "## HHM - "

            if notice_num == 1:
                message += " 1 νέα ανακοίνωση "
            else:
                message += f" {notice_num} νέες ανακοινώσεις "

            message += f"{nickname}\n\n"

            for notice in notices[:-1]:
                message += f"> {notice['title']}\n> {notice['url']}\n> \n"
            
            message += f"> {notices[-1]['title']}\n> {notices[-1]['url']} \n" 

    return message


if __name__ == "__main__":
    main()
