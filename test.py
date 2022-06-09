import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix=',', intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    # for i in client.users:
    #     if i.name == "notclone":
    #         print(i.id)
    #         await i.send("hello bitch")
    #         await i.send(file=discord.File('logo.png'), content="test")
    #         await client.close()
    user = await client.fetch_user("698554257221222451")
    await user.send("hello")
    await client.close()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('OTgyMDg5MDEyMzMwMjMzODU3.G_yHnN.GJdeFcua5Fhpz-etvHby5ib7kup1RqYPIhu_B0')
