
import discord
import urllib.request
import xml.etree.ElementTree as ET
from discord.ext import tasks

client = discord.Client()

token = "NzAyNzA5NjEzMTU3NTQ4MDk4.XqD_Uw.aDrkAf7RcqOmOHqYAA_gNWClEyQ"

@tasks.loop(minutes=1)
async def status():
    channel = client.get_channel(int("797887766801023014"))
    try:
        url = urllib.request.urlopen('http://localhost:7240/')
        xml = ET.parse(url)
        root = xml.getroot()
        whitelist = 0

        for name in [ './Name' ]:
            value1 = root.find(name);
            str1 = ET.tostring(value1, method="text").decode()
        for players in [ './NumberOfActivePlayers' ]:
            value2 = xml.find(players);
            str2 = ET.tostring(value2, method="text").decode()
        for mapa in [ '.MapName' ]:
            value3 = xml.find(mapa);
            str3 = ET.tostring(value3, method="text").decode()
        for passw in [ '.HasPassword' ]:
            value4 = xml.find(passw);
            str4 = ET.tostring(value4, method="text").decode()
            if 'Yes' in str4:
                whitelist = 1

        if (whitelist == 1):
            cor=0xf46a01
        else:
            cor=0x38b10b
        embed=discord.Embed(title="WarbandBot", color=cor)
        embed.set_author(name="WarbandBot", icon_url="https://media.moddb.com/images/mods/1/37/36148/Asset_23.png")
        embed.set_thumbnail(url="https://media.moddb.com/images/mods/1/37/36148/Asset_23.png")
        embed.add_field(name="Name", value=str1, inline=True)
        embed.add_field(name="Players", value=str2, inline=True)
        embed.add_field(name="Map", value=str3, inline=True)
        if (whitelist == 1):
            embed.add_field(name="Senha", value="Sim", inline=True)
            embed.set_footer(icon_url = 'https://i.pinimg.com/originals/72/a8/91/72a8910613b3df0b066ad2fabf1284a2.png', text='Ops... o servidor está com senha talvez esteja em testes') 
        else:
            embed.add_field(name="Senha", value="Não", inline=True)
        await channel.purge()
        await channel.send(embed=embed);
    except:
        embed=discord.Embed(title="WarbandBot", color=0xff0000)
        embed.set_author(name="WarbandBot", icon_url="https://media.moddb.com/images/mods/1/37/36148/Asset_23.png")
        embed.set_thumbnail(url="https://media.moddb.com/images/mods/1/37/36148/Asset_23.png")
        embed.add_field(name="Name", value="offline", inline=True)
        embed.add_field(name="Players", value="offline", inline=True)
        embed.add_field(name="Map", value="offline", inline=True)
        embed.add_field(name="Senha", value="offline", inline=True)
        await channel.purge()
        await channel.send(embed=embed)

@client.event
async def on_ready():
  print('Deu certo, {0.user}'.format(client))
  status.start()
client.run(token)

