import discord
from discord import app_commands

TOKEN = "YOUR_BOT_TOKEN_HERE"

class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # This runs every time the bot starts
        print("Syncing slash commands...")
        synced = await self.tree.sync()  # Global sync
        print(f"Synced {len(synced)} command(s)")

client = MyClient()

@client.tree.command(name="ping", description="Replies with Pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")

@client.tree.command(name="hello", description="Says hello to you")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Hello, {interaction.user.mention}!"
    )

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("------")

client.run(TOKEN)
