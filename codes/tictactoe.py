import discord
from discord.ext import commands
from discord_components import Button, ButtonStyle
import asyncio
import random
class TTT(commands.Cog, name="TTT"):
    def __init__(self, client):
        self.client=client
    @commands.Cog.listener()
    async def on_button_click(self,res):
        if res.component.label in ["Play", "Play Again"]:
            async def tictactoe(msg, player1,player2):
                def is_player_win(player):
                    win = None

                    n = len(board)

                    # checking rows
                    for i in range(n):
                        win = True
                        for j in range(n):
                            if board[i][j] != player:
                                win = False
                                break
                        if win:
                            return win

                    # checking columns
                    for i in range(n):
                        win = True
                        for j in range(n):
                            if board[j][i] != player:
                                win = False
                                break
                        if win:
                            return win

                    # checking diagonals
                    win = True
                    for i in range(n):
                        if board[i][i] != player:
                            win = False
                            break
                    if win:
                        return win

                    win = True
                    for i in range(n):
                        if board[i][n - 1 - i] != player:
                            win = False
                            break
                    if win:
                        return win
                    return False

                def is_board_filled():
                    for row in board:
                        for item in row:
                            if item == '-':
                                return False
                    return True
                async def board_msg():
                    b=""
                    buttons=[]
                    for i,y in zip(board,range(3)):
                        e=""
                        c=[]
                        for a,x in zip(i, range(3)):
                            e+=f":{a}:"
                            c.append(Button(label=a.replace("-", "⠀").upper(), style=ButtonStyle.green, disabled=a!="-", custom_id=f"{x} {y}"))
                        b+=e+"\n"
                        buttons.append(c)
                    if status.endswith("Win") or status.endswith("Tied"):
                        buttons=[]
                    embed=discord.Embed(description=f"{status}\n\n⭕={player1}\n❌={player2}")
                    embed.add_field(name="⠀", value=b.replace(":-:", "⬛"))
                    await msg.edit(embed=embed)
                    await player1_msg.edit(embed=embed,components=buttons, content="")
                    await player2_msg.edit(embed=embed,components=buttons, content="")
                player1=player1
                player2=player2
                board=[]
                for _ in range(3):
                    c=[]
                    for _ in range(3):
                        c.append("-")
                    board.append(c)
                player1_msg=m
                player2_msg=await player2.send("Please wait")
                await msg.edit(components=[])
                players={
                    "o": {"user": player1,"msg": player1_msg},
                    "x": {"user": player2,"msg": player2_msg}
                }
                cr=random.choice(["o", "x"])
                status=f"{players[cr]['user']} turns"
                await board_msg()
                while True:
                    ctx=await self.client.wait_for("button_click")
                    if ctx.message==players[cr]['msg']:
                        pass
                    elif ctx.message==players['x' if cr == 'o' else 'o']['msg']:
                        await ctx.respond(type=4, content="It's not your turn yet")
                        continue
                    else:
                        continue
                    await ctx.respond(type=6)
                    xy=ctx.component.id.split()
                    board[int(xy[1])][int(xy[0])]=cr
                    if is_player_win(cr):
                        status=f"{players[cr]['user']} Win"
                        await board_msg()
                        break

                    # checking whether the game is draw or not
                    if is_board_filled():
                        status="Game Tied"
                        await board_msg()
                        break
                    cr='x' if cr == 'o' else 'o'
                    status=f"{players[cr]['user']} turns"
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
                        break


def setup(client):
    client.add_cog(TTT(client))