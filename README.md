# HighwaymanBot
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
![Maintaner](https://img.shields.io/badge/Maintainer-benjam9-red)
[![GitHub release](https://img.shields.io/github/release/benjam9/HighwaymanBot)](https://GitHub.com/benjam9/HighwaymanBot/releases/)

This bot requires the following python libraries: ```discord``` ```python-dotenv``` ```asyncio```

The commands for this bot follow this syntax: `$<command> <arguments>`

| Command | Description
|---------|-------------|
| $help | Displays commands |
| $lyrics a/h | Sends a message with the lyrics of Highwaymen or American Remains |
| $quote | Sends a message with the line of the day |
| $highwayman | Sends a message with the highwayman of the day |
| $highwaymen | Displays all current highwaymen |
| $add person | Adds a name to the current highwaymen |
| $remove person | Removes a name from the current highwaymen |

The bot will @everyone with the updated highwayman and line daily

To run the bot follow these instructions:
1. Follow the process of making a bot with the discord API [here.](https://discordpy.readthedocs.io/en/latest/discord.html)
2. Clone this repo and create a .env file in the repository and add ```TOKEN = '[DISCORD BOT TOKEN]'```
3. Run ```python bot.py```


### TODO
- [ ] Add characters/items/places/events that users can collect as cards.
- [ ] Add images for each card.
- [ ] Add database that stores each user's cards.
- [ ] Add points system for each user that are gained by listening to Highwayman or American Remains (1000 points each play).
- [ ] Add the ability to unlock a random card for 10,000 points, a card from a certain song for 15,000 points, or a specific card for 20,000
- [ ] Add a system where users can spend points and the bot will them a highwaymen when they send a message, e.g, ```^ This guy's a sailor!```
- [ ] Add a quiz game for the lyrics with the difficulties: Bandit - Multiple Choice. Soldier - Fill in the blank. Highwayman - Find an incorrect line in a certain amount of time. 
