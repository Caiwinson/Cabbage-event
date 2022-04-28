import discord
from discord_components import DiscordComponents, Button, ButtonStyle
client=discord.ext.commands.Bot(command_prefix="-",intents=discord.Intents.all())
from PIL import Image
from PIL.ImageColor import getcolor
import random
from image import image_run
DiscordComponents(client)
db={}
count=1
while count<=25:
    db[str(count)]="#ff0000"
    count+=1
Image.new('RGB', (1000, 1000), (255, 255, 255)).save("C:/Users/User/Desktop/events/event codes/place/full.png")
print(db)
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
async def on_button_click(ctx):
    #a=b[(b.index(a)+1)%len(b)]
    image=Image.open("C:/Users/User/Desktop/events/event codes/place/full.png")
    #l=["red", "green", "blue", "yellow", "purple", "orange", "black", "white"]
    l=["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#ff8000", "#000000", "#ffffff"]
    b=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    for i in range(5):
        for j in range(5):
            print(b[i][j])
            if b[i][j]==int(ctx.component.label):
                image.paste(Image.new('RGB', (200,200), getcolor(db[ctx.component.label], "RGB")), (j*200,i*200))
                image.save("C:/Users/User/Desktop/events/event codes/place/full.png")
                db[ctx.component.label]=l[(l.index(db[ctx.component.label])+1)%len(l)]
                print(db[ctx.component.label])
                break
    await ctx.respond(type=7,content="http://192.168.100.15:8080/full.png")
@client.command()
async def test(ctx):
    id="".join(random.sample("qwertyuiopasdfghjklzxcvbnm", 8))
    count=0
    b=[]
    for i in range(5):
        a=[]
        for j in range(5):
            count+=1
            a.append(Button(label=str(count), style=ButtonStyle.green))
        b.append(a)
    msg=await ctx.send(content="http://192.168.100.15:8080/full.png", components=b)
    db["place"]={"id": msg.id, "c":{}}
    count=1
    while count<=25:
        db[str(count)]="#ff0000"
        count+=1
image_run()
client.run(get_token())
