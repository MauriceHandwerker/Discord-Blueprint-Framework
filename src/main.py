import discord
import config

@client.event
async def on_ready():
    print(f'Bot logged in : {client.user}')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith(config.prefix+'ping'):
        await message.channel.send('pong')



client.run(config.token)