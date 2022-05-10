import discord
print(discord.__file__)
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption
import random
import time
db={"m":{"1":{"user":"723790474069934121","part":"1","status":"\u274c"},"2":{"user":"849906356660338689","status":"\u274c"},"3":{"user":"867455448936218684","status":"\u274c"},"4":{"user":"739509364037255223","status":"\u274c"},"5":{"user":"877868146931957760","status":"\u274c"},"6":{"user":"550761973277655046","status":"\u274c"},"7":{"user":"739509364037255223","status":"\u274c"},"8":{"user":723790474069934121,"status":"\u274c"},"9":{"user":723790474069934121,"status":"\u274c"},"10":{"user":"560849044713373696","status":"\u274c"},"11":{"user":939440004114038805,"status":"\u274c"},"12":{"user":939440004114038805,"status":"\u274c"},"13":{"user":712176200620965889,"status":"\u274c"},"14":{"user":"550761973277655046","status":"\u274c"},"15":{"user":"550761973277655046","status":"\u274c"},"16":{"user":"560849044713373696","status":"\u274c"},"17":{"user":467693698663186432,"status":"\u274c"},"18":{"user":467693698663186432,"status":"\u274c"},"19":{"user":467693698663186432,"status":"\u274c"},"20":{"user":718477228190728196,"status":"\u274c"},"21":{"user":718477228190728196,"status":"\u274c"},"22":{"user":718477228190728196,"status":"\u274c"},"23":{"user":696287458433826857,"status":"\u274c"},"24":{"user":"712176200620965889","part":"24","status":"\u274c"},"25":{"user":"712937293962543115","status":"\u274c"}}}
for i in range(26,65):
    db["m"][str(i)]=None
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
        count=25
        b=[]
        for i in range(5):
            a=[]
            for j in range(5):
                count+=1
                if db["m"][str(count)]:
                    d=True
                else:
                    d=False
                a.append(Button(label=str(count), style=ButtonStyle.green, disabled=d))
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
        await ctx.respond(type=7,embed=embed,content="Your application has been submitted\nPls wait for a while for the mod to pick your part",components=[])
        await client.get_channel(956850251803791390).send(embed=embed,components=[[Button(label="Accept", style=ButtonStyle.green), Button(label="Reject", style=ButtonStyle.red)]])
    elif res.component.label in ["Accept", "Reject"]:
        await res.respond(type=7, components=[Button(label=res.component.label+"ed", style=res.component.style,disabled=True)])
        await client.get_channel(956850251803791390).send(f"<@{res.message.embeds[0].fields[2].value}> has been {res.component.label}ed to part {res.message.embeds[0].fields[0].value}")
        if res.component.label=="Accept":
            db["m"][res.message.embeds[0].fields[0].value]={"user": res.message.embeds[0].fields[2].value, "part": res.message.embeds[0].fields[0].value, "status": "❌"}
    elif res.component.label=="Reload":
        if res.author.guild_permissions.administrator:
            desc=""
            for i in db["m"]:
                if db["m"][i]:
                    desc+=f"**Part {i}**\n<@{db['m'][i]['user']}> {db['m'][i]['status']}\n\n"
                else:
                    desc+=f"**Part {i}**\n-\n\n"
            embed=discord.Embed(title="Mep Parts", description=desc)
            co=[[Button(label="Join", style=ButtonStyle.green), Button(label="Reload", style=ButtonStyle.blue)],[Button(label="Mep Link", url="https://youtu.be/imJcFSJQF_8", style=ButtonStyle.URL)]]
            await res.respond(type=7,embed=embed, components=co)
        else:
            await res.respond(type=4, content="You don't have permission to do that")
@client.command()
async def test(ctx):
    embed=discord.Embed(title="Mep Parts")
    for i in db["m"]:
        if db["m"][i]:
            c=f"<@{db['m'][i]['user']}> {db['m'][i]['status']}"
        else:
            c="-"
        embed.add_field(name="Part "+i, value=c, inline=False)
    co=[[Button(label="Join", style=ButtonStyle.green), Button(label="Reload", style=ButtonStyle.blue)],[Button(label="Mep Link", url="https://youtu.be/yHTKIH1aNug", style=ButtonStyle.URL)]]
    await ctx.send(embed=embed, components=co)
client.run(get_token())