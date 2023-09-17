import discord
from discord.ext import commands
from discordify import Spotify, emojify_image

bot = commands.Bot(
    command_prefix=",",
    intents=discord.Intents.all(),
    allowed_mentions=discord.AllowedMentions.none()
)

@bot.command(name="spotify")
async def _spotify(ctx: commands.Context, member: discord.Member = None):
    member = member or ctx.author
    client = Spotify(bot=bot, member=member)
    content, image, view = await client.get()
    await ctx.reply(content=content, file=image, view=view)


@bot.command(name="emojify")
async def _emojify(ctx, url: Union[discord.Member, str], size: int = 14):
    if not isinstance(url, str):
        url = url.display_avatar.url

    def get_emojified_image():
        r = requests.get(url, stream=True)
        image = Image.open(r.raw).convert("RGB")
        res = emojify_image(image, size)

        if size > 14:
            res = f"```{res}```"
        return res

    result = await bot.loop.run_in_executor(None, get_emojified_image)
    await ctx.send(result)


bot.run("token")