import discord, time, asyncio, random

client = discord.Client()

@client.event
async def on_ready():
    print("Logged on as {0}!".format(client))
    
i = 0

@client.event
async def on_message(message):
    global i
    pokemonList = [ENTER LIST OF POKEMON #'s! MAKE SURE EACH NUMBER IS INSIDE OF A ""!]
    channel = client.get_channel(ENTER CHANNEL ID)
    while True:
        if message.author.id == ENTER POKEMON BOT ID and message.channel.id == ENTER CHANNEL ID:
            for z in range(0, 1):
                title = message.embeds[0].title
                desc = message.embeds[0].description
                    #print(title)
                    #print(desc)
                name = "ENTER YOUR NICKNAME IN THE SERVER"
                level = "100"
                try:
                    if name in title and level in desc:
                        print("hello")
                        channel = client.get_channel(ENTER CHANNEL ID) 
                        await channel.send(f"p!select {pokemonList[i]}")
                        channel = client.get_channel(ENTER CHANNEL ID)
                        i += 1
                        print(i)
                        time.sleep(0.8)
                except:
                    pass
        await channel.send(random.randint(1, 1000000))
        time.sleep(0.8)

client.run("ENTER TOKEN", bot = False)
