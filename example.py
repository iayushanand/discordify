import discord
from discord.ext import commands
from discordify import spotify

bot = commands.Bot(command_prefix=",")

@bot.command(name="spotify")
async def spotif(ctx: commands.Context, member: discord.Member = None):
    member = member or ctx.author
    client = spotify.Spotify(bot=bot, member=member)
    content, image, view = await client.get()
    await ctx.reply(content=content, file=image, view=view)

bot.run("token")