import discord
import os
from keep_alive import keep_alive
client = discord.Client()

@client.event
async def on_ready():
    print('hi dumbass we logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        await message.channel.send('hi')
    if message.content.startswith('st'):
      x = 1
      for x in range(10):
        await message.channel.send('<:st:906280934003863602><:st:906280934003863602><:st:906280934003863602><:st:906280934003863602><:st:906280934003863602><:st:906280934003863602><:st:906280934003863602><:st:906280934003863602><:st:906280934003863602><:st:906280934003863602>')
        x+=1
    if message.content.startswith('ts'):
      x = 1
      for x in range(10):
        await message.channel.send('<:ts:880916580253433906><:ts:880916580253433906><:ts:880916580253433906><:ts:880916580253433906><:ts:880916580253433906><:ts:880916580253433906><:ts:880916580253433906><:ts:880916580253433906><:ts:880916580253433906><:ts:880916580253433906>')
        x+=1

    if message.content.startswith('!'):
          await message.channel.send('go to a bot channel {}'.format(message.author.name))
    if message.content.startswith('?'):
          await message.channel.send('go to a bot channel {}'.format(message.author.name))
    if message.content.startswith(';'):
          await message.channel.send('go to a bot channel {}'.format(message.author.name))
    if message.content.startswith('>'):
          await message.channel.send('go to a bot channel {}'.format(message.author.name))
    if message.content.startswith('g.'):
          await message.channel.send('go to a bot channel {}'.format(message.author.name))
    if message.content.startswith('l:'):
          await message.channel.send('go to a bot channel {}'.format(message.author.name))
    if message.content.startswith('e!'):
          await message.channel.send('go to a bot channel {}'.format(message.author.name))
    if message.content.startswith('&'):
          await message.channel.send('go to a bot channel {}'.format(message.author.name))


keep_alive()
client.run(os.environ['token'])
