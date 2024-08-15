#!/bin/bash

docker run -d --name eee_notices --env-file .env -e DISCORD_TOKEN=${DISCORD_TOKEN} -v "$(pwd)"/data:user/src/data vaggm/eee-discord-notifier
