import discord
from discord_components import DiscordComponents, Button, ButtonStyle, Select, SelectOption
client=discord.ext.commands.Bot(command_prefix="-",intents=discord.Intents.all())
from PIL import Image
from PIL.ImageColor import getcolor
import random
from image import image_run
DiscordComponents(client)
import os
def colour():
    return int(''.join([random.choice('0123456789ABCDEF') for j in range(6)]),16)
db={"place": {}}
Image.new('RGB', (1000, 1000), (255, 255, 255)).save("event codes/place/full.png")
def get_token():
    with open('token.txt', 'r') as f:
        return f.read()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
@client.command()
async def test(ctx):
    b=[]
    count=0
    for i in range(5):
        a=[]
        for j in range(5):
            count+=1
            a.append(Button(label="⠀", style=ButtonStyle.green, custom_id=str(count)))
        b.append(a)
    msg=await ctx.send(content="Based on reddit r/place", components=b)
    db["place"]={"id": msg.id, "user":{}}
    a=[]
    for i in ["white", "light-gray", "gray", "black", "pink", "red", "orange", "brown", "yellow", "lime", "green", "cyan", "cyan-blue", "blue", "lavender", "magenta"]:
        a.append(SelectOption(label=i, value=i, default=(i=="white")))
    await msg.reply(content="Select your colour choice",components=[Select(placeholder="Select a Colour", options=a)])
@client.event
async def on_select_option(res):
    c={"red": "#E50000", "green": "#02BE01", "blue": "#0000EA", "yellow": "#E5D900", "magenta": "#820080", "orange": "#E59500", "black": "#222222", "white": "#ffffff", "lime": "#94E044", "cyan": "#00D3DD", "cyan-blue": "#0083C7", "lavender": "#CF6EE4", "gray": "#888888", "light-gray": "#E4E4E4", "pink": "#FFA7D1", "brown": "#A06A42"}
    db["place"]["user"][str(res.author.id)]=c[res.values[0]]
    await res.respond(type=6)
@client.event
async def on_button_click(res):
    if res.message.id==db["place"]["id"]:
        if str(res.author.id) not in db["place"]["user"]:
            db["place"]["user"][str(res.author.id)]="#ffffff"
        id="".join(random.sample("qwertyuiopasdfghjklzxcvbnm", 8))
        image=Image.open("event codes/place/full.png")
        b=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
        dir=""
        for i in range(5):
            for j in range(5):
                if b[i][j]==int(res.component.id):
                    image.paste(Image.new('RGB', (200,200), getcolor(db["place"]["user"][str(res.author.id)], "RGB")), (j*200,i*200))
                    dir = 'event codes/place/place'
                    for f in os.listdir(dir):
                        os.remove(os.path.join(dir, f))
                    image.save("event codes/place/full.png")
                    image.save(f"event codes/place/place/{id}.png")
                    break
            if dir:
                break
        embed=discord.Embed(title="Kingdom of agony Global Art", colour=colour(), description=f'{res.author.mention}\n{j},{i}\n{db["place"]["user"][str(res.author.id)]}').set_image(url=f"http://192.168.100.15:8080/{id}.png")
        await res.respond(type=7,content="",embed=embed)
image_run()
client.run(get_token())
