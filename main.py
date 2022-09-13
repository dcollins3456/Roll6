from unittest import result
import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import random

intents = nextcord.Intents.default()

client = commands.Bot(command_prefix = "!", intents=intents)

@client.event
async def on_ready():
    print("Roll6 bot is ready to roll.")
    print("---------------------------")

@client.slash_command(name="action", description="Make an Action Roll")
async def actionroll(interaction: Interaction, number:int):
    result = []
    res = ""
    #If rolling a 0, need to roll two dice
    if number < 1:
        num = 2
    #Limit input to 200 max, so as not to break any servers:    
    elif number > 200:
        num = 200
        res = "Limiting to 200 dice: "
    else:
        num = number
    for i in range(num):
        result.append(random.randint(1,6))
        if number < 1:
            result.sort()
        else:
            result.sort(reverse=True)
    #check for result fail/success/partial/crit
    if result[0] == 6 and result[1] == 6:
        if number > 0:
            res = res+"**CRITICAL!!** "
        else:
            res = res+"**Success!** "
    elif result[0] == 6 and result [1] != 6:
        res = res+"**Success!** "
    elif result[0] == 4 or result [0] == 5:
        res = res+"**Partial Success.** "
    elif result[0] < 4:
        res = res+"**Failure.** "
    
    await interaction.response.send_message(f'ACTION ROLL:\n{res}{result}')

@client.slash_command(name="fortune", description="Make a Fortune Roll")
async def actionroll(interaction: Interaction, number:int):
    result = []
    res = "Your result: "
    if number < 1:
        num = 2
    #Limit input to 200 max, so as not to break any servers:    
    elif number > 200:
        num = 200  
        res = "(Limiting to 200 dice): "  
    else:
        num = number
    for i in range(num):
        result.append(random.randint(1,6))
        if number < 1:
            result.sort()
        else:
            result.sort(reverse=True)
    #check for result fail/success/partial/crit
    if result[0] == 6 and result[1] == 6:
        if number > 0:
            res = res+"**Exceptional Result!!** Great/extreme effect."
        else:
            res = res+"**Good Result**. Standard, full effect."
    elif result[0] == 6 and result [1] != 6:
        res = res+"**Good Result**. Standard, full effect."
    elif result[0] == 4 or result [0] == 5:
        res = res+"**Mixed Result**. Limited, partial effect."
    elif result[0] < 4:
        res = res+"**Bad Result**. Poor, little effect."
    
    await interaction.response.send_message(f'FORTUNE ROLL:\n{res} {result}')

@client.slash_command(name="resist", description="Make a Resist Roll")
async def resistroll(interaction: Interaction, number:int):
    result = []
    res = ""
    if number < 1:
        num = 2
    #Limit input to 200 max, so as not to break any servers:    
    elif number > 200:
        num = 200
        res = "(Limiting to 200 dice): "
    else:
        num = number
    for i in range(num):
        result.append(random.randint(1,6))
        if number < 1:
            result.sort()
        else:
            result.sort(reverse=True)
    #check for result fail/success/partial/crit
    if result[0] == 6 and result[1] == 6:
        if number > 0:
            res = res+"**THAT WAS EASY!** Clear 1 stress! "
        else:
            res = res+"Take a total of **ZERO STRESS!** "
    elif result[0] == 6 and result [1] != 6:
        res = res+"Take a total of **ZERO STRESS!**"
    else:
        reduction = 6 - result[0]
        reduction = str(reduction)
        res = "Take a total of **"+reduction+" stress**."
    
    await interaction.response.send_message(f'RESIST ROLL:\n{res} {result}')

with open("token.0", "r", encoding="utf-8") as f:
    botkey = f.read()

client.run(botkey)