import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
from random import randint
import asyncio
import time
client=commands.Bot(command_prefix='!', intents=discord.Intents.all())
def get_token():
    with open('token.txt', 'r') as f:
        return f.read()
@client.event
async def on_ready():
    DiscordComponents(client)
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
@client.event
async def on_button_click(res):
    print(res)
    if res.component.label in ["Play", "Play Again"]:
        if res.component.label == "Play":
            try:
                msg=await res.author.send("Are you ready", components=[Button(label="yes", style=ButtonStyle.green)])
            except discord.errors.Forbidden:
                await res.respond(type=4, content="Please enable DM's in your setting")
                return
            def check(m):
                return m.message==msg
            await res.respond(type=6)
            res=await client.wait_for('button_click', check=check)
        else:
            msg=res.message
            def check(m):
                return m.message==msg
@client.command()
async def test(ctx):
    await ctx.send("test", components=[Button(label="Play", style=ButtonStyle.green)])
client.run(get_token())
