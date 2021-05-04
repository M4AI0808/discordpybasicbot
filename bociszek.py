import discord
import dotenv
import os
client = discord.Client()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged as {0}!'.format(self.user))



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!love'):
        await message.channel.send('🍒')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name} welcome to our server! '
    )
@client.event
async def send_dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    await channel.send(content)



client.run(os.getenv('TOKEN'))