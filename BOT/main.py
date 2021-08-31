import discord
import requests
import json
import random
import calendar

client = discord.Client()
sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
starter_encouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person!",
  "Why are you sad?",
  "Everything wil get better soon"]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="bot help"))

@client.event
async def on_message(message):
    msg = message.content
    
    if message.author == client.user:
        return

    if msg.startswith('bot help'):
        await message.channel.send(' > **bot inspire**\n get random quotes\n'
                                   ' > **bot "month year"**\n get calendar of that month in that year\n')

    if msg.startswith('bot inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if msg.startswith('bot 2021 10'):
        await message.channel.send('```\n' + calendar.month(2021,10) + '```')


    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

client.run('ODAzMzA3MDMxMjQyMDgwMjc2.YA73-A.QYFzHFxoGUprsF99VKtpTw6W7j8')


