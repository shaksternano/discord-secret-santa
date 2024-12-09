#!/usr/bin/env python3

import json
import random

import discord

with open("config.json") as file:
    config: dict = json.load(file)

token: str = config["discord_token"]
participants: list[dict] = config["participants"]
random.shuffle(participants)

intents = discord.Intents().none()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    try:
        for i in range(len(participants)):
            participant = participants[i]
            if i < len(participants) - 1:
                recipient = participants[i + 1]
            else:
                recipient = participants[0]

            sender_name = participant["name"]
            sender_id = participant["discord_id"]
            sender = await client.fetch_user(sender_id)

            recipient_name = participant["name"]
            recipient_id = recipient["discord_id"]

            message = f"Hello {sender_name}, you are <@{recipient_id}> ({recipient_name})'s secret santa!"
            await sender.send(message)
    finally:
        await client.close()


client.run(token)
