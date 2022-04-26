import discord
print(discord.__file__)
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
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
    if res.component.label == 'Play':
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
        s=time.time()
        def check(ctx):
            return ctx.message.content.startswith(id)
        while count>1:
            ctx=await client.wait_for('button_click', check=check)
            #replace the 24th button with a red button
            for i in range(5):
                for j in range(5):
                    if b[i][j].label==ctx.component.label:
                        b[i][j].style=ButtonStyle.red
                        b[i][j].disabled=True
                        break
            count-=1
            await ctx.respond(type=7, components=b)
        ctx=await client.wait_for('button_click', check=check)
        for i in range(5):
            for j in range(5):
                if b[i][j].label==ctx.component.label:
                    b[i][j].style=ButtonStyle.red
                    b[i][j].disabled=True
                    break
        await ctx.respond(type=7, content=str(round(time.time()-s, 2)) + " seconds",components=b)
@client.command()
async def test(ctx):
    await ctx.send("test", components=[Button(label="Play", style=ButtonStyle.green)])
client.run(get_token())
