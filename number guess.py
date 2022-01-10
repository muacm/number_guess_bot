import discord
from discord.ext import commands
import random
import math

client = commands.Bot(command_prefix='!')

global count
count = 1

@client.command()
async def game(ctx, play : discord.Member):
	global x
	x = random.randint(1, 200)
	global player
	player = play
	print("\tYou've only ", round(math.log(200 - 1 + 1, 2)), " chances to guess the integer between 1 to 200!\n")
	embed = discord.Embed(title=f"You've only  {round(math.log(200, 2))} chances to guess the integer between 1 to 200!", colour=discord.Colour.random())
	await ctx.reply(embed=embed)



@client.command()
async def p(ctx, guess : int):
	global count
	global turn
	global player
	# while count < math.log(200, 2):

	turn = ctx.author

	if turn == player:
		if x == guess:
			print("Congratulations you did it in ", count, " try")
			embed = discord.Embed(title=f"Congratulations you did it in {count} try.\nPlease start a new game again", colour=discord.Colour.random())
			await ctx.reply(embed=embed)
			count = 1

		elif x > guess:
			print("You guessed too small!")
			await ctx.reply("You guessed too small!")
			count += 1

		elif x < guess:
			print("You Guessed too high!")
			await ctx.reply("You Guessed too high!")
			count += 1

	if count >= 8:
		print("\nThe number is %d" % x)
		print("\tBetter Luck Next time!")
		embed = discord.Embed(title=f"The number is {x}, Better Luck Next time!.\nPLease start a new game.", colour=discord.Colour.random())
		await ctx.reply(embed=embed)
		count = 1

	elif (turn!=player):
		await ctx.reply("It's not your turn so just sit & keep quite, don't jump in between.")




client.run('Your_bot_token')  





