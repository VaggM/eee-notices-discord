## EEE-Notice-Discordbot

Run container
```bash
docker run \\
-e CHANNEL_ID="desired_channel_id" \\
-e DISCORD_TOKEN="discord_bot_token" \\
--name notifier \\
vaggm/eee-notices-discord:1.0
```

Start container
```bash
docker start notifier
```