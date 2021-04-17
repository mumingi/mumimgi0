import discord


client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("무민기의 영원한 노예")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("아잇"):
        embed = discord.Embed(title="MuMinGi Bot 01", description="어 프르륵", color=0x00aaaa)
        msg = await message.channel.send(embed=embed)
        await msg.add_reaction(":heart:")
        await msg.add_reaction(":green_heart:")

    if message.content.startswith("!무민기"):
        await message.channel.send("우주최강귀여미")

    if message.content.startswith("/c"):
        ch = client.get_channel(int(message.content[3:21]))
        msg = message.content[22:]
        await ch.send(msg)

    if message.content.startswith("/e"):
        embed = discord.Embed(title="", description="", color=0x62c1cc)
        ch = client.get_channel(int(message.content[3:21]))
        msg = message.content[22:]
        embed.set_footer(text=msg)
        await ch.send(embed=embed)
        await message.channel.send(embed=embed)
        embed.add_field(name="소제목", value="설명", inline=True)


    if message.content.startswith("/dm"):
       author = message.guild.get_member(int(message.content[4:22]))
       msg = message.content[23:]
       await author.send(msg)

async def on_reaction_add(reaction, user):
    if user.bot == 1:
        return None
    if str(reaction.emoji) == ":heart:":
        await user.add_roles('GUEST')
    if str(reaction.emoji) == ":green_heart:":
        await message.channel.send("우주최강귀여미")



access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
