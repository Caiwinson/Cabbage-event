from contextlib import suppress
import discord
from discord.ext import commands, tasks
import requests
from discord_components import DiscordComponents, Button, ButtonStyle
client=commands.Bot(command_prefix='!', intents=discord.Intents.all())
DiscordComponents(client)
import random
def get_token():
    with open('token.txt', 'r') as f:
        return f.read()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
@client.event
async def on_button_click(res):
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
        embed=discord.Embed(title="Who is this?").set_image(url="https://upload.wikimedia.org/wikipedia/commons/7/7a/MyAnimeList_Logo.png")
        await res.respond(type=7,content="Loading...",components=[],embed=embed)
        data=requests.get("https://animelist.caiwinson.repl.co/get").json()["data"]
        picked=random.choice(data)
        embed=discord.Embed(title="Who is this?").set_image(url=picked[1])
        buttons=[]
        for i in data:
            buttons.append(Button(label=i[0],style=ButtonStyle.blue))
        await msg.edit(embed=embed, components=buttons, content="")
        ctx=await client.wait_for("button_click", check=check)
        if ctx.component.label==picked[0]:
            embed=discord.Embed(title="You won", description=picked[0],colour=0x00ff00).set_image(url=picked[1])
        else:
            embed=discord.Embed(title="You lost", description=picked[0],colour=0xff0000).set_image(url=picked[1]).set_footer(text="You picked {}".format(ctx.component.label))
        await ctx.respond(type=7, embed=embed, components=[Button(label="Play Again", style=ButtonStyle.green), Button(label="Close", emoji="❌",style=ButtonStyle.red)], content="")
@client.command()
async def test(ctx):
    await ctx.send("test", components=[Button(label="Play")])
client.run(get_token())
