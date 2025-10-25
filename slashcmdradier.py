import os
try:
    import discord
    from discord.ext import commands
    import asyncio
except:
    os.system('pip install discord.py asyncio')
    os.system('cls')
    print('restart the script it should work now')
    os.system('pause')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")

@bot.tree.command(name="sp", description="spam message")
async def raid(interaction: discord.Interaction):
    await interaction.response.send_message(",", ephemeral=True)

    await asyncio.sleep(1)

    for i in range(5):
        await interaction.followup.send("@everyone")
        await asyncio.sleep(0.5)

bot.run("enter your bot token here")

