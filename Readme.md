# discordify

[![Downloads](https://static.pepy.tech/badge/cbvx)](https://pepy.tech/project/cbvx)

A Python package to retrieve detailed Spotify album images for Discord integration.



`example.py`
```py
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
```

### Comparision:

`discord`

![discord](https://media.discordapp.net/attachments/766518336329744415/1148991813399621773/IMG_20230906_201232.png?width=469&height=300)

`spotify mobile notification`
    
![notification](https://media.discordapp.net/attachments/766518336329744415/1148991813118595182/IMG_20230906_201113.jpg?width=541&height=406)


### Emojify

![](https://media.discordapp.net/attachments/743817386792058971/1152893621239021598/image.png?width=382&height=265)

*Emojify is directly taken and modified from [codewithswastik/emojify-bot](https://github.com/CodeWithSwastik/emojify-bot)*