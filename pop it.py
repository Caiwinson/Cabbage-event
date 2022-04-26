import discord
from discord_components import DiscordComponents, Button, ButtonStyle
client=discord.Client()
DiscordComponents(client)
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
    if res.component.label=="Play":
        count=0
        b=[]
        for i in range(6):
            a=[]
            for j in range(6):
                count+=1
                a.append(Button(label=str(count), style=ButtonStyle.green))
            b.append(a)
    await res.respond("test", components=b)
@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await message.channel.send("test", components=[Button(label="Play", style=ButtonStyle.green)])
client.run(get_token())
