#Import module
import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button,ButtonStyle

#discord client
intents = discord.Intents.default()
intents.guilds=True
intents.messages=True
intents.members=True
client=commands.Bot(command_prefix="!", intents=intents)
def get_token():
    with open('token.txt', 'r') as f:
        return f.read()
DiscordComponents(client)
@client.event
async def on_ready():
    print(client.user)
@client.command(name="print")
async def rint(ctx,*,command):
    if ctx.author.id!=720900711260487681:
        return
    try:
        pr=eval(command)
    except Exception as ex:
        pr=f"{type(ex).__name__}: {ex.args[0]}"
    await ctx.reply(pr)
@client.command()
async def run(ctx, *,command):
    if ctx.author.id==720900711260487681:
        try:
            exec(command)
        except Exception as ex:
            await ctx.reply(f"{type(ex).__name__}: {ex.args[0]}")
        else:
            await ctx.message.add_reaction("✅")
@client.command()
async def load(ctx, cog):
    client.load_extension(f"codes.{cog}")
@client.command()
async def reload(ctx, cog):
    client.reload_extension(f"codes.{cog}")
@client.command()
async def test(ctx):
    await ctx.send("test", components=[Button(label="Play", style=ButtonStyle.green)])
client.run(get_token())