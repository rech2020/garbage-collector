import discord
from discord.ext import commands
import time
from random import randint

bot = commands.Bot(command_prefix='>collector ', self_bot=True)

@bot.event
async def on_ready():
    pass

@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # Check if the message is from a webhook named "Cat bot"
    if message.webhook_id is not None and message.author.display_name.lower() == "cat bot":
        # check if the message doesn't have bot's username
        if not bot.user.name in message.content and "cat" in message.content and "appeared" in message.content:
            # wait a second to make it not so suspiciously good
            time.sleep(randint(1,5))
            await message.channel.send("cat")


@bot.command
async def restart():
    eval("python garbagemain.py")
    exit()

bot.run(open("collectorToken.txt").read())