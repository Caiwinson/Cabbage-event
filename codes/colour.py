import discord
from discord.ext import commands
import asyncio
from discord_components import DiscordComponents, Button, ButtonStyle
client=commands.Bot(command_prefix='!', intents=discord.Intents.all())
DiscordComponents(client)
import random
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
    if res.component.label in ["Play", "Play Again"]:
        if res.component.label == "Play":
            try:
                msg=await res.author.send("Are you ready", components=[Button(label="yes", style=ButtonStyle.green)])
            except discord.errors.Forbidden:
                await res.respond(type=4, content="Please enable DM's in your setting")
                return
            def check(m):
                return m.message==msg
            await res.respond(type=6)
            res=await client.wait_for('button_click', check=check)
        else:
            msg=res.message
            def check(m):
                return m.message==msg
        colours=["⚪", "⚫", "🔴", "🔵", "🟡", "🟢", "🟣", "🟤"]
        #pick 5 random circles
        picked_colours=random.sample(colours, 5)
        num=random.randint(3,5)
        order="".join(random.choices(picked_colours, k=num))
        embed=discord.Embed(title="Remember this, you have 5 seconds").add_field(name="⠀", value=order)
        await res.respond(type=7, embed=embed, components=[], content="")
        await asyncio.sleep(5)
        buttons=[[]]
        for i in picked_colours:
            buttons[0].append(Button(label="⠀", emoji=i, custom_id=i))
        embed=discord.Embed(title="Your turn", description="Enter the order of the circles you saw")
        await msg.edit(embed=embed, components=buttons)
        ans=""
        for e in range(num):
            ctx=await client.wait_for('button_click',check=check)
            ans+=ctx.component.id
            if e+1<num:
                embed=discord.Embed(title="Your turn", description="Enter the order of the circles you saw").add_field(name="⠀", value=ans)
                await ctx.respond(type=7, embed=embed)
        if ans==order:
            embed=discord.Embed(title="You won", description="You got it right",colour=0x00ff00).add_field(name="⠀", value=ans)
        else:
            embed=discord.Embed(title="You lost", description="You got it wrong",colour=0xff0000).add_field(name="Your colours", value=ans).add_field(name="Correct colours", value=order)
        await ctx.respond(type=7, embed=embed,components=[Button(label="Play Again", style=ButtonStyle.green)])
@client.command()
async def test(ctx):
    await ctx.send("test", components=[Button(label="Play")])
client.run(get_token())
