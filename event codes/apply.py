import discord
print(discord.__file__)
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption
import random
import time
client=commands.Bot(command_prefix="-",intents=discord.Intents.all())
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
    if res.component.label == 'Join':
        id="".join(random.sample("qwertyuiopasdfghjklzxcvbnm", 8))
        count=0
        b=[]
        for i in range(5):
            a=[]
            for j in range(5):
                count+=1
                a.append(Button(label=str(count), style=ButtonStyle.green))
            b.append(a)
        await res.respond(type=4,content=id+ " ignore", components=b)
        def check(ctx):
            return ctx.message.content.startswith(id)
        ctx=await client.wait_for('button_click', check=check)
        part=ctx.component.label
        a=[]
        for i in ["ccp", "kinemaster", "flipaclip", "am", "live2d", "other"]:
            a.append(SelectOption(label=i, value=i))
        await ctx.respond(content=id+"\nWhat app do you use, just pick 1",type=7, components=[Select(placeholder="Select an app", options=a)])
        ctx=await client.wait_for('select_option', check=check)
        app=ctx.values[0]
        embed=discord.Embed(description=f"{res.author.mention} Application").add_field(name="Part", value=part, inline=False).add_field(name="App", value=app, inline=True).add_field(name="id", value=res.author.id, inline=False)
        await ctx.respond(embed=embed,content="Your application has been submitted\nPls wait for a while for the mod to pick your part",components=[])
        await client.get_channel(956850251803791390).send(embed=embed,components=[[Button(label="Accept", style=ButtonStyle.green), Button(label="Reject", style=ButtonStyle.red)]])
    elif res.component.label in ["Accept", "Reject"]:
        await res.respond(type=7, components=[Button(label=res.component.label+"ed", style=res.component.style,disabled=True)])
        await client.get_channel(956850251803791390).send(f"<@{res.message.embeds[0].fields[2].value}> has been {res.component.label}ed to part {res.message.embeds[0].fields[0].value}")
        if res.component.label=="Accept":
            db["m"][res.message.embeds[0].fields[0].value]={"user": res.message.embeds[0].fields[2].value, "part": res.message.embeds[0].fields[0].value, "status": "❌"}
@client.command()
async def test(ctx):
    await ctx.send("test", components=[Button(label="Join", style=ButtonStyle.green)])
client.run(get_token())