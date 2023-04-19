# This example requires the 'message_content' privileged intents

import os
import discord
from discord.ext import commands
import openai

# Initialize the OpenAI client
openai.api_key = os.environ["OPENAI_TOKEN"]

intents = discord.Intents.default()
intents.members = True  # You need to explicitly set this to access members data

# Create a bot instance with the specified intents
bot = commands.Bot(command_prefix='/', intents=intents)

# Define a function to generate an OpenAI response
async def generate_response(message):
    # Use OpenAI to generate a response
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message.content,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Send the response back to the user
    await message.channel.send(response.choices[0].text)

# Set up a message listener
@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Generate a response using OpenAI
    await generate_response(message)




bot.run(os.environ["DISCORD_TOKEN"])
