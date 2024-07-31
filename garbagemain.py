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
async def restart(ctx):
    await ctx.reply("perms issue")

@bot.command()
async def image(ctx):
    # Ensure the bot has permissions to send messages
    await ctx.message.channel.set_permissions(bot.user, send_messages=True)
    
    # Open the image file in binary mode
    with open('do_you_think_even_the_worst_person_can_change.png', 'rb') as f:
        image = discord.File(f, filename='do_you_think_even_the_worst_person_can_change.png')
    
    # Send the image to the user who invoked the command
    await ctx.author.send(file=image)

bot.run(open("collectorToken.txt").read())