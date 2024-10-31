import discord
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('-hello'):
        await message.channel.send(f'Merhaba {client.user}! ben bir botum!')
    elif  message.content.startswith('-iklim değişikliği nedir'):
        await message.channel.send("nedeni ne olursa olsun iklimin ortalama durumunda ve/ya da değişkenliğinde onlarca yıl ya da daha uzun süre boyunca gerçekleşen değişiklikler")
    elif message.content.startswith('-iklim değişikliği neden olur'):
        await message.channel.send("En büyük nedenler **fabrika atıkları , egzozlar , yere atılan çöplerdir**") 
      
client.run('BURAYA TOKEN')
