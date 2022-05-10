import discord
from PIL import Image, ImageDraw, ImageOps
from discord.ext import commands
import requests
client=commands.Bot(command_prefix='!', intents=discord.Intents.all())
def get_token():
    with open('token.txt', 'r') as f:
        return f.read()
table={ '0': 0, '1': 100, '2': 255, '3': 475, '4': 770, '5': 1150, '6': 1625, '7': 2205, '8': 2900, '9': 3720, '10': 4675, '11': 5775, '12': 7030, '13': 8450, '14': 10045, '15': 11825, '16': 13800, '17': 15980, '18': 18375, '19': 20995, '20': 23850, '21': 26950, '22': 30305, '23': 33925, '24': 37820, '25': 42000, '26': 46475, '27': 51255, '28': 56350, '29': 61770, '30': 67525, '31': 73625, '32': 80080, '33': 86900, '34': 94095, '35': 101675, '36': 109650, '37': 118030, '38': 126825, '39': 136045, '40': 145700, '41': 155800, '42': 166355, '43': 177375, '44': 188870, '45': 200850, '46': 213325, '47': 226305, '48': 239800, '49': 253820, '50': 268375, '51': 283475, '52': 299130, '53': 315350, '54': 332145, '55': 349525, '56': 367500, '57': 386080, '58': 405275, '59': 425095, '60': 445550, '61': 466650, '62': 488405, '63': 510825, '64': 533920, '65': 557700, '66': 582175, '67': 607355, '68': 633250, '69': 659870, '70': 687225, '71': 715325, '72': 744180, '73': 773800, '74': 804195, '75': 835375, '76': 867350, '77': 900130, '78': 933725, '79': 968145, '80': 1003400, '81': 1039500, '82': 1076455, '83': 1114275, '84': 1152970, '85': 1192550, '86': 1233025, '87': 1274405, '88': 1316700, '89': 1359920, '90': 1404075, '91': 1449175, '92': 1495230, '93': 1542250, '94': 1590245, '95': 1639225, '96': 1689200, '97': 1740180, '98': 1792175, '99': 1845195, '100': 1899250 }
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
@client.command()
async def rank(ctx, user:discord.Member=None):
    if user is None:
        user=ctx.author
    exp=requests.get(f"https://api.tatsu.gg/v1/guilds/869132302746275880/rankings/members/{user.id}/all", headers={"Authorization": "9ps9HkTEc5-UjGF4DY4YbIFicb2KQTE9L"}).json()["score"]
    def drawProgressBar(d, x, y, w, h, progress, bg="gray", fg="yellow"):
        # draw background
        d.ellipse((x+w, y, x+h+w, y+h), fill=bg)
        d.ellipse((x, y, x+h, y+h), fill=bg)
        d.rectangle((x+(h/2), y, x+w+(h/2), y+h), fill=bg)

        # draw progress bar
        w *= progress
        d.ellipse((x+w, y, x+h+w, y+h),fill=fg)
        d.ellipse((x, y, x+h, y+h),fill=fg)
        d.rectangle((x+(h/2), y, x+w+(h/2), y+h),fill=fg)
    for lvl, rexp in table.items():
        if exp >= rexp:
            level = int(lvl)
    current_exp=exp-table[str(level)]   
    next_exp=table[str(level+1)]-table[str(level)]
    progress=current_exp/next_exp
    img=Image.open('codes/rank/background.png')
    d=ImageDraw.Draw(img)
    avatar=Image.open(requests.get(user.avatar_url_as(format='png', size=256), stream=True).raw).convert('RGBA').resize((256,256))
    avatar = ImageOps.expand(avatar, border=5, fill=(255, 255, 255))
    avatar = avatar.resize((250, 250))
    img.paste(avatar, (42, 37), avatar)
    drawProgressBar(d, 100, 400, 800, 50, progress)
    img.save('codes/rank/rank.png')
    await ctx.send(file=discord.File('codes/rank/rank.png'))

client.run(get_token())
