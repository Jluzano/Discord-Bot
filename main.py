import discord, os
from discord import Color
from discord.ext import commands
from webserver import keep_alive


# =========================================================

client = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

# =========================================================
# List of BTR songs
# Last value in each array:
# 1 = hitori, 2 = nijika, 3 = ryo, 4 = kita
song_list = [
  [
    "Seisyun Complex (青春コンプレックス)",
    'https://open.spotify.com/track/60nwK1iMgnFCznF6FiNfts?si=e161628087084ea7',
    'https://youtu.be/RWFW1OSlMkM', 4
  ],
  [
    "Lonely Tokyo/Hitoribocchi Tokyo (ひとりぼっち東京)",
    'https://open.spotify.com/track/1ZFnNl8O8zd4mef77SAd91?si=83dfd8de204d4074',
    'https://youtu.be/7TovqLDCosk', 4
  ],
  [
    "Distortion!!",
    'https://open.spotify.com/track/3l8rIBKJUDQFqQfKvcpQ1w?si=a79ff6fb442e4334',
    'https://youtu.be/c7oexOKsP6c', 4
  ],
  [
    "Secret Base/Himitsu Kichi (ひみつ基地)",
    'https://open.spotify.com/track/6P0RocRd21jJxs3E9vQoNH?si=4f152baaea6243b6',
    'https://youtu.be/ztF1ru7LEzs', 4
  ],
  [
    "Guitar, Loneliness and Blue Planet/Guitar to Kodoku to Aoihoshi (ギターと孤独と蒼い惑星)",
    'https://open.spotify.com/track/1rgncjmlpHMP3DBhpagyVb?si=6a0647f3296f444b',
    'https://youtu.be/fYBQJfPBmRg', 4
  ],
  [
    "I Can't Sing a Love Song/Love Song ga Utaenai (ラブソングが歌えない)",
    'https://open.spotify.com/track/5e9Pocvg3lRkVAsAKeiNio?si=b2ee4a5e1f1b4b54',
    'https://youtu.be/vW9d8-8gm7o', 4
  ],
  [
    "That Band/Ano Band (あのバンド)",
    'https://open.spotify.com/track/4Ji17AjAdjf83FsIDcXe0J?si=a263de531f8c4e66',
    'https://youtu.be/MtuFP3Tl1kE', 4
  ],
  [
    "Clatter/Karakara (カラカラ)",
    'https://open.spotify.com/track/1ofAXq6xfHjn6ZUxdsY3YW?si=d888a880e23b45ab',
    'https://youtu.be/3RWMMNsULsA', 3
  ],
  [
    "The Little Sea/Chiisana Umi (小さな海)",
    'https://open.spotify.com/track/54SWXjFN2XYo3G5YiNSCqd?si=57aab5c41e544ac6',
    'https://youtu.be/NF8c5pXx-Xc', 4
  ],
  [
    "What is Wrong With/Nani ga Warui (なにが悪い)",
    'https://open.spotify.com/track/2Ifn0MXm7x9ddBQPUabV9a?si=160530209ded4ffa',
    'https://youtu.be/h1uTWpCySRo', 2
  ],
  [
    "Never Forget/Wasurete Yaranai (忘れてやらない)",
    'https://open.spotify.com/track/5ISHFvPLUqKz2JfDRtwnb2?si=7608564a8d494d9e',
    'https://youtu.be/8Selo-P1Ovc', 4
  ],
  [
    "If I Could Be a Constellation/Seiza ni Naretara (星座になれたら)",
    'https://open.spotify.com/track/1iNhNmEwrd2TP4XrV7pQBI?si=bc9c33088e5f4163',
    'https://youtu.be/-LwBbLa_Vhc', 4
  ],
  [
    "Flashbacker (フラッシュバッカー)",
    'https://open.spotify.com/track/2qdPWFrknWyLXYIPpbtAgD?si=1d1b6d6a90a644c5',
    'https://youtu.be/ecVnw_SiREQ', 4
  ],
  [
    "Rockn' Roll, Morning Light Falls on You/Korogaru Iwa, Kimi ni Asa ga Furu (転がる岩、君に朝が降る)",
    'https://open.spotify.com/track/6wH2RsJUO8oypx8c5PG0bP?si=4ad2c6c54d0f4c66',
    'https://youtu.be/H7ZyZdqLb5Q', 1
  ],
  [
    "Into the Light/Hikari no Naka e (光の中へ)",
    'https://open.spotify.com/track/5pRchw0E4RpVqIWcyVCrJv?si=467b78b9378846c6',
    'https://youtu.be/omckrS77vDo', 4
  ],
  [
    "Blue Spring and Western Sky/Aoi Haru to Nishi no Sora (青い春と西の空)",
    'https://open.spotify.com/track/7hfOYw1pDISWok8ZR8JALg?si=13279620bc1447d0',
    'https://youtu.be/BN1ofrqIl9I', 4
  ],
]

# =========================================================
# Discord user IDs
my_id = MYID
jacob = JACOBSID
server_id = SERVERID
text_channel_id = TEXTCHANNEL
# =========================================================


@client.event
async def on_ready():
  print(
    "Bot is running...\n========================================================="
  )
  # Change bot activity
  activity = discord.Activity(type=discord.ActivityType.listening,
                              name="kessoku band 🔥")
  await client.change_presence(activity=activity)


# =========================================================


# Sends an image when a certain someone joins the vc
@client.event
async def on_voice_state_update(member, before, after):
  global my_id, jacob
  capyCon = discord.utils.get(client.guilds, id=GUILDID)  # ID of the server to check
  channelId = 1019430551154872320  # ID of the channel to send the message to
  channel = client.get_channel(channelId)
  
  if member.voice and member.voice.channel and before.channel is None and member.id == jacob:
    if member.voice.channel.guild.id == capyCon.id:
      print("Printing...")
      await channel.send("https://tenor.com/view/jacob-is-online-jacob-chad-zato-zato1-gif-21626204")
  elif before.channel and after.channel is None and member.id == jacob:
    print("See ya jacob")
    await channel.send("https://tenor.com/view/jd-jd-leaving-gif-19432511")
  
  # For debugging purposes
  if member.voice and member.voice.channel and before.channel is None and member.id == my_id:
    print("Working!")
  elif before.channel and after.channel is None and member.id == my_id:
    print("You left the voice chat.")


# =========================================================


# Get a list of all of kessoku band's songs
@client.command()
async def songlist(ctx):
  "Returns a list of all kessoku band songs"
  global song_list
  embed1 = discord.Embed(title="Hitori Gotoh", color=Color(int("FFC0CB", 16)))
  embed2 = discord.Embed(title="Nijika Ijichi", color=Color(int("FFFF00", 16)))
  embed3 = discord.Embed(title="Ryo Yamada", color=Color(int("0000FF", 16)))
  embed4 = discord.Embed(title="Ikuyo Kita", color=Color(int("FF0000", 16)))

  for song in song_list:
    name = song[0]
    spotify = song[1]
    youtube = song[2]

    if song[3] == 1:
      embed1.add_field(name=f"{name}",
                       value=f"[Spotify]({spotify})\n[YouTube]({youtube})",
                       inline=False)
    elif song[3] == 2:
      embed2.add_field(name=f"{name}",
                       value=f"[Spotify]({spotify})\n[YouTube]({youtube})",
                       inline=False)
    elif song[3] == 3:
      embed3.add_field(name=f"{name}",
                       value=f"[Spotify]({spotify})\n[YouTube]({youtube})",
                       inline=False)
    elif song[3] == 4:
      embed4.add_field(name=f"{name}",
                       value=f"[Spotify]({spotify})\n[YouTube]({youtube})",
                       inline=False)

  await ctx.send(embed=embed1)
  await ctx.send(embed=embed2)
  await ctx.send(embed=embed3)
  await ctx.send(embed=embed4)


# =========================================================


# Gets a user's profile picture
@client.command()
async def pfp(ctx, user: discord.Member):
  "Grabs a mentioned user's profile picture"
  # Get the user's avatar URL
  avatar_url = user.avatar.with_size(1024)
  # Send the avatar URL as a message
  await ctx.send(avatar_url)


# =========================================================

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
