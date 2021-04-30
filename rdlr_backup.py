import discord
import os
import requests
import json

client = discord.Client()

def get_help():
    response = requests.get("https://dc.fandom.com/wiki/DC_Comics_Database")
    json_data = json.load(response.text)
    result = json_data[0]['q']

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event 
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('-rl'):
        await message.channel.send('Hello! Add content behind the command')
    
client.run(os.getenv('token'))
