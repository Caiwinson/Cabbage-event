import discord
from discord import app_commands
from discord.ext import commands

class Test(commands.Cog,name="Test"):
    def __init__(self,client):
        self.client=client
    @app_commands.command(name="create_canvas")
    async def create_canvas(self,interaction):
        await interaction.response.send_message(content="Ligma",ephemeral=False)
        msg=await interaction.original_message()
        print(msg.content)
async def setup(client):
    await client.add_cog(Test(client))