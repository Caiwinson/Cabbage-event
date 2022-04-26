import discord
print(discord.__file__)
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
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
        count=0
        b=[]
        for i in range(5):
            a=[]
            for j in range(5):
                count+=1
                a.append(Button(label=str(count), style=ButtonStyle.green, custom_id=str(res.author.id)))
            b.append(a)
        await res.respond(type=4,content="test", components=b)
@client.command()
async def test(ctx):
    await ctx.send("test", components=[Button(label="Play", style=ButtonStyle.green)])
client.run(get_token())
