import discord
import os.path
import random

COWBOT_TOKEN = os.environ['COWBOT_TOKEN']


# Nuevas líneas de código añadidas para la nueva versión de la api de discord 1.5.1
intent = discord.Intents(messages=True, guilds=True)
intent.members = True

# Imprimimos en pantalla para asegurarnos que estan en True
print(intent.members)

# Al definir el cliente damos como parametro los intents (intents=intent)
# Antes estaba asi client = discord.Client()
client = discord.Client(intents=intent)


# A partir de aqui ya todo es igual :)
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# Registers and triggers "on_message" event
@client.event
async def on_message(message):
    # If new messsage author is this bot, returns
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@client.event
async def on_member_join(member):
    categories = member.guild.categories 
    for category in categories:
        if category.name == "Text Channels":
            for channel in category.channels:
                if channel.name == "general":
                    print("Hola" + str(member))
                    file = discord.File("Hola.gif", filename = "hola.gif")
                    await channel.send("Hola" + str(member))
                    await channel.send(file=file)

client.run(COWBOT_TOKEN)  # Recuerden aqui poner su token entre parentesis