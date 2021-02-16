import os
import random
import lyricProg
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
import threading
import asyncio

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='$')
time = datetime.now
highwaymenArr = ["Highwayman", "Sailor", "Dam Builder", "Starship", "Shotgun Rider", "River Gambler", "Mid-West Farmer", "American Indian"]


line = random.choice(lyricProg.lyrics)
hMan = random.choice(highwaymenArr)


@bot.command(name='quote', help="Displays the lyric of the day.")
async def quote(ctx):

    response = "The Highwayman/American Remains lyric of the day is: **" + line + "**"
    await ctx.send(response)

@bot.command(name='highwaymen', help="Displays all of the highwaymen.")
async def highwaymen(ctx):
    global highwaymenArr
    print(highwaymenArr)
    response = "The Highwaymen are **" +', '.join(highwaymenArr) +"**"
    await ctx.send(response)


@bot.command(name='add', help="Adds a highwayman to the list of highwaymen.")
async def add(ctx, *args):
    global highwaymen
    person = ' '.join(args)
    highwaymenArr.append(person)
    response = "**" + person + "** has been added to the highwaymen"
    await ctx.send(response)

@bot.command(name='remove', help="Removes a highwayman from the list of highwaymen.")
async def add(ctx, person):
    global highwaymenArr
    person = ' '.join(args)
    highwaymenArr.remove(person)
    response = "**" + person + "** has been removed from the highwaymen"
    await ctx.send(response)

@bot.command(name='highwayman', help="Displays the highwayman of the day.")
async def highwayman(ctx):

    response = "The Highwayman of the day is: **" + hMan + "**"
    await ctx.send(response)

@bot.command(name='lyrics', help="Displays all the lyrics from Highwayman or American Remains. Use 'h' or 'a' after the lyrics commands to choose which song you would like to be displayed.")
async def test(ctx, song=None):
    if song is None:
        response = "Please specify which song with **!lyrics h** or **!lyrics a**."
    if(song == "h"):
        response = ''.join(lyricProg.hLyrics)
    elif(song == "a"):
        response = ''.join(lyricProg.aLyrics)

    await ctx.send(response)
async def daily():
    await bot.wait_until_ready()
    channel = bot.get_channel(808789910621519883) # replace with channel ID that you want to send to
    msg_sent = False

    while True:
        if time().hour == 0 and time().minute == 0:
            if not msg_sent:
                global line
                global hMan
                global highwaymenArr
                line = random.choice(lyricProg.lyrics)
                hMan = random.choice(highwaymenArr)
                print("Highwayman changed to " + hMan)
                print("Quote changed to " + line)
                await channel.send("@everyone Today's highwayman of the day is: **" + hMan + "**, and the line of the day is **" + line + "**.")
                msg_sent = True
        else:
            msg_sent = False

    await asyncio.sleep(1)

bot.loop.create_task(daily())
bot.run(TOKEN)
