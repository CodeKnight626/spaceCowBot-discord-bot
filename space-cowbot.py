import discord
import os.path
import random

COWBOT_TOKEN = os.environ['COWBOT_TOKEN']
#New addition for compatibility with new discord python api verison
intent = discord.Intents(messages=True, guilds=True)
intent.members = True # Subscribe to the privilged memebers intent.\
print(intent.members)

WHITE_LIST_MEMBER = ["CodeKnight#3703", "Space Cowboy#7179", "lap#1225"]
WHITE_LIST_MEMBER_NUMBER = [504219755327258636, 475560429624492032]#754541836315525222 CodeKnight code
client = discord.Client(intents=intent)

members_status = {}

channels = {}#CANALES DE TEXTO}

@client.event
async def on_ready():
   
    """for guild in client.guilds:
        print(guild.name)
        for category in guild.categories:
            for channel in category.channels:
                channels[f"{channel.guild}_{channel.category.name}_{channel.name}"] = channel.id
    print(channels)"""


    for guild in client.guilds:
        for member in guild.members:
            members_status[member.id] = 0
    print('We have logged in as {0.user}'.format(client))

# Registers and triggers "on_message" event
@client.event
async def on_message(message):

    # If new messsage author is this bot, returns
    if message.author == client.user:
        return
    # Get the member who sent the message
    member = message.author

    # If the message contains "hola" send greetings gif image
    if message.content.lower().find('hola') != -1:
        file = discord.File(f"images/cowboy-hola-{random.randint(1,2)}.gif", filename = "cowboy-hola.gif")
        await message.channel.send(member.mention, file=file)


    # Check if the comment contains the "!kick" command
    if message.content.startswith('!kick'):
        # Check if the user who sent the command has permission to kick a user 
        if message.author.id in WHITE_LIST_MEMBER_NUMBER:
            #Creates a list with the users to kick
            for userToKick in message.mentions:
                # Send terminator gif and kisck the users
                file = discord.File("images/hasta-la-vista.gif", filename = "hasta-la-vista.gif")
                await message.channel.send(userToKick.mention, file=file)
                await message.guild.kick(userToKick)
                await message.channel.send(".\n.\n.")
                await message.channel.send(str(userToKick.name) + " ha sido exterminado") 
        #If the user has no permission to kick, the bots sends a message notifying it
        else:
            file = discord.File("images/spit.gif", filename = "spit.gif")
            await message.channel.send("No tienes permiso para kickear", file=file)

    # When the "!canales" command is sent it displays all the categories and channels
    if message.content.startswith('!canales'):
        for category in message.guild.categories:
            print(category.mention)
            await message.channel.send(category.mention)
            for channel in category.channels:
                print("---" + channel.mention)
                await message.channel.send("---" + channel.mention)


# Registers and triggers this event when a user joins the guild and sends a gif image
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
    file = discord.File("images/hola.gif", filename = "hola.gif")
    await generalChannel.send("Hola " + member.mention + " bienvenido, " + "porfavor lee las " + rulesChannel.mention, file=file)


# Registers and triggers when a member updates its profile
@client.event
async def on_member_update(memberBefore, memberAfter):
    # Check for none activity or spotify to 
    if not((memberAfter.activity == None) or (memberAfter.activity.name == "Spotify")):
        if memberAfter.guild.name == "LAP FAMILY":
            categories = memberAfter.guild.categories
            if (memberAfter.activity.name == "Among Us") and (members_status[memberAfter.id] == 0):
                await memberAfter.guild.get_channel(751894176190300252).send(memberAfter.name + " está jugando Among Us")
            if (memberAfter.activity.name == "Fall Guys") and (members_status[memberAfter.id] == 0):
                await memberAfter.guild.get_channel(753080335427829921).send(memberAfter.name + " está jugando Fall Guys")
            members_status[memberAfter.id] = 1
    else:

       members_status[memberAfter.id] = 0

        
        

client.run(COWBOT_TOKEN)