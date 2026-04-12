#!/bin/bash

echo "BACKEND"
cd ~/BackEnd || exit 1
nohup python3 BackServer.py > backend.log 2>&1 &

echo "Starting FRONTEND"
cd ~/FrontEnd || exit 1
nohup python3 FrontServer.py > frontend.log 2>&1 &

echo "Starting DISCORDBOT"
cd ~/DiscordBot || exit 1
nohup /home/rocky/DiscordBot/.venv/bin/python Bot.py > bot.log 2>&1 &

echo "Done."
echo "BackEnd log:   ~/BackEnd/backend.log"
echo "FrontEnd log:  ~/FrontEnd/frontend.log"
echo "DiscordBot log: ~/DiscordBot/bot.log"