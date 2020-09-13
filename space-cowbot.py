import discord
import os.path


COWBOT_TOKEN = os.environ['COWBOT_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	print (type(message.author))
	if message.author == client.user:
		return
	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
	categories = member.guild.categories
	for category in categories:
		if (category.name.lower() == "canales de texto") or (category.name.lower() == "text channels"):
			for channel in category.channels:
				if channel.name == "general":
					generalChannel = channel
				if channel.name == "reglas-para-jugar":
					rulesChannel = channel
	file = discord.File("hola.gif", filename = "hola.gif")
	await generalChannel.send("Hola " + member.mention + " bienvenido, " + "porfavor lee las " + rulesChannel.mention, file=file)

client.run(COWBOT_TOKEN)