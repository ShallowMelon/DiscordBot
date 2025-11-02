import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf8', mode='w')
Intents = discord.Intents.default()
Intents.message_content = True
Intents.members = True

bot = commands.Bot(command_prefix='!', intents=Intents)

test_role = "Melon"

@bot.event
async def on_ready():
    print(f"A Legendary Melon have appeared!,{bot.username},Kneel before its presence!")

@bot.event
async def on_member_join(member):
    await member.send(f"Welcome to the server {member.name}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if "faggot" in message.content.lower():
        await message.delete()
        await message.channel.send(f"{message.author.mention} - no such words will be said!")

    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command()
async def assign(ctx):
    role = discord.utils.get(ctx.guild.roles,name=test_role)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"{ctx.author.mention} have been granted a {test_role}role")
    else:
        await ctx.send("No such role exist within this realm")

@bot.command()
async def remove(ctx):
    role = discord.utils.get(ctx.guild.roles,name=test_role)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"{ctx.author.mention} have been revoked of the {test_role} role!")
    else:
        await ctx.send("No such role exist within this realm")

@bot.command()
async def dm(ctx,*,msg):
    await ctx.author.send(f"Message: {msg}")

@bot.command()
async def reply(ctx):
    await ctx.reply("Hello")

@bot.command()
async def poll(ctx,*,msg):
    embed = discord.Embed(title="New Poll", description=question)
    poll_message = await ctx.send(embed=embed)
    await poll_message.add_reaction("✔️")
    await poll_message.add_reaction("❌")

@bot.command()
@commands.has_role(test_role)
async def Melon(ctx):
    await ctx.send("What has thou wished for thy presence")

@Melon.error
async def Melon_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("Thou are just a wretch staring heaven from hell!")

bot.run(token, log_handler=handler, log_level=logging.DEBUG)