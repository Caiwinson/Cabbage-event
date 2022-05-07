import discord
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
client=commands.Bot(command_prefix='!')
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
    if res.message.id==972396378569457704:
        r={"Change Nickname": "Type the new nickname you want to change", "Announcement": "Type the Announcement you want to make\nYou can also provide a single Image", "Report": "Type the reason you want to report the user\nProvide both user id and Screenshot", "Suggestion": "Type the suggestion you want to make"}
        try:
            await res.author.send(r[res.component.label])
        except discord.errors.Forbidden:
            await res.respond(type=4,content="Please Enable DM's in your settings")
            return
        await res.respond(type=4,content="Check your DM's")
        def check(n):
            return n.author==res.author and n.channel.type==discord.ChannelType.private
        msg=await client.wait_for('message',check=check)
        embed=discord.Embed(title=res.component.label, description=msg.content, color=0x00ff00).set_author(name=str(res.author), icon_url=res.author.avatar_url)
        if res.component.label=="Announcement":
            await msg.reply("Would you like to ping <@&869132302746275882>", components=[Button(label="Yes", style=ButtonStyle.green), Button(label="No", style=ButtonStyle.red)])
            ping=await client.wait_for('button_click',check=check)
            embed.add_field(name="Ping", value=ping.component.label)
        if msg.attachments:
            embed.set_image(url=msg.attachments[0].url)
        await client.get_channel(956850251803791390).send(embed=embed.add_field(name="User ID", value=res.author.id))
@client.command()
async def test(ctx):
    await ctx.send("What would you Request for?", components=[Button(label="Change Nickname", style=ButtonStyle.blue, emoji="✏️"), Button(label="Announcement", style=ButtonStyle.green, emoji="📢"), Button(label="Report", style=ButtonStyle.red, emoji="📢"), Button(label="Suggestion", style=ButtonStyle.grey, emoji="📝")])
client.run(get_token())
