import nextcord
import random
from nextcord.ext import commands

punching_gifs = ["https://c.tenor.com/b9aXVS6p7ucAAAAC/edens-zero-shiki-granbell.gif","https://i.imgur.com/g91XPGA.gif","https://i.imgur.com/7jErgl1.gif","https://i.imgur.com/hlqNBXp.gif","https://i.imgur.com/jznCcr2.gif","https://i.imgur.com/f2kkp3L.gif", "https://i.imgur.com/cgMbUYX.gif", "https://i.imgur.com/pX1E9uU.gif", "https://i.imgur.com/hODM1tI.gif", "https://i.imgur.com/e4bi40y.gif"]
punching_names = ['Knocks You Out!', 'Punches You!', 'Destroys Your Skull!']

kick_gifs = ['https://c.tenor.com/LEgnGzli8VMAAAAC/anime-fight.gif', 'https://c.tenor.com/7te6q4wtcYoAAAAC/mad-angry.gif', 'https://c.tenor.com/2l13s2uQ6GkAAAAM/kick.gif', 'https://c.tenor.com/QxoBMmf2bRwAAAAC/jormungand-anime.gif', 'https://c.tenor.com/f1mFGp6vujkAAAAd/charlotte-window-kick-anime-kick.gif',
             'https://c.tenor.com/kvxt9X-gXqQAAAAC/anime-clannad.gif', 'https://c.tenor.com/D67kRWw_cEEAAAAC/voz-dap-chym-dap-chym.gif', 'https://c.tenor.com/EcdG5oq7MHYAAAAM/shut-up-hit.gif', 'https://c.tenor.com/Lyqfq7_vJnsAAAAC/kick-funny.gif', 'https://c.tenor.com/4zwRLrLMGm8AAAAM/chifuyu-chifuyu-kick.gif']
kick_names = ['Boots You!', 'Kicks You!']

class ActionGifs(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def punch(self, ctx: commands.Context,):
        embed = nextcord.Embed(
            colour=nextcord.Colour(0xCE3011),
            description=f"{ctx.author.mention} {(random.choice(punching_names))}"

        )
        embed.set_image(url=(random.choice(punching_gifs)))

        await ctx.send(embed=embed)

    @commands.command(name='kick', aliases=['kicks'])
    async def kick(self, ctx: commands.Context):
        embed = nextcord.Embed(
            colour=(nextcord.Colour(0xE42C47)),
            description=f"{ctx.author.mention} {(random.choice(kick_names))}"
        )
        embed.set_image(url=random.choice(kick_gifs))

        await ctx.send(embed=embed)
