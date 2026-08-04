import re
import discord
from discord import app_commands
from discord.ext import commands

discord.Intents.message_content = True

#Count Paths
badCountPath = "c:\\BADDMBot\\badDMCount.txt"
goodCountPath = "c:\\BADDMBot\\goodDMCount.txt"
cringeCountPath = "c:\\BADDMBot\\cringeDMCount.txt"
basedCountPath = "c:\\BADDMBot\\basedDMCount.txt"

token = "TOKEN HERE"
client = commands.Bot(command_prefix="/", intents=discord.Intents(messages=True, guilds=True))

#Syncs commands, starts bot
@client.event
async def on_ready():
    print(f"Bot logged in as {client.user}")
    try:
        synced = await client.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as err:
        print(err)

#Function to get specific count
def getCount(file):
     #Open file and get count
     with open(file, "r") as f:
         for line in f:
             pass
         #Get count and return (first number in last line)
         return int(re.search(r'\d+', line).group(0))

def writeCount(file, text):
    #Open file and write count and reason
    with open(file, "a") as f:
        f.write(text + "\n")


@client.tree.command(name="bad")
async def bad(interaction: discord.Interaction, reason: str):
    count = getCount(badCountPath) + 1
    writeCount(badCountPath, f"{count} - {reason}")

    await interaction.response.send_message(
        f"**BAD DM**: This is **BAD DM** number **{count}**\n"
        f"Reason: **{reason}**"
        "Read up on Reddit pal\n"
        "https://www.reddit.com/r/DnD/comments/6u1doa/what_makes_a_bad_dm/\n"
    )

@client.tree.command(name="good")
async def good(interaction: discord.Interaction, reason: str):
    count = getCount(goodCountPath) + 1
    writeCount(goodCountPath, f"{count} - {reason}")

    await interaction.response.send_message(
        f"**GOOD DM**: This is **GOOD DM** number **{count}**\n"
        f"Reason: **{reason}**"
    )

@client.tree.command(name="based")
async def based(interaction: discord.Interaction, reason: str):
    count = getCount(basedCountPath) + 1
    writeCount(basedCountPath, f"{count} - {reason}")

    await interaction.response.send_message(
        f"**BASED DM**: This is **BASED DM** number **{count}**\n"
        f"Reason: **{reason}**"
    )

@client.tree.command(name="cringe")
async def cringe(interaction: discord.Interaction, reason: str):
    count = getCount(cringeCountPath) + 1
    writeCount(cringeCountPath, f"{count} - {reason}")

    await interaction.response.send_message(
        f"**CRINGE DM**: This is **CRINGE DM** number **{count}**\n"
        f"Reason: **{reason}**"
    )

client.run(token)
