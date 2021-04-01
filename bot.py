import os
import random
import lyricProg
import time
import discord
from discord.ext import commands, tasks
from dotenv import load_dotenv
from datetime import datetime
import threading
import asyncio
from pymongo import MongoClient

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
DB_URL = os.getenv('DATABASE_URL')
bot = commands.Bot(command_prefix='$')
time = datetime.now
highwaymenArr = ["Highwayman", "Sailor", "Dam Builder", "Starship Pilot", "Shotgun Rider", "River Gambler", "Mid-West Farmer", "American Indian"]
countArr = [4,0,0,3,0,1,1,0]
target_channel_id = 811297609577922590
line = random.choice(lyricProg.lyrics)
hMan = random.choice(highwaymenArr)



client = MongoClient(DBURL)


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
    global countArr
    if args:
        person = ' '.join(args)
        highwaymenArr.append(person)
        countArr.append(0)
        response = "**" + person + "** has been added to the highwaymen"
    else:
        response = "Please input a person to add"

    await ctx.send(response)

@bot.command(name='remove', help="Removes a highwayman from the list of highwaymen.")
async def remove(ctx, *args):
    global highwaymenArr
    global countArr
    if args:
        person = ' '.join(args)
        countArr.pop(highwaymenArr.index(person))
        highwaymenArr.remove(person)

        response = "**" + person + "** has been removed from the highwaymen"
    else:
        response = "Please input a person to remove"

    await ctx.send(response)

@bot.command(name='highwayman', help="Displays the highwayman of the day.")
async def highwayman(ctx):

    response = "The Highwayman of the day is: **" + hMan + "**"
    await ctx.send(response)

@bot.command(name='lyrics', help="Displays all the lyrics from Highwayman or American Remains. Use 'h' or 'a' after the lyrics commands to choose which song you would like to be displayed.")
async def lyrics(ctx, song=None):
    if song is None:
        response = "Please specify which song with **!lyrics h** or **!lyrics a**."
    if(song == "h"):
        response = ''.join(lyricProg.hLyrics)
    elif(song == "a"):
        response = ''.join(lyricProg.aLyrics)

    await ctx.send(response)

@bot.command(name='hotd', help= "Displays how many times each highwayman was highwayman of the day.")
async def hotd(ctx, *args):
    global highwaymenArr
    global countArr
    hwm = ' '.join(args)
    if args:
        if hwm in highwaymenArr:
            response = "**" + hwm + "** has been Highwayman of the Day **" + str(countArr[highwaymenArr.index(hwm)]) + "** times"
        else:
            response = "**" + hwm + "** is not a highwayman. Please input a highwayman"
    else:

        response = "__HOTD:__\n"
        for hwm in highwaymenArr:
            response += "**" + hwm + "**: " + str(countArr[highwaymenArr.index(hwm)]) +"\n"
    await ctx.send(response)
@tasks.loop(hours=24)
async def called_once_a_day():
    message_channel = bot.get_channel(target_channel_id)
    global line
    global hMan
    global highwaymenArr
    line = random.choice(lyricProg.lyrics)
    hMan = random.choice(highwaymenArr)
    print("Highwayman changed to " + hMan)
    print("Quote changed to " + line)
    countArr[highwaymenArr.index(hMan)] += 1;
    print(countArr)
    await message_channel.send("@here: Today's highwayman of the day is: **" + hMan + "**, and the line of the day is: **" + line + "**")
@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()
#
# daily.start()
bot.run(TOKEN)
