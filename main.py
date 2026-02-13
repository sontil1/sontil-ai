import discord
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} SUDAH ONLINE!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower() == '!halo':
        await message.channel.send('Halo! Sontil AI sudah bangun!')

client.run(os.getenv('DISCORD_TOKEN'))
