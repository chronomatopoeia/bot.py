import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='-')


@bot.command()
async def hello(ctx):
    await ctx.reply(f'Hello {ctx.author.mention} 👋!')

@bot.command()
async def love(ctx):
    await ctx.reply(f'I love you {ctx.author.mention} ❤!')

@bot.command()
async def goodbye(ctx):
    await ctx.reply(f"Goodbye {ctx.author.mention} 👋!")
    
@bot.command()
async def add(ctx, num1 : int, num2 : int):
    await ctx.reply(num1+num2)

@bot.command()
async def subtract(ctx, num3 : int, num4 : int):
    await ctx.reply(num3-num4)   

@bot.command()
async def guide(ctx):
    embed=discord.Embed(title= 'NebulaBot Basic Commands', description= 'These are all the commands to get started using Nebulabot! ')
    embed.add_field(name= '-hello', value= 'NebulaBot says hello!', inline=False)
    embed.add_field(name= '-goodbye', value= 'Nebula says goodbye!', inline=False)
    embed.add_field(name= '-love', value= 'NebulaBot says I love you', inline=False)
    embed.add_field(name= '-guide', value= 'Brings up the commands and features of NebulaBot', inline=False)
    embed.add_field(name= '-add', value= 'add two numbers together and get the sum (Ex. -add 1 1, NebulaBot: 2)', inline=False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/998599136091840562/998701707229921421/NebulaBot_Logo.png')
    await ctx.reply(embed=embed)
    
@bot.event
async def on_ready():
    print('I am running!')


bot.run(TOKEN)
