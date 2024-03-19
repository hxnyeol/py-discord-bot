# Bot: hanyeol
import os
from profanity_check import predict_prob
import discord
import time

# global_variables
__secret_token = os.getenv('DISCORD_PRIKEY')
intent = discord.Intents.default()
intent.messages = True
intent.members = True
intent.message_content = True



client = discord.Client(intents=intent)

hello_messages = ['rohoe', 'rohoelita']


# add person's ID here
peepul = []


@client.event
async def on_ready():
    print(f'I am here to bully you {client.user} (ID: {client.user.id})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.author.id in peepul:
        response = await message.channel.send('hi ~_~')
    
    # response = await message.channel.send(message.content)
    # print("content", response)
    if message.content.lower() in hello_messages:
        response = await message.channel.send('haiiii')
        time.sleep(1)
        await response.delete()
        

    if predict_prob([message.content])[0] > 0.85:
        response = await message.channel.send('no! meow~')
        await message.delete()
        await response.delete()
        

        
client.run(__secret_token)


