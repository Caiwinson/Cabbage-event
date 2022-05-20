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
        #code block
        pass
client.run(get_token())
