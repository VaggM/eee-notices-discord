# bot.py
import os
import json
import discord
import asyncio
from dotenv import load_dotenv
from notifier import get_all_new_notices


def main():
    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')
    CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

    # Define intents
    intents = discord.Intents.default()
    intents.messages = True  # Enable the ability to receive message events

    # Initialize a Discord client with intents
    client = discord.Client(intents=intents)

    # Function to send the message
    async def send_message():
        # Replace 'CHANNEL_ID' with the ID of the channel you want to send the message to
        channel = client.get_channel(CHANNEL_ID)

        if channel:
            # Replace 'YOUR_MESSAGE_HERE' with the message you want to send
            await message_sending(channel)

        else:
            print("Channel not found.")

    # Event handler for when the bot is ready
    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')
        await send_message()
        await client.close()  # Close the bot after sending the message

    # Run the client with your bot token
    client.run(TOKEN)


async def message_sending(channel):

    announce_grammateia = "https://eee.uniwa.gr/el/anakinoseis/anakoinoseis-grammateias"
    announce_mathimaton = "https://eee.uniwa.gr/el/anakinoseis/anakoinoseis-mathimaton"
    announce_ekdiloseis = "https://eee.uniwa.gr/el/anakinoseis/ekdilwseis"

    filename = "last_urls.json"
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

    await send_message(channel, notices_grammateia, "γραμματείας")
    await asyncio.sleep(60)
    await send_message(channel, notices_mathimaton, "μαθημάτων")
    await asyncio.sleep(60)
    await send_message(channel, notices_grammateia, "εκδηλώσεων")



async def send_message(channel, notices, nickname):

    if notices:

            notice_num = len(notices)

            message = "@everyone"

            if notice_num == 1:
                message += " 1 νέα ανακοίνωση "
            else:
                message += f" {notice_num} νέες ανακοινώσεις "

            message += f"{nickname}\n\n>>> "

            for notice in notices:
                message += f"**{notice['title']}**\n{notice['url']}\n\n"

            await channel.send(message)


if __name__ == "__main__":
    main()
