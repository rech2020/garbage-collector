import discord
from discord.ext import commands
import asyncio
from random import randint, choice

bot = commands.Bot(command_prefix='!', self_bot=True)

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
            await asyncio.sleep(randint(0,5))
            await message.channel.send("cat")
    
    if message.content.startswith('!image'):
        await message.author.send(choice(["consider this as a warning", "do you think even the worst cat can change?"]),
                                  file=discord.File("do_you_think_even_the_worst_person_can_change.png"))
    
    if bot.user.mentioned_in(message):
        print("oh someone pinged")
        if message.author.id == 1073619066272620666:
            commandss = await message.channel.application_commands()
            commands_by_name = {
                cmd.name: cmd
                for cmd in commandss
                if (
                    cmd.application_id == 1073619066272620666
                    and isinstance(cmd, discord.SlashCommand)
                )
            }
            garden = {
                cmd.name: cmd 
                for cmd in commands_by_name["garden"].children
                if (
                    isinstance(cmd, discord.SubCommand)
                )
            }
            print("getting swift package")
            await garden["claim"](message.channel,package="swift")
            print("getting daily package")
            await garden["claim"](message.channel, package="daily")
        return

@bot.command
async def restart(ctx):
    await ctx.reply("perms issue")

@bot.command()
async def image(ctx):
    await ctx.author.send(file=discord.File("do_you_think_even_the_worst_person_can_change.png"))

bot.run(open("collectorToken.txt").read())
