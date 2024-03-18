## EEE-Notice-Discordbot

Simple app to have a discord bot show new announcements 
from the Department of Electrical and Electronics Engineering, UniWA.

Run container
```bash
docker run \
-e DISCORD_TOKEN="" \
-e CHANNEL_ID="" \
--name notifier \
vaggm/eee-notices-discord:1.0
```

Start container
```bash
docker start notifier
```
