#Import module
import discord
from discord.ext import commands

#discord client
intents = discord.Intents.all()
client=commands.Bot(command_prefix="!", intents=intents)
def get_token():
    with open('token.txt', 'r') as f:
        return f.read()
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
    await client.load_extension(f"codes.{cog}")
@client.command()
async def reload(ctx, cog):
    await client.reload_extension(f"codes.{cog}")
client.run(get_token())