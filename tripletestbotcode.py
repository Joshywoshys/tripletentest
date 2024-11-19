import nest_asyncio
import discord
from discord.ext import commands
import os

# this line of code applies nest_asyncio to allow async code to run
nest_asyncio.apply()

# this lines of code set up intents (to track member joins)
intents = discord.Intents.default()
intents.members = True

# this line of codeCreate the bot object
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.event
async def on_member_join(member):
    # this line of code finds the welcome channel
    channel = discord.utils.get(member.guild.text_channels,
                                name='welcome-channel')
    if channel:
        await channel.send(
            f'Hello, {member.mention}, welcome to the Tripleten test community!'
            f'Please review the onboarding document here: [Onboarding Document](https://docs.google.com/document/d/e/2PACX-1vTSTZaIG_WdEsIvmHyUzmjNYgvq_rKFzGpt2bSYoq3_GlaiqhraMvbip4WM7xqBSs1Bvy-oQmO0KRl4/pub)'
        )


bot.run(os.getenv('DISCORD_BOT_TOKEN'))
