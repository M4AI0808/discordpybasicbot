import discord
import dotenv
import os
client = discord.Client()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

@client.event
async def on_message(message):
    if message.content.startswith('!members'):
        await message.channel.send('There is {guild.member_count} members on serwer.')

@client.event
async def on_message(message):
    if message.content.startswith('!'):
        await message.channel.send('Gracz  dodany/na do whitelist!🍒')
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Cześć witam cię na ciastkowym serwerze! '
    )

client.run(os.getenv('TOKEN'))