import discord, subprocess, shlex, bottoken
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print("Ready to get fucked")

@bot.command()
async def run(ctx, *args):
    forbidden = set(["rm", "mv", "cp", "su", "sudo", "touch", "doas", "cd", "zoxide", "pushd", "alias"])
    if len(set.intersection(set(args), forbidden)) != 0:
        await ctx.send("Naughty.")
        return
    elif args[0] == "ls" and len(args) > 1:
        await ctx.send("Don't try and snoop around my filesystem.")
        return
    try:
        command_result = subprocess.run(args, stdout=subprocess.PIPE).stdout.decode('utf-8')
        await ctx.send(f"```\n{command_result}\n```")
    except FileNotFoundError:
        await ctx.send(f"Command not found {args[0]}")

bot.run(bottoken.TOKEN)
