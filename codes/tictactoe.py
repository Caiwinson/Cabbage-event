import discord
from discord.ext import commands
from discord_components import Button, ButtonStyle
import asyncio
class TTT(commands.Cog, name="TTT"):
    def __init__(self, client):
        self.client=client
    @commands.Cog.listener()
    async def on_button_click(self,res):
        if res.component.label in ["Play", "Play Again"]:
            async def tictactoe(msg, player1,player2):
                player1=player1.id
                player2=player2.id
                board=[]
                for _ in range(3):
                    c=[]
                    for _ in range(3):
                        c.append("-")
                    board.append(c)
                async def board_msg():
                    status="HA"
                    b=""
                    for i in board:
                        e=""
                        for a in i:
                            e+=f":{a}:"
                        b+=e+"\n"
                    embed=discord.Embed(description=f"{status}")
                    embed.add_field(name="⠀", value=b.replace(":-:", "<:blank:872313293342138418>"))
                    await msg.edit(embed=embed)
                await board_msg()
            await res.respond(type=4,content="Check your DM")
            m=await res.author.send("Would you like to host or join a match", components=[[Button(label="Host", style=ButtonStyle.green), Button(label="Join", style=ButtonStyle.blue)]])
            a=await self.client.wait_for("button_click", check=lambda i:i.message==m)
            if a.component.label=="Join":
                await a.respond(type=7, content="You can join a match at <#998362117101068358>", components=[])
                await asyncio.sleep(60)
                await m.delete()
                return
            msg=await self.client.get_channel(998362117101068358).send(f"{res.author.mention} just hosted an Match", components=[Button(label="Join", style=ButtonStyle.green)])
            await a.respond(type=7,content="Please wait till somebody join your match", components=[Button(label="Cancel", emoji="❌", style=ButtonStyle.red)])
            while True:
                ctx=await self.client.wait_for("button_click")
                if ctx.message==m:
                    await msg.delete()
                    await ctx.respond(type=6)
                    await m.delete()
                    return
                elif ctx.message==msg:
                    if ctx.author==res.author:
                        await ctx.respond(type=4,content="you are not allowed to join your own match")
                    else:
                        await ctx.respond(type=4, content="Check your DM")
                        await msg.edit(content=f"Spectating {res.author.mention} vs {ctx.author.mention}")
                        await tictactoe(msg, res.author, ctx.author)


def setup(client):
    client.add_cog(TTT(client))