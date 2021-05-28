BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
END = "\033[0m"

import os
import asyncio
import discord
import aiohttp
import io
import random
import datetime
import time
import requests
import json
import requests
import traceback
import colorama
import shutil
from discord import webhook,AsyncWebhookAdapter
from discord.ext import commands
from os import system
import urllib.request

intents = discord.Intents.all()

with open("config.json") as f:
    config = json.load(f)

token = config.get("token")
Prefix = config.get("Prefix")

bot = commands.Bot(command_prefix = Prefix, self_bot = True, intents=intents)
start_time = datetime.datetime.utcnow()
bot.remove_command("help")

os.system("cls")

@bot.event
async def on_ready():
    UN = bot.user.name
    re = requests.get(f"https://ipinfo.io/json").json()
    os.system(F"title Element - Selfbot I Connected as {UN}")
    print(f"""
                         {END}╔════════════════════════════════════════════════════════════════════╗
                         {END}║                                                                    ║
  ░░░░░░░░░░█            {END}║   {LIGHT_RED}███████{RED}╗{LIGHT_RED}██{RED}╗     {LIGHT_RED}███████{RED}╗{LIGHT_RED}███{RED}╗   {LIGHT_RED}███{RED}╗{LIGHT_RED}███████{RED}╗{LIGHT_RED}███{RED}╗   {LIGHT_RED}██{RED}╗{LIGHT_RED}████████{RED}╗   {END}║  ░░░░░░░░░░█
  ░░░░░░░░▄▄█▄▄          {END}║   {LIGHT_RED}██{RED}╔════╝{LIGHT_RED}██{RED}║     {LIGHT_RED}██{RED}╔════╝{LIGHT_RED}████{RED}╗ {LIGHT_RED}████{RED}║{LIGHT_RED}██{RED}╔════╝{LIGHT_RED}████{RED}╗  {LIGHT_RED}██{RED}║╚══{LIGHT_RED}██{RED}╔══╝   {END}║  ░░░░░░░░▄▄█▄▄
  ░░░░▀▀▀██▀▀▀██▀▀▀      {END}║   {LIGHT_RED}█████{RED}╗  {LIGHT_RED}██{RED}║     {LIGHT_RED}█████{RED}╗  {LIGHT_RED}██{RED}╔{LIGHT_RED}████{RED}╔{LIGHT_RED}██{RED}║{LIGHT_RED}█████{RED}╗  {LIGHT_RED}██{RED}╔{LIGHT_RED}██{RED}╗ {LIGHT_RED}██{RED}║   {LIGHT_RED}██{RED}║      {END}║  ░░░░▀▀▀██▀▀▀██▀▀▀  
  ▄▄▄▄▄▄▄███████▄▄▄▄▄▄▄  {END}║   {LIGHT_RED}██{RED}╔══╝  {LIGHT_RED}██{RED}║     {LIGHT_RED}██{RED}╔══╝  {LIGHT_RED}██{RED}║╚{LIGHT_RED}██{RED}╔╝{LIGHT_RED}██{RED}║{LIGHT_RED}██{RED}╔══╝  {LIGHT_RED}██{RED}║╚{LIGHT_RED}██{RED}╗{LIGHT_RED}██{RED}║   {LIGHT_RED}██{RED}║      {END}║  ▄▄▄▄▄▄▄███████▄▄▄▄▄▄▄
  ░░█▄█░░▀██▄██▀░░█▄█    {END}║   {LIGHT_RED}███████{RED}╗{LIGHT_RED}███████{RED}╗{LIGHT_RED}███████{RED}╗{LIGHT_RED}██{RED}║ ╚═╝ {LIGHT_RED}██{RED}║{LIGHT_RED}███████{RED}╗{LIGHT_RED}██{RED}║ ╚{LIGHT_RED}████{RED}║   {LIGHT_RED}██{RED}║      {END}║  ░░█▄█░░▀██▄██▀░░█▄█    
                         {END}║   {RED}╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝      {END}║
                         {END}║                                                                    ║
                         {END}╚═════════════════════════════════╗╔═════════════════════════════════╝
                                                      {LIGHT_GRAY}[{RED}ID{LIGHT_GRAY}]{END} ║║ {LIGHT_GRAY}[{LIGHT_RED}{bot.user.id}{LIGHT_GRAY}]
                                                    {LIGHT_GRAY}[{RED}User{LIGHT_GRAY}]{END} ║║ {LIGHT_GRAY}[{LIGHT_RED}{UN}{LIGHT_GRAY}]
                                                  {LIGHT_GRAY}[{RED}Status{LIGHT_GRAY}]{END} ║║ {LIGHT_GRAY}[{LIGHT_RED}Online{LIGHT_GRAY}]
                                                  {LIGHT_GRAY}[{RED}Prefix{LIGHT_GRAY}]{END} ║║ {LIGHT_GRAY}[{LIGHT_RED}{Prefix}{LIGHT_GRAY}]
                         ╔═════════════════════════════════╝╚═════════════════════════════════╗
                         ║ {LIGHT_RED}Yanny#1970                                  burden/abby's acc#0523{END} ║
                         ╚════════════════════════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════
 """)

@bot.command()
async def help(ctx, category=None):
    await ctx.message.delete()
    if category is None:
        print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Help command executed")
        embed = discord.Embed(color=0xFF0000)
        embed.set_author(name="",
                         icon_url="")
        embed.set_thumbnail(url="")
        embed.set_image(url="")
        embed.add_field(name="`GENERAL`", value=f"{Prefix}help general", inline=False)
        embed.add_field(name="`IMAGE`", value=f"{Prefix}help image", inline=False)
        embed.add_field(name="`FUN`", value=f"{Prefix}help fun", inline=False)
        embed.add_field(name="`ACCOUNT`", value=f"{Prefix}help account", inline=False)
        embed.add_field(name="`MISC`", value=f"{Prefix}help misc", inline=False)
        embed.add_field(name="`TEXT`", value=f"{Prefix}help text", inline=False)
        await ctx.send(embed=embed)
    elif str(category).lower() == "general":
        embed = discord.Embed(color=0xFF0000)
        embed.set_image(url="")
        embed.description = f"`GENERAL COMMANDS`\n`> help <category>` - returns all commands of that category\n`> uptime` - return how long the selfbot has been running\n`> av <user>` - returns the user's pfp\n`> whois <user>` - returns user's account info\n`> copy` - makes a copy of the server\n`> swipe` - remove's all your message's in chat\n`> ri <role>` - give's info on specified role\n`> ping` - displays your ping"
        await ctx.send(embed=embed)
    elif str(category).lower() == "image":
        embed = discord.Embed(color=0xFF0000)
        embed.set_image(
            url="")
        embed.description = f"`IMAGE MANIPULATION COMMANDS`\n`> tweet <user> <message>` makes a fake tweet\n`> 8ball <Question>` - makes decisions for you"
        await ctx.send(embed=embed)
    elif str(category).lower() == "fun":
        embed = discord.Embed(color=0xFF0000)
        embed.set_image(
            url="")
        embed.description = f"`FUN COMMANDS`\n`> joke` - tell's you a joke\n`> kiss <user>` - kisses the specified user\n`> slap <user>` - slaps the specified user\n`> hug <user>` - hugs the specified user\n`> smug <user>` - send's gif\n`> pat <user>` - pat's your kitten"
        await ctx.send(embed=embed)
    elif str(category).lower() == "account":
        embed = discord.Embed(color=0xFF0000)
        embed.set_image(
            url="")
        embed.description = f"`ACCOUNT COMMANDS`\n`> fdmall ` - DM's everyone on your friend list\n`> sdmall <message>` - DM's everyone on a specific server cmd must be done in server \n`> listening <message>` - appears to listen to <message>\n`> watching <message>` - appears to be watching <message>\n`> game <message>` - appears to be playing <message>\n`> auto-bump <channel id>` - automatically bumps the server"
        await ctx.send(embed=embed)
    elif str(category).lower() == "misc":
        embed = discord.Embed(color=0xFF0000)
        embed.set_image(
            url="")
        embed.description = f"`MISC COMMANDS`\n`> copy` - create's copy of specified server\n`> spam <amount> <text>` - spam's message specified amount of times\n`> embedspam <amount> <text>` - spam's embed specified amount of times\n`> group-leaver` - Leave's all groups\n`> sc` - create's server\n`> fm` - get's first message in channel\n`> clear ` - places invis message to clear chat"
        await ctx.send(embed=embed)
    elif str(category).lower() == "text":
        embed = discord.Embed(color=0xFF0000)
        embed.set_image(
            url="")
        embed.description = f"`TEXT COMMANDS`\n`> ascii <text>` - turn's specified text to ascii\n`> shrug` - send's shrug emoji\n`> lenny` - send's lenny face\n`> tableflip` - send's tableflip emoji\n`> unflip` - send's unflip emoji\n`> bold <text>` - turn's text bold\n`> secret <text>` - hide's text\n"
        await ctx.send(embed=embed)


@bot.command()
async def swipe(message):
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Starting to clear message's")
    counter = 0
    async for message in message.channel.history(limit=1000):
        if message.author == bot.user:
            await message.delete()
            counter += 1
    embed = discord.Embed(color = 0xFF0000)
    embed.add_field(name="Element Clear", value="All Message's cleared", inline=False)
    end = await message.channel.send(embed=embed)
    await asyncio.sleep(5)
    await end.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Finished clearing message's")

@bot.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] AV command executed")
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format = format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file = discord.File(file, f"Avatar.{format}"))   


@bot.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] RoleInfo command executed")
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em) 


@bot.command()
async def whois(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] whois command executed")
    if user is None:
        user = ctx.author      
    date_format = "%a, %d %b %Y %I:%M %p"
    em = discord.Embed(description=user.mention)
    em.set_author(name=str(user), icon_url=user.avatar_url)
    em.set_thumbnail(url=user.avatar_url)
    em.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    em.add_field(name="Join position", value=str(members.index(user)+1))
    em.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        em.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    em.add_field(name="Guild permissions", value=perm_string, inline=False)
    em.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=em)


@bot.command()
async def copy(ctx):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Copy command executed")
    await bot.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in bot.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:                
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass


@bot.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()  
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Spam command executed")  
    for _i in range(amount):
        await ctx.send(message)

@bot.command()
async def embedspam(ctx,amount,*,text):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Embed Spam command executed")
    for _i in range(int(amount)):
        e = discord.Embed(title = f'**🚨 ALERT 🚨**',color = 0xFF0000)
        e.add_field(name="ALERT", value=f"{text}")
        await ctx.send(embed=e)


@bot.command()
async def uptime(ctx):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Uptime command executed")
    uptime = datetime.datetime.utcnow() - start_time
    uptime = str(uptime).split('.')[0]
    await ctx.send(f'`'+uptime+'`')


@bot.command(name='group-leaver', aliase=['leaveallgroups', 'leavegroup', 'leavegroups'])
async def _group_leaver(ctx):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Group-Leaver command executed")
    for channel in bot.private_channels:
        if isinstance(channel, discord.GroupChannel):
            await channel.leave()


@bot.command()
async def fdmall(ctx):
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Starting DMAll")
    Counter = 0
    for user in bot.user.friends:
        try:
            Counter = Counter + 1
            embed = discord.Embed(title="🚨 ALERT 🚨",color = 0xFF0000)
            embed.set_image(url="https://i.gifer.com/5HnJ.gif")
            embed.add_field(name="════════════════════", value=f"\n" + "I'm a dmall" + "\n" + "════════════════════" + "\n" + "    »  join for a free cookie and a kiss :kiss:" + "\n" + "    »  " + "\n" + "    » " + "\n" + "════════════════════" + "\n" + "» <dm all>" + "\n" + "════════════════════", inline=False)
            await user.send(embed=embed)
            print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"{LIGHT_GREEN}[LOG] Message Sent to {LIGHT_RED}{user.name}{END} {Counter}")
        except KeyError:
            print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"{RED}[ERROR] {LIGHT_RED}Message Failed{WHITE}")
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Finished DMAll")

@bot.command()
async def sdmall(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await asyncio.sleep(1)    
            await user.send(message)
        except:
            pass

@bot.command()
async def joke(ctx):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Joke command executed")
    headers = {
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])

@bot.command()
async def ascii(ctx, *, text):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Ascii command executed")
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")


@bot.command()
async def slap(ctx, user: discord.Member):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Slap command executed")
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def hug(ctx, user: discord.Member):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Hug command executed")
    r = requests.get("https://nekos.life/api/v2/img/hug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def smug(ctx, user: discord.Member):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Smug command executed")
    r = requests.get("https://nekos.life/api/v2/img/smug")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def pat(ctx, user: discord.Member):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Pat command executed")
    r = requests.get("https://nekos.life/api/v2/img/pat")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
async def kiss(ctx, user: discord.Member):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Kiss command executed")
    r = requests.get("https://nekos.life/api/v2/img/kiss")
    res = r.json()
    em = discord.Embed(description=user.mention)
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command(aliases=['markasread', 'ack'])
async def read(ctx):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Read command executed")
    for guild in bot.guilds:
        await guild.ack()


@bot.command()
async def shrug(ctx):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Shrug command executed")
    shrug = r'¯\_(ツ)_/¯'
    await ctx.send(shrug)

@bot.command()
async def lenny(ctx):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Lenny command executed")
    lenny = '( ͡° ͜ʖ ͡°)'
    await ctx.send(lenny)

@bot.command()
async def tableflip(ctx):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Tableflip command executed")
    tableflip = '(╯°□°）╯︵ ┻━┻'
    await ctx.send(tableflip)

@bot.command()
async def unflip(ctx):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Unflip command executed")
    unflip = '┬─┬ ノ( ゜-゜ノ)'
    await ctx.send(unflip)

@bot.command()
async def bold(ctx, *, message):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Bold command executed")
    await ctx.send('**'+message+'**')

@bot.command()
async def secret(ctx, *, message):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Secret command executed")
    await ctx.send('||'+message+'||')

@bot.command(aliases=["sc","SC"])
async def server_create(ctx):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Server create command executed")
    e = discord.Embed(color = 0xFF0000)
    e.add_field(name="Create Server",value="https://discord.new/qDXbBSE6FT2T" + "\n" + "https://discord.new/GFxJQQxXVb8g" + "\n" + "https://discord.new/ue3fGgqW8BS4" + "\n" + "https://discord.new/jdcDH9BQsgvB" + "\n" + "https://discord.new/RVMccvNvcMJ4")
    await ctx.send(embed=e)

def GenAddress(addy: str):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    four_char = ''.join(random.choice(letters) for _ in range(4))
    should_abbreviate = random.randint(0,1)
    if should_abbreviate == 0:
        if "street" in addy.lower():
            addy = addy.replace("Street", "St.")
            addy = addy.replace("street", "St.")
        elif "st." in addy.lower():
            addy = addy.replace("st.", "Street")
            addy = addy.replace("St.", "Street")
        if "court" in addy.lower():
            addy = addy.replace("court", "Ct.")
            addy = addy.replace("Court", "Ct.")
        elif "ct." in addy.lower():
            addy = addy.replace("ct.", "Court")
            addy = addy.replace("Ct.", "Court")
        if "rd." in addy.lower():
            addy = addy.replace("rd.", "Road")
            addy = addy.replace("Rd.", "Road")
        elif "road" in addy.lower():
            addy = addy.replace("road", "Rd.")
            addy = addy.replace("Road", "Rd.")
        if "dr." in addy.lower():
            addy = addy.replace("dr.", "Drive")
            addy = addy.replace("Dr.", "Drive")
        elif "drive" in addy.lower():
            addy = addy.replace("drive", "Dr.")
            addy = addy.replace("Drive", "Dr.")
        if "ln." in addy.lower():
            addy = addy.replace("ln.", "Lane")
            addy = addy.replace("Ln.", "Lane")
        elif "lane" in addy.lower():
            addy = addy.replace("lane", "Ln.")
            addy = addy.replace("lane", "Ln.")
    random_number = random.randint(1,99)
    extra_list = ["Apartment", "Unit", "Room"]
    random_extra = random.choice(extra_list)
    return four_char + " " + addy + " " + random_extra + " " + str(random_number)

@bot.command()
async def address(ctx, *, text):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Address command executed")
    addy = ' '.join(text)
    address_array = []
    i = 0
    while i < 10:
        address_array.append(GenAddress(addy))
        i+=1
    final_str = "\n".join(address_array)
    em = discord.Embed(description=final_str)
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(final_str)    

@bot.command()
async def tweet(ctx, username: str, *, message: str):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Tweet command executed")
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.set_image(url=res["message"])
            await ctx.send(embed=em)

@bot.command(name='8ball')
async def ball(ctx, *, question):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] 8ball command executed")
    responses = [
      'That is a resounding no',
      'It is not looking likely',
      'Too hard to tell',
      'It is quite possible',
      'That is a definite yes!',
      'Maybe',
      'There is a good chance'
    ]
    answer = random.choice(responses)
    embed = discord.Embed()
    embed.add_field(name="Question", value=question, inline=False)
    embed.add_field(name="Answer", value=answer, inline=False)
    embed.set_thumbnail(url="https://www.horoscope.com/images-US/games/game-magic-8-ball-no-text.png")
    await ctx.send(embed=embed)

@bot.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    print(f"{LIGHT_GREEN}"+"[{:%H:%M:%S}]".format(datetime.datetime.now()),f"{END}| {LIGHT_GREEN}[LOG]{END} First message command executed")  
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)

@bot.command(name='game')
async def game(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] game command executed")
    game = discord.Game(
        name=message
    )
    await bot.change_presence(activity=game)

@bot.command(name='listening')
async def listening(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Listening command executed")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name=message, 
        ))

@bot.command(name='watching')
async def watching(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Watching command executed")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, 
            name=message
        ))

@bot.command(name='auto-bump', aliases=['bump'])
async def _auto_bump(ctx, channelid): # b'\xfc'
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] auto bump command executed")
    count = 0
    while True:
        try:
            count += 1 
            channel = bot.get_channel(int(channelid))
            await channel.send('!d bump')           
            print(f'{Fore.BLUE}[AUTO-BUMP] {Fore.GREEN}Bump number: {count} sent'+Fore.RESET)
            await asyncio.sleep(7200)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)

@bot.command(name='clear')
async def clear(ctx): # b'\xfc'
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Clear command executed")
    await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')

@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    print("[{:%H:%M:%S}]".format(datetime.datetime.now()),f"| [LOG] Ping command executed")
    await ctx.send(f"Pong! {bot.latency*1000}ms")

#@bot.event
#async def on_command_error(ctx,error):
#    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
#        print(f"{RED}[ERROR] {END}Command doesn't exist")
#    if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
#        print(f"{RED}[ERROR] {END}Missing Argument")
#    if isinstance(error, discord.ext.commands.errors.CommandInvokeError):
#        print(f"{RED}[ERROR] {END}Missing Permission")

bot.run(token, bot = False)
