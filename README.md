## EEE-Notice-Discordbot

Simple app to have a discord bot show new announcements 
from the Department of Electrical and Electronics Engineering, UniWA.

**Important!** In folder data you should provide the latest EEE annoucement urls in the file [last_urls.json](./data/last_urls.json),
plus a list of channel ids to send the announcements to in the file [channel_ids.txt](./data/channel_ids.txt). Each id should be in each own line.

If running without docker a .env file should be created containing the DISCORD_BOT token just like [.envsample](./.envsample).

Run container 1st time
```bash
docker run \
-e DISCORD_TOKEN="" \
-v /desired/path:/usr/src/app \
--name notifier \
vaggm/eee-notices-discord:1.0.1
```

Start container after 1st time
```bash
docker start notifier
```
