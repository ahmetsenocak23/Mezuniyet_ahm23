import discord
import random
import os
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
    
    if message.content.startswith('-merhaba'):
        await message.channel.send("Merhaba benim ismim Mezun_Bot kullanabilecğin komutlar **\n -iklim değişikliği nedir \n -iklim değişikliği neden olur \n -iklim değişikliğini nasıl önleyebiliriz \n -iklim değişikliği fotoğrafları \n -iklim değişikliği insan sağlığını nasıl etkiler**")

    elif message.content.startswith('-komutlar'):
        await message.channel.send("-iklim değişikliği nedir \n-iklim değişikliği neden olur \n-iklim değişikliğini nasıl önleyebiliriz")

    elif  message.content.startswith('-iklim değişikliği nedir') or message.content.startswith('iklim değişikliği?'):
        await message.channel.send("nedeni ne olursa olsun iklimin ortalama durumunda ve/ya da değişkenliğinde onlarca yıl ya da daha uzun süre boyunca gerçekleşen değişiklikler")


    elif message.content.startswith('-iklim değişikliği neden olur'):
        await message.channel.send("En büyük nedenler **fabrika atıkları , egzozlar , yere atılan çöplerdir**") 


    elif message.content.startswith('-iklim değişikliğini nasıl önleyebiliriz') or message.content.startswith('-iklim değişikliğini nasıl önleyebilirim') or message.content.startswith('-iklim değişikliğini nasıl önlerim'):
        await message.channel.send("1. Sürdürülebilir Tarıma Destek Olun. Et ve süt üretimi sırasında, atmosfere büyük oranda karbon salınımı yapılıyor. \n 2. Uçak Kullanımızı Sınırlandırın \n 3. Yeşil Alanları Koruyun. \n 4. fosil yakıt kullanımınızı azaltın.")


    elif message.content.startswith('-iklim değişikliği fotoğrafları') or message.content.startswith('-iklim değişikliği foto') or message.content.startswith('-iklim foto'):
        foto = os.listdir('foto')
        rfoto = random.choice(foto)
        print(rfoto)
        with open(f'foto/{rfoto}', 'rb') as f:
            picture = discord.File(f)
        await message.channel.send(file=picture)

    elif message.content.startswith("-iklim değişikliği insan sağlığını nasıl etkiler"):
        await message.channel.send("İklimlerde meydana gelen değişiklikler sadece fiziksel sağlığı değil psikolojik sağlığı da önemli ölçüde etkilemektedir.\n İklim değişikliğinin sonucunda ortaya çıkan aşırı hava olayları ve doğal afetler, akut stres bozukluğu, travma sonrası stres bozukluğu ve depresyon\n gibi direk etkilere sebep olmaktadır")        





client.run('Gizli Token Buraya / Hidden Token İs Here')
