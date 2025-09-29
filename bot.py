import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
from keep_alive import keep_alive

# --- BOT SETUP ---
# Load environment variables from .env file
load_dotenv()

# It's highly recommended to use an environment variable for your token!
# Most hosting services have a section for "Secrets" or "Environment Variables".
TOKEN = os.getenv('DISCORD_TOKEN')

# Define the bot's intents. This is required.
# We need `message_content` to read messages.
intents = discord.Intents.default()
intents.message_content = True

# Create the bot instance with a command prefix and the defined intents.
bot = commands.Bot(command_prefix='!', intents=intents)

# Define the channel ID for the "alive" message
ALIVE_CHANNEL_ID = 1422237319754416259


# --- EVENTS ---
@bot.event
async def on_ready():
    """This function runs when the bot has successfully connected to Discord."""
    print(f'Bot is online and ready!')
    print(f'Logged in as: {bot.user.name}')
    print(f'Bot ID: {bot.user.id}')
    print('------')
    # Start the alive message loop
    send_alive_message.start()


# --- TASKS ---
@tasks.loop(minutes=10)
async def send_alive_message():
    """Sends an 'alive' message to the specified channel every 10 minutes."""
    channel = bot.get_channel(ALIVE_CHANNEL_ID)
    if channel:
        await channel.send("I'm alive!")
    else:
        print(f"Could not find channel with ID: {ALIVE_CHANNEL_ID}")


# --- COMMANDS ---
@bot.command()
async def ping(ctx):
    """A simple command that replies with Pong! to check if the bot is responsive."""
    await ctx.send('Pong! 🏓')


# --- RUN THE BOT ---
if TOKEN is None:
    raise ValueError("DISCORD_TOKEN environment variable not set. Please set it to your bot's token.")

keep_alive()
bot.run(TOKEN)