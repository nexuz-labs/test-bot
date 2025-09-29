import discord
from discord.ext import commands
import os

# --- BOT SETUP ---
# It's highly recommended to use an environment variable for your token!
# Most hosting services have a section for "Secrets" or "Environment Variables".
TOKEN = os.getenv('DISCORD_TOKEN')

# Define the bot's intents. This is required.
# We need `message_content` to read messages.
intents = discord.Intents.default()
intents.message_content = True

# Create the bot instance with a command prefix and the defined intents.
bot = commands.Bot(command_prefix='!', intents=intents)


# --- EVENTS ---
@bot.event
async def on_ready():
    """This function runs when the bot has successfully connected to Discord."""
    print(f'Bot is online and ready!')
    print(f'Logged in as: {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
    print('------')


# --- COMMANDS ---
@bot.command()
async def ping(ctx):
    """A simple command that replies with Pong! to check if the bot is responsive."""
    await ctx.send('Pong! 🏓')


# --- RUN THE BOT ---
if TOKEN is None:
    raise ValueError("DISCORD_TOKEN environment variable not set. Please set it to your bot's token.")

bot.run(TOKEN)