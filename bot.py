import os
import random
import lyricProg
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
from datetime import datetime
import threading

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print(TOKEN)
bot = commands.Bot(command_prefix='!')

highwaymenArr = ["Highwayman", "Sailor", "Dam Builder", "Starship", "Shotgun Rider", "River Gambler", "Mid-West Farmer", "American Indian"]

lyric = random.choice(lyricProg.lyrics)
hMan = random.choice(highwaymenArr)
@bot.command(name='quote', help="Displays the lyric of the day.")
async def quote(ctx):

    response = "The Highwayman/American Remains lyric of the day is: **" + lyric + "**"
    await ctx.send(response)

@bot.command(name='highwaymen', help="Displays all of the highwaymen.")
async def highwaymen(ctx):
    global highwaymenArr
    print(highwaymenArr)
    response = "The Highwaymen are **" +', '.join(highwaymenArr) +"**"
    await ctx.send(response)


@bot.command(name='add', help="Adds a highwaymen to the list of highwaymen.")
async def add(ctx, person):
    global highwaymen
    highwaymenArr.append(person)
    response = "**" + person + "** has been added to the highwaymen"
    await ctx.send(response)

@bot.command(name='remove', help="Removes a highwaymen from the list of highwaymen.")
async def add(ctx, person):
    global highwaymenArr
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
        response = "Please specify which song: '!lyrics h' or '!lyrics a'."
    if(song == "h"):
        response = ''.join(lyricProg.hLyrics)
    elif(song == "a"):
        response = ''.join(lyricProg.aLyrics)

    await ctx.send(response)

def checkTime():
    # This function runs periodically every 1 second
    threading.Timer(1, checkTime).start()

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    if(current_time == '00:00:00'):  # check if matches with the desired time
        global lyric
        global hMan
        global highwaymenArr
        lyric = random.choice(lyricProg.lyrics)
        hMan = random.choice(highwaymenArr)

checkTime()
bot.run(TOKEN)
