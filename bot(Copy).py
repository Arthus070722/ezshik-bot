import discord
from discord.ext import commands
import json
import requests
import os
from googleapiclient.discovery import build 
import random 
from googlesearch import search
from discord.ext.commands import BucketType
from io import BytesIO

TOKEN = 'TOKEN''
bot = commands.Bot(command_prefix='ёжик ')
api_key = "api_key"

@bot.command()
async def айпи(ctx):
    author = ctx.message.author
    await ctx.send('IP: 92.28.211.234 N: 43.7462 W: 12.4893 SS Number: 6979191519182016 IPv6: fe80:-5ded: ef69fb22-d9888 UPNP Enabled DMZ: 10.112.42.15 MAC: 5A:78.3E-7E:00 ISP: Ucom Unversal DNS: 8.8.8.8 ALT DNS: 1.1.1.8.1 DNS SUFFIX: Dlink WAN: 100.23.10.15 SUBNET MASK: 255.255.0.255 UDP OPEN PORTS: 8080, 80 TCP OPEN PORTS: 443 ROUTER VENDOR: ERICCSON DEVICE VENDOR: WIN32-X WAN TYPE: Private Nat GATEWAY: 192.168.0.1') 
    
@commands.cooldown(1, (6), commands.BucketType.user)
@bot.command(aliases=["show"])
async def картинка(ctx, *, search): 
    ran = random.randint(0, 9) 
    resource = build("customsearch", "v1", developerKey=api_key).cse() 
    result = resource.list( 
        q=f"{search}", cx="cx", searchType="image" 
    ).execute() 
    url = result["items"][ran]["link"] 
    embed1 = discord.Embed(title=f"")
    embed1.set_image(url=url) 
    await ctx.send(embed=embed1)

@bot.event    
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        embed = discord.Embed( 
            title = 'Ошибка!', 
            description = f'Подожди {error.retry_after :.0f} секунд', 
            colour = discord.Color.red() 
        )

        return await ctx.send(embed = embed)    
        
@bot.command(pass_context=True)
async def бен(ctx, arg):
    words_list = ["ughh", "ho ho ho", "no", "yes", "*повесил трубку*"]
    random_word = random.choice(words_list)
    print(random_word)
    await ctx.send(random_word)    
  
bot.run(TOKEN)